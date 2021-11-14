from german_article_classifier.utils.config import read_yaml, get_root_path
from german_article_classifier.utils.custom_logger import CustomLogger
import pandas as pd


CONFIG = read_yaml(root_path=get_root_path())
load_logger = CustomLogger.construct_logger(
    name="CONFIG", log_file_path=get_root_path() + "logs/LOAD.log", logger_level=40
)


def load_dataset():
    try:
        return pd.read_csv(filepath_or_buffer=CONFIG[""])
    except FileNotFoundError as e:
        print("File was not found at specific location.")
        raise
    except KeyError as e:

        raise
