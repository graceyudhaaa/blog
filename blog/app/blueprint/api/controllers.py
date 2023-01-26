from flask import Blueprint, jsonify, request, Response
from ...utils import (
    load_tokenizer_from_json,
    text_cleaning_stopword_in_not_stemmed,
    text_cleaning_stopword_in_stemmed,
    text_cleaning_stopword_removed_not_stemmed,
    text_cleaning_stopword_removed_stemmed
)
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow import keras

text_cleaning_dict = {
    "tokenizer_stopword_in_not_stemmed"         : text_cleaning_stopword_in_not_stemmed,
    "tokenizer_stopword_in_stemmed"             : text_cleaning_stopword_in_stemmed,
    "tokenizer_stopword_removed_not_stemmed"    : text_cleaning_stopword_removed_not_stemmed,
    "tokenizer_stopword_removed_stemmed"        : text_cleaning_stopword_removed_stemmed
}

api = Blueprint(
    "api", __name__, template_folder="templates", static_folder="static"
)

@api.route('/api/test')
def api_test():
    return jsonify('hello world')

@api.route('/api/predict', methods=['POST'])
def predict():
    data = request.json                         # get data from request

    text      = data['text']                    # get text
    stopword  = data['stopword']                # get the stopword parameter
    stemming  = data['stemming']                # get the stemming parameter
    lstm_mode = data['lstm']                    # get the lstm layer type parameter
    embedding = data['embedding']               # get the embedding type parameter

    tokenizer_name = "_".join(['tokenizer', stopword, stemming])
    tokenizer_path = f"blog/app/tokenizers/{tokenizer_name}.json"

    text_cleaning_func = text_cleaning_dict[tokenizer_name]

    model_name = "_".join(['model', stopword, stemming, lstm_mode, embedding])
    model_path = f"blog/app/models/{model_name}"

    tokenizer = load_tokenizer_from_json(tokenizer_path)
    model = keras.models.load_model(model_path)

    # predict the text
    text = text_cleaning_func(text)
    sequence = tokenizer.texts_to_sequences([text])
    sequence = pad_sequences(sequence, maxlen=30)

    score = model.predict(sequence).flatten()[0]

    response = {"score": str(score),
                "model": model_name,
                "tokenizer": tokenizer_name,
                "text_cleaning_func": tokenizer_name.replace("tokenizer", "text_cleaning") 
               }

    return jsonify(response)

