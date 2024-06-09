from collections import OrderedDict, Counter

from sklearn.metrics import f1_score

# Not available result constant.
NEUTRAL_NA = 'neutral (na)'

SENTIMENT_CLASS_TO_UINT_PRESET = {'neutral': 0, 'negative': -1, 'positive': 1, NEUTRAL_NA: 0}
SENTIMENT_CLASS_TO_STR_PRESET = {0: "neutral", -1: "negative", 1: "positive"}


def calculate_metrics(pred, etalon, do_format_predict_labels=True, do_format_etalon_labels=True):
    assert(isinstance(pred, list))
    assert(isinstance(etalon, list))
    assert(len(pred) == len(etalon))

    na_coeff = round(pred.count(NEUTRAL_NA) / len(pred) * 100, 2)

    if do_format_predict_labels:
        pred = [SENTIMENT_CLASS_TO_UINT_PRESET[elem] for elem in pred]
    if do_format_etalon_labels:
        etalon = [SENTIMENT_CLASS_TO_UINT_PRESET[elem] for elem in etalon]

    f1_macro = round(f1_score(etalon, pred, average='macro') * 100, 2)
    f1_posneg_macro = round(f1_score(etalon, pred, average='macro', labels=[1, -1]) * 100, 2)

    return OrderedDict({
        "f1pn": f1_posneg_macro,
        "f1pn0": f1_macro,
        "no_ans_rate": na_coeff
    })


def parse_model_response_universal(response, ctr_log=None):
    """universal parser for all models"""
    assert (isinstance(ctr_log, Counter) or ctr_log is None)

    prefixes = [
        'choose from: positive, negative, neutral.',
        "выбери из трех вариантов: позитивная, негативная, нейтральная."
    ]

    # Lowercase response first.
    response = response.lower()

    # Seeking for the prompt prefix.
    p_ind = -1
    for ind, prefix in enumerate(prefixes):
        if prefix in response:
            p_ind = ind
            break

    if ctr_log is not None:
        ctr_log["_prompts-removed"] += 1 if p_ind > -1 else 0

    # Removing the presence of the prompt in the generated answer.
    response = response.split(prefixes[p_ind])[1].strip() if p_ind > -1 else response

    if any(e in response for e in ['neutral', 'нейтральн']):
        label = 'neutral'
    elif any(e in response for e in ['positiv', 'позитивн']):
        label = 'positive'
    elif any(e in response for e in ['negativ', 'негатив']):
        label = 'negative'
    else:
        label = 'neutral (na)'

    if ctr_log is not None:
        ctr_log[f"answer-{label}"] += 1

    return label
