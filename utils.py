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

    return f1_posneg_macro, f1_macro, na_coeff


def parse_model_response_universal(response):
    """universal parser for all models"""

    if 'choose from: positive, negative, neutral.' in response.lower():
        response = response.lower().split('choose from: positive, negative, neutral.')[1].strip()
    else:
        response = response.lower()

    if any(e in response for e in ['neutral', 'нейтральн']):
        return 'neutral'
    elif any(e in response for e in ['positiv', 'позитивн']):
        return 'positive'
    elif any(e in response for e in ['negativ', 'негатив']):
        return 'negative'
    else:
        return 'neutral (na)'

