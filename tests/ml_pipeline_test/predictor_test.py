from german_article_classifier.mlpipeline.predictor import predict_text
import numpy as np


def test_predict_text_check_type():
    t1 = str(["s", 448488])
    t2 = "correctstr"
    t3 = str(9445544)
    t4 = str(5.47788)

    res1 = predict_text(text=t1)
    res2 = predict_text(text=t2)
    res3 = predict_text(text=t3)
    res4 = predict_text(text=t4)

    assert res1
    assert res2
    assert res3
    assert res4
    assert type(res1) == np.ndarray
