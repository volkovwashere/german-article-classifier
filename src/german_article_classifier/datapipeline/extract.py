import logging
import datetime
import pandas as pd
from typing import Union

extract_logger = logging.getLogger("classifier.extract")


def load_dataset_from_csv(data_path: str) -> Union[pd.DataFrame, None]:
    """
    This function loads a CSV as a pandas dataframe and returns it if the file exists else it raises and logs an error.
    Args:
        data_path (str): Absolute path of the given csv.

    Returns: Pandas dataframe OR None

    """
    try:
        return pd.read_csv(filepath_or_buffer=data_path)
    except FileNotFoundError as e:
        extract_logger.info(f"At {datetime.datetime.now()} got error: {e} during dataset loading.")
        raise
