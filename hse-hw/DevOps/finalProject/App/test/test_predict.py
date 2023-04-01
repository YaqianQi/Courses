from src.model.predict.predict import get_prediction_keywords, get_prediction_ml

def test_get_prediction_ml():
    # # Make predictions on new data
    positive_data = 'This movie is great'
    output = get_prediction_ml(positive_data)
    assert output == "positive"

    negative_data = 'I hate this product.'

    output = get_prediction_ml(negative_data)
    assert output == "negative"


def test_get_prediction_keywords():
    # # Make predictions on new data
    positive_data = 'This movie is great'
    output = get_prediction_keywords(positive_data)
    assert output == "positive"

    negative_data = 'I hate this product.'

    output = get_prediction_keywords(negative_data)
    assert output == "negative"
