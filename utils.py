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


def parse_model_response_universal_closest(response, ctr_log=None):
    """ This is the revised version of assessment.
        That counts the first entry.
    """
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

    def try_reg_label(r, entries, to, v):
        for e in entries:
            e_ind = r.find(e)
            if e_ind >= 0:
                to.append([v, e_ind])
                break

    # Here we collect all the possible entries.
    labels = []
    try_reg_label(response, entries=['neutral', 'нейтральн'], to=labels, v="neutral")
    try_reg_label(response, entries=['positiv', 'позитивн'], to=labels, v='positive')
    try_reg_label(response, entries=['negativ', 'негатив'], to=labels, v='negative')

    if len(labels) == 0:
        labels.append(['neutral (na)', 0])

    labels = sorted(labels, key=lambda item: item[1], reverse=False)

    # logging the case of multiple answers presence.
    if len(labels) > 1:
        ctr_log["_multiple_answers"] += 1

    # Collecting the actual answer.
    answer = labels[0][0]

    if ctr_log is not None:
        ctr_log[f"answer-{answer}"] += 1

    return answer


def parse_model_response_universal_original(response, ctr_log=None):
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
