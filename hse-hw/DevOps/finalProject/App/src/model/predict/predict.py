import pickle
import random

build_model =  "src/model/pickles/model.pkl"
build_vectorizer = "src/model/pickles/vectorizer.pkl"


def get_prediction_ml(new_data: str):
    # Load the model
    with open(build_model, 'rb') as f:
        clf = pickle.load(f)

    # Load the vectorizer
    with open(build_vectorizer, 'rb') as f:
        vectorizer = pickle.load(f)

    new_data_arr = [new_data]
   
    X_new = vectorizer.transform(new_data_arr)
    y_pred = clf.predict(X_new) 
    return y_pred[0]



def get_prediction_keywords(new_data: str):
    positive_words = ['love', 'happy', 'joy', 'great', 'excited', 'kind', 'amazing', 'fantastic', 'wonderful', 'good', 'great', 'excellent', 'beautiful', 'awesome', 'fun', 'fabulous', 'smile', 'laugh', 'grateful', 'thankful', 'blessed', 'cheerful', 'glad', 'pleased', 'satisfied', 'content', 'delightful', 'enjoyable', 'thrilled', 'elated', 'blissful', 'euphoric', 'upbeat', 'positive', 'optimistic']
    negative_words = ["abandoned", "aberration", "hate", "abhor", "abject", "abominable", "abrasive", "abscond", "absence", "absurd", "abuse", "accident", "accursed", "accusation", "accuse", "acerbic", "aching", "acrid", "acrimonious", "afraid", "aggravate", "aggression", "aggressive", "agonize", "agonizing", "agony", "ailment", "alarm", "alienate", "allergic", "aloof", "amiss", "amputate", "anarchism", "anarchist", "anger", "angry", "anguish", "annihilate", "annoy", "annoyance", "anomalous", "antagonism", "antagonize", "anxiety", "anxious", "apathetic", "apathy", "appalling", "apprehension", "apprehensive", "arbitrary", "archaic", "arduous", "argumentative", "arrogance", "ashamed", "asinine", "aspersion", "assail", "assassin", "assassination", "assault", "astray", "asunder", "atrocious", "atrocities", "atrophy", "attack", "audacious", "austere", "authoritarian", "autocrat", "autocratic", "avarice", "aversion", "awful", "awkward", "ax", "babble", "backache", "backbite", "backslider", "bad", "bad-tempered", "baffle", "balky", "banal", "baneful", "banned", "barbarian", "barbaric", "barbarous", "barren", "base", "battered", "batty", "beastly"]

    positive_words_cnt = 0 
    negative_words_cnt = 0 

    word_token = new_data.strip().split(" ")

    for token in word_token: 
        if token in positive_words:
            positive_words_cnt += 1
        elif token in negative_words: 
            negative_words_cnt += 1
    
    if positive_words_cnt > negative_words_cnt:
        return "positive"
    elif positive_words_cnt < negative_words_cnt:
        return "negative"
    else: 
        return random.choice(["negative", "positive"]) 

