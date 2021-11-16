from german_article_classifier.datapipeline.pre_processing_pipeline import pre_process_text, run_pre_processing_pipeline
import pandas as pd


def test_pre_processing_pipeline():
    t1 = "ëß 15s 5 A.:@ das"
    d = {"text": [t1], "label": ["LABEL"]}
    test_df = pd.DataFrame(data=d)

    test_df = run_pre_processing_pipeline(df=test_df)
    assert test_df["text"][0] == "eb s a"
    assert test_df["label"][0] == "label"


def test_preprocess_text():
    t1 = "ëß 15s 5 A.:@ das"
    assert pre_process_text(document=t1) == "eb s a"
