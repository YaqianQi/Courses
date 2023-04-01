import requests

def test_predict_ml():
    url = 'http://127.0.0.1:5000/predict_ml'
    data = {'text': 'I love this product.'}
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, json=data, headers=headers)
    sentiment = response.json()
    assert sentiment["prediction"] ==  'positive' 


    url = 'http://127.0.0.1:5000/predict_ml'
    data = {'text': 'I hate this product.'}
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, json=data, headers=headers)
    sentiment = response.json()
    assert sentiment["prediction"] ==  'negative' 


def test_predict_keywords():
    url = 'http://127.0.0.1:5000/predict_keywords'
    data = {'text': 'I love this product.'}
    headers = {'Content-Type': 'application/json'}

    response = requests.get(url, json=data, headers=headers)
    sentiment = response.json()
    assert sentiment["prediction"] ==  'positive' 


    url = 'http://127.0.0.1:5000/predict_keywords'
    data = {'text': 'I hate this product.'}
    headers = {'Content-Type': 'application/json'}

    response = requests.get(url, json=data, headers=headers)
    sentiment = response.json()
    assert sentiment["prediction"] ==  'negative' 