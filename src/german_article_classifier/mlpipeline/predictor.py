from german_article_classifier.datapipeline.pre_processing_pipeline import pre_process_text
from german_article_classifier.mlpipeline.model import CatGnad


def predict_text(text: str):
    return CatGnad.predict([pre_process_text(document=text)])
