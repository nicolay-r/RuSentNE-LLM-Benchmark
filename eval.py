import argparse
from os.path import basename, join

from src.sqlite_provider import SQLiteProvider
from utils import parse_model_response_universal, calculate_metrics


def predict_from_sqlite(sqlite_filepath, table, col_answers):
    columns = SQLiteProvider.get_columns(target=sqlite_filepath, table=table)
    col_answers = columns[-1] if col_answers is None else col_answers
    responses = list([r[0] for r in SQLiteProvider.read(target=sqlite_filepath, column_names=[col_answers], table=table)])
    predictions_str = list(map(lambda r: parse_model_response_universal(response=r), responses))
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
            return k_to_text[k], join(dir, filename)


def md_link_value(text, link):
    return f"[{text}]({link})"


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--sources', dest='sources', nargs="+", default=None)
    parser.add_argument('--csv-sep', dest='csv_sep', type=str, default='\t')
    parser.add_argument('--answer-col', dest='answer_col', type=str, default=None)

    args = parser.parse_args()

    predict_source = {
        "sqlite": lambda source: predict_from_sqlite(source, table="contents", col_answers=args.answer_col),
    }

    label_source = {
        "sqlite": lambda source: labels_from_sqlite(source, col_labels="label"),
    }

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
        prompt_md_text, prompt_path = file_to_prompt(source=source_name, lang=lang, dir="data")

        line = [m_name] + \
               [lang] + \
               [md_link_value(text=prompt_md_text, link=prompt_path)] + \
               list(eval_result) + \
               [md_link_value(text="answers", link=s)]

        print(",".join([str(r) for r in line]))
