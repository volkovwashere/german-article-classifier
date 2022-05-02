from fastapi.testclient import TestClient
from _pytest.monkeypatch import MonkeyPatch
from german_article_classifier.mlpipeline import predictor
import numpy as np
from german_article_classifier.main import app
import json

monkey_patch = MonkeyPatch()
client = TestClient(app)


def test_get_predict():
    def mock_predict_text(text: str):
        return np.array([str(text)])

    monkey_patch.setattr(predictor, "predict_text", mock_predict_text)
    assert res.status_code == 200
    assert type(res.json()) == dict


def test_post_get_predict():
    def mock_predict_text(text: str):
        return np.array([str(text)])

    monkey_patch.setattr(predictor, "predict_text", mock_predict_text)
    res = client.post("/classifier/predict", data=json.dumps(["asd", "asd"]))
    assert res.status_code == 200
    assert type(res.json()) == list
