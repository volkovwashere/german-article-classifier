import pandas as pd
from german_article_classifier.utils.config import get_root_path, read_yaml
# from german_article_classifier.utils.custom_logger import CustomLogger
from german_article_classifier.datapipeline.transform import (
    remove_numbers,
    remove_punctuation,
    stop_word_removal,
    map_umlaut,
)
from typing import Union
# import datetime
CONFIG = read_yaml(root_path=get_root_path())
# data_pipeline_logger = CustomLogger.construct_logger(
#     name=__name__, log_file_path=get_root_path() + "logs/DATAPIPELINE.log", logger_level=40
# )


def run_pre_processing_pipeline(*, df: pd.DataFrame) -> Union[pd.DataFrame, None]:
    """
    This function transforms and loads the specified dataset for training. Mainly it lowers, removes punctuation,
    numbers, maps umlaut chars to english ones and removes stop words from a given sentence. This function by default
    loads in either the test or train dataset, based on the dataset_level and is_split params, where the latter is
    TRUE by default. There are 4 dataset type levels:
    0 - no splitting, raw dataset
    1 - train set
    2 - test set
    If the is_split param is FALSE, then the pipeline tries to load in the raw not split dataset and preprocesses it.

    Args:
        df (pd.DataFrame): pandas dataframe that we want to preprocess.

    Returns (pd.DataFrame or None): Returns cleaned pandas df else returns None and raises.

    """
    print("Started preprocessing ...")
    try:
        new_df = df.copy(deep=False)

        new_df["text"] = new_df["text"].str.lower()
        new_df["label"] = new_df["label"].str.lower()
        new_df = new_df.dropna()
        new_df["text"] = new_df["text"].apply(remove_punctuation)
        new_df["text"] = new_df["text"].apply(remove_numbers)
        new_df["text"] = new_df["text"].apply(map_umlaut)
        new_df["text"] = new_df["text"].apply(stop_word_removal)

        # data_pipeline_logger.log_info(f"... at {datetime.datetime.now()} finished preprocessing.")
        print("... finished preprocessing.")
        return new_df
    except Exception as e:
        # data_pipeline_logger.log_info(message=f"At {datetime.datetime.now()}, got error: {e}")
        raise


def pre_process_text(document: str) -> str:
    document = document.lower()
    document = remove_punctuation(document=document)
    document = remove_numbers(document=document)
    document = map_umlaut(document=document)
    document = stop_word_removal(document=document)
    return document
