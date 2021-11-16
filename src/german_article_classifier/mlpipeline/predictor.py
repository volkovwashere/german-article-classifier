from german_article_classifier.datapipeline.pre_processing_pipeline import pre_process_text
from german_article_classifier.mlpipeline.model import CatGnad
import numpy as np


def predict_text(*, text: str) -> np.ndarray:
    """
    This function predicts a string with the loaded pre-trained classifier and returns a numpy array.
    Args:
        text (str): String to predict.

    Returns (np.ndarray): Predicted numpy array (containing a string).

    """
    return CatGnad.predict([pre_process_text(document=text)])
