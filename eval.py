import argparse
from os.path import basename

from src.sqlite_provider import SQLiteProvider
from utils import parse_model_response_universal, calculate_metrics


def predict_from_sqlite(sqlite_filepath, table, col_answers):
    columns = SQLiteProvider.get_columns(target=sqlite_filepath, table=table)
    col_answers = columns[-1] if col_answers is None else col_answers
    responses = list([r[0] for r in SQLiteProvider.read(target=sqlite_filepath, column_names=[col_answers], table=table)])
    predictions_str = list(map(lambda r: parse_model_response_universal(response=r), responses))
    return predictions_str


def labels_from_sqlite(source, col_labels):
    labels = list([int(r[0]) for r in SQLiteProvider.read(target=source, column_names=[col_labels], table="contents")])
    return labels


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
        prefix, m_name = basename(s).split('.csv_')
        line = [m_name] + (['en' if 'en' in prefix else "ru"]) + list(eval_result) + [f"[answers]({s})"]
        print(",".join([str(r) for r in line]))
