import sys
import os
from pathlib import Path

import pytest

BLOG_PATH = Path(__file__).parents[4]
sys.path.append(str(BLOG_PATH))

from app import create_app

def test_api():
    response = create_app().test_client().get('/api/test')
    assert response.status_code == 200
    assert b'hello world' in response.data

def test_model_1():
    response = create_app().test_client().post('/api/predict', json={
        "text"     : "Sayap Kanan Pesawat Lion Air Tabrak Atap Bandara di Merauke",
        "stopword" : "stopword_in",
        "stemming" : "not_stemmed",
        "lstm"     : "bidirectional",
        "embedding": "keras_embedding"
    })

    assert response.status_code == 200
    assert response.json["model"] == "model_stopword_in_not_stemmed_bidirectional_keras_embedding"

def test_model_2():
    response = create_app().test_client().post('/api/predict', json={
        "text"     : "Sayap Kanan Pesawat Lion Air Tabrak Atap Bandara di Merauke",
        "stopword" : "stopword_in",
        "stemming" : "not_stemmed",
        "lstm"     : "bidirectional",
        "embedding": "word2vec"
    })

    assert response.status_code == 200
    assert response.json["model"] == "model_stopword_in_not_stemmed_bidirectional_word2vec"

def test_model_3():
    response = create_app().test_client().post('/api/predict', json={
        "text"     : "Sayap Kanan Pesawat Lion Air Tabrak Atap Bandara di Merauke",
        "stopword" : "stopword_in",
        "stemming" : "not_stemmed",
        "lstm"     : "non_bidirectional",
        "embedding": "keras_embedding"
    })

    assert response.status_code == 200
    assert response.json["model"] == "model_stopword_in_not_stemmed_non_bidirectional_keras_embedding"

def test_model_4():
    response = create_app().test_client().post('/api/predict', json={
        "text"     : "Sayap Kanan Pesawat Lion Air Tabrak Atap Bandara di Merauke",
        "stopword" : "stopword_in",
        "stemming" : "not_stemmed",
        "lstm"     : "non_bidirectional",
        "embedding": "word2vec"
    })

    assert response.status_code == 200
    assert response.json["model"] == "model_stopword_in_not_stemmed_non_bidirectional_word2vec"

def test_model_5():
    response = create_app().test_client().post('/api/predict', json={
        "text"     : "Sayap Kanan Pesawat Lion Air Tabrak Atap Bandara di Merauke",
        "stopword" : "stopword_in",
        "stemming" : "stemmed",
        "lstm"     : "bidirectional",
        "embedding": "keras_embedding"
    })

    assert response.status_code == 200
    assert response.json["model"] == "model_stopword_in_stemmed_bidirectional_keras_embedding"

def test_model_6():
    response = create_app().test_client().post('/api/predict', json={
        "text"     : "Sayap Kanan Pesawat Lion Air Tabrak Atap Bandara di Merauke",
        "stopword" : "stopword_in",
        "stemming" : "stemmed",
        "lstm"     : "bidirectional",
        "embedding": "word2vec"
    })

    assert response.status_code == 200
    assert response.json["model"] == "model_stopword_in_stemmed_bidirectional_word2vec"

def test_model_7():
    response = create_app().test_client().post('/api/predict', json={
        "text"     : "Sayap Kanan Pesawat Lion Air Tabrak Atap Bandara di Merauke",
        "stopword" : "stopword_in",
        "stemming" : "stemmed",
        "lstm"     : "non_bidirectional",
        "embedding": "keras_embedding"
    })

    assert response.status_code == 200
    assert response.json["model"] == "model_stopword_in_stemmed_non_bidirectional_keras_embedding"

def test_model_8():
    response = create_app().test_client().post('/api/predict', json={
        "text"     : "Sayap Kanan Pesawat Lion Air Tabrak Atap Bandara di Merauke",
        "stopword" : "stopword_in",
        "stemming" : "stemmed",
        "lstm"     : "non_bidirectional",
        "embedding": "word2vec"
    })

    assert response.status_code == 200
    assert response.json["model"] == "model_stopword_in_stemmed_non_bidirectional_word2vec"

def test_model_9():
    response = create_app().test_client().post('/api/predict', json={
        "text"     : "Sayap Kanan Pesawat Lion Air Tabrak Atap Bandara di Merauke",
        "stopword" : "stopword_removed",
        "stemming" : "not_stemmed",
        "lstm"     : "bidirectional",
        "embedding": "keras_embedding"
    })

    assert response.status_code == 200
    assert response.json["model"] == "model_stopword_removed_not_stemmed_bidirectional_keras_embedding"

def test_model_10():
    response = create_app().test_client().post('/api/predict', json={
        "text"     : "Sayap Kanan Pesawat Lion Air Tabrak Atap Bandara di Merauke",
        "stopword" : "stopword_removed",
        "stemming" : "not_stemmed",
        "lstm"     : "bidirectional",
        "embedding": "word2vec"
    })

    assert response.status_code == 200
    assert response.json["model"] == "model_stopword_removed_not_stemmed_bidirectional_word2vec"

def test_model_11():
    response = create_app().test_client().post('/api/predict', json={
        "text"     : "Sayap Kanan Pesawat Lion Air Tabrak Atap Bandara di Merauke",
        "stopword" : "stopword_removed",
        "stemming" : "not_stemmed",
        "lstm"     : "non_bidirectional",
        "embedding": "keras_embedding"
    })

    assert response.status_code == 200
    assert response.json["model"] == "model_stopword_removed_not_stemmed_non_bidirectional_keras_embedding"

def test_model_12():
    response = create_app().test_client().post('/api/predict', json={
        "text"     : "Sayap Kanan Pesawat Lion Air Tabrak Atap Bandara di Merauke",
        "stopword" : "stopword_removed",
        "stemming" : "not_stemmed",
        "lstm"     : "non_bidirectional",
        "embedding": "word2vec"
    })

    assert response.status_code == 200
    assert response.json["model"] == "model_stopword_removed_not_stemmed_non_bidirectional_word2vec"

def test_model_13():
    response = create_app().test_client().post('/api/predict', json={
        "text"     : "Sayap Kanan Pesawat Lion Air Tabrak Atap Bandara di Merauke",
        "stopword" : "stopword_removed",
        "stemming" : "stemmed",
        "lstm"     : "bidirectional",
        "embedding": "keras_embedding"
    })

    assert response.status_code == 200
    assert response.json["model"] == "model_stopword_removed_stemmed_bidirectional_keras_embedding"

def test_model_14():
    response = create_app().test_client().post('/api/predict', json={
        "text"     : "Sayap Kanan Pesawat Lion Air Tabrak Atap Bandara di Merauke",
        "stopword" : "stopword_removed",
        "stemming" : "stemmed",
        "lstm"     : "bidirectional",
        "embedding": "word2vec"
    })

    assert response.status_code == 200
    assert response.json["model"] == "model_stopword_removed_stemmed_bidirectional_word2vec"

def test_model_15():
    response = create_app().test_client().post('/api/predict', json={
        "text"     : "Sayap Kanan Pesawat Lion Air Tabrak Atap Bandara di Merauke",
        "stopword" : "stopword_removed",
        "stemming" : "stemmed",
        "lstm"     : "non_bidirectional",
        "embedding": "keras_embedding"
    })

    assert response.status_code == 200
    assert response.json["model"] == "model_stopword_removed_stemmed_non_bidirectional_keras_embedding"

def test_model_16():
    response = create_app().test_client().post('/api/predict', json={
        "text"     : "Sayap Kanan Pesawat Lion Air Tabrak Atap Bandara di Merauke",
        "stopword" : "stopword_removed",
        "stemming" : "stemmed",
        "lstm"     : "non_bidirectional",
        "embedding": "word2vec"
    })

    assert response.status_code == 200
    assert response.json["model"] == "model_stopword_removed_stemmed_non_bidirectional_word2vec"

