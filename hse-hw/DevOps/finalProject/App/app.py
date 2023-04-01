# export PYTHONPATH="${PYTHONPATH}:/Users/aliciaqi/Desktop/learnspace/DevOps Final" 
import logging
from flask import Flask, request, jsonify


from src.model.predict.predict import get_prediction_keywords, get_prediction_ml

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the sentiment analysis API!"


@app.route('/predict_ml', methods=['POST'])
def predict_ml():
    text = request.get_json()['text']
    
    try: 
        prediction = get_prediction_ml(text)
    except Exception as e: 
        logging.info(f"Proper solution failed: {e}")
        raise("Sentiment prediction based on machine learning methods is not available. Please try later.")
    
    output = jsonify({'prediction': prediction})  


    return output


@app.route('/predict_keywords', methods=['GET'])
def predict_keywords():
    text = request.get_json()['text']
    
    try:
        prediction = get_prediction_keywords(text)  
    except Exception as e:
        logging.info(f"Fallback solution failed: {e}")
        raise("Sentiment prediction based on keyworkd methods is not available. Please try later.")
    
    output = jsonify({'prediction': prediction})  
    return output 


if __name__ == '__main__':
    app.run(debug=True)