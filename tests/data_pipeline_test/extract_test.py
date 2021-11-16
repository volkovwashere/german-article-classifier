import os.path
import pandas as pd
import pytest

from german_article_classifier.datapipeline.extract import load_dataset_from_csv


def test_load_dataset_from_csv():
    t1 = os.path.join("D:/10kgerdataset/", "train.csv")
    df = load_dataset_from_csv(data_path=t1)
    assert type(df) == pd.DataFrame

    with pytest.raises(expected_exception=FileNotFoundError):
        t2 = "wrongpathlol"
        load_dataset_from_csv(data_path=t2)
