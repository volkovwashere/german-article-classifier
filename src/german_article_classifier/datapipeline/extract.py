from german_article_classifier.utils.config import get_root_path
from german_article_classifier.utils.custom_logger import CustomLogger
import pandas as pd
from typing import Union
import datetime

load_logger = CustomLogger.construct_logger(
    name="CONFIG", log_file_path=get_root_path() + "logs/LOAD.log", logger_level=40
)


def load_dataset_from_csv(data_path: str) -> Union[pd.DataFrame, None]:
    """
    This function loads a CSV as a pandas dataframe and returns it if the file exists else, it raises and logs an error.
    Args:
        data_path (str): Absolute path of the given csv.

    Returns: Pandas dataframe OR None

    """
    try:
        return pd.read_csv(filepath_or_buffer=data_path)
    except FileNotFoundError as e:
        load_logger.log_info(message=f"At {datetime.datetime.now()}, file at location: {data_path} was not found. Error: {e}")
        raise
