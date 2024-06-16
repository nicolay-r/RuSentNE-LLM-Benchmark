import argparse
from collections import Counter
from os.path import basename, join

from src.sqlite_provider import SQLiteProvider
from utils import parse_model_response_universal_closest, calculate_metrics, parse_model_response_universal_original


def predict_from_sqlite(sqlite_filepath, table, col_answers, eval_f, do_log=False):
    columns = SQLiteProvider.get_columns(target=sqlite_filepath, table=table)
    col_answers = columns[-1] if col_answers is None else col_answers
    responses = list([r[0] for r in SQLiteProvider.read(target=sqlite_filepath, column_names=[col_answers], table=table)])
    ctr_log = Counter() if do_log else None
    predictions_str = list(map(lambda r: eval_f(response=r, ctr_log=ctr_log), responses))
    if ctr_log is not None:
        print(ctr_log)
    return predictions_str


def labels_from_sqlite(src_filepath, col_labels):
    data = SQLiteProvider.read(target=src_filepath, column_names=[col_labels], table="contents")
    labels = list([int(r[0]) for r in data])
    return labels


def file_to_prompt(source, lang, dir):

    # Mapping dictionary.
    m_dict = {
       "ru": {"_prompt": "prompt_v2_ru.txt"},
       "en": {"_prompt": "prompt_v2_en.txt",
              "-thor-cot": "thor_cot_schema.json"},
    }

    # key to text.
    k_to_text = {
        "_prompt": "zero-shot",
        "-thor-cot": "CoT THoR"
    }

    for k, filename in m_dict[lang].items():
        if k in source:
            return k_to_text[k], join(dir, filename), k


def md_link_value(text, link):
    return f"[{text}]({link})"


eval_funcs = {
    "default": parse_model_response_universal_original,
    "closest": parse_model_response_universal_closest,
    "closest-qwen": lambda **kwargs: parse_model_response_universal_closest(
        forced_patterns={"without expressing": "neutral"}, **kwargs),
}


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--sources', dest='sources', nargs="+", default=None)
    parser.add_argument('--csv-sep', dest='csv_sep', type=str, default='\t')
    parser.add_argument('--answer-col', dest='answer_col', type=str, default=None)
    parser.add_argument('--eval-mode', dest='eval_mode', type=str, default="closest", choices=list(eval_funcs.keys()))
    parser.add_argument('--no-lang', dest="no_lang", action='store_true', default=False)
    parser.add_argument('--no-prompt-link', dest="no_prompt_link", action='store_true', default=False)
    parser.add_argument('--no-answer-link', dest="no_answer_link", action='store_true', default=False)
    parser.add_argument('--metrics', dest="metrics", nargs="+", type=str, default=["f1pn", "f1pn0", "no_ans_rate"])
    parser.add_argument('--prompts', dest="prompts", nargs="+", type=str, default=["_prompt", "-thor-cot"])
    parser.add_argument('--sort-column', dest="sort_column", type=int, default=0)

    args = parser.parse_args()


    print("Evaluation mode: {}".format(args.eval_mode))

    predict_source = {
        "sqlite": lambda source: predict_from_sqlite(source, table="contents", col_answers=args.answer_col, 
                                                     eval_f=eval_funcs[args.eval_mode], do_log=True),
    }

    label_source = {
        "sqlite": lambda source: labels_from_sqlite(source, col_labels="label"),
    }

    lines = []
    for s in args.sources:
        assert(isinstance(s, str))

        # The case of the inferred from the LLM results.
        ext = s.split('.')[-1]
        predictions = predict_source[ext](s)
        etalon = label_source[ext](s)

        if predictions is None:
            continue

        assert(len(predictions) == len(etalon))

        eval_result = calculate_metrics(pred=predictions, etalon=etalon,
                                        do_format_predict_labels=True,
                                        do_format_etalon_labels=False)

        # Displaying results.
        source_name = basename(s)
        prefix, m_name = source_name.split('.csv_')
        lang = 'en' if 'en' in prefix else "ru"
        prompt_md_text, prompt_path, prompt_template = file_to_prompt(source=source_name, lang=lang, dir="data")

        if prompt_template not in args.prompts:
            continue

        # Remove prompt template from name.
        m_name = m_name.split(prompt_template)[0]

        line = [m_name] + \
               ([lang] if not args.no_lang else []) + \
               ([md_link_value(text=prompt_md_text, link=prompt_path)] if not args.no_prompt_link else []) + \
               list([v for k, v in eval_result.items() if k in args.metrics]) + \
               ([md_link_value(text="answers", link=s)] if not args.no_answer_link else [])

        lines.append(line)

    # Sort the output.
    sorted(lines, key=lambda item: item[args.sort_column])

    # Output everything.
    for line in lines:
        print("|".join([str(r) for r in line]))
