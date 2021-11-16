import datetime
import os
import numpy as np
from german_article_classifier.datapipeline.pre_processing_pipeline import run_pre_processing_pipeline
from german_article_classifier.datapipeline.extract import load_dataset_from_csv
from german_article_classifier.utils.config import get_root_path
from catboost import Pool, CatBoostClassifier
import logging

logger = logging.getLogger("classifier.training")


def run_training_pipeline(**kwargs) -> None:
    """
    This function runs the whole training pipeline for catboosted models. First it loads and preprocesses the training,
    testing data, then based on the given parameters by the kwargs the training is started based on the specified params
    in dev.yaml. After that the model is either saved or not.
    Args:
        **kwargs: Input arguments needed to configure the training pipeline flow.

    Returns (NoneType): None

    """
    logger.info("Initializing training params ...")
    try:
        training_params = {
            "iterations": kwargs.get("iterations"),
            "learning_rate": kwargs.get("lr"),
            "eval_metric": kwargs.get("eval_metric"),
            "task_type": kwargs.get("task_type"),
            "early_stopping_rounds": kwargs.get("early_stopping_rounds"),
            "use_best_model": kwargs.get("use_best_model"),
            "verbose": kwargs.get("verbose"),
        }
    except KeyError as e:
        logger.info(f"At {datetime.datetime.now()}, error {e} occurred during training")
        raise

    try:
        df_train = load_dataset_from_csv(data_path=os.path.join(kwargs.get("data_path"), kwargs.get("train_csv")))
        df_test = load_dataset_from_csv(data_path=os.path.join(kwargs.get("data_path"), kwargs.get("test_csv")))
    except FileNotFoundError as e:
        logger.info(f"At {datetime.datetime.now()}, got {e} ...")
        raise

    df_train = run_pre_processing_pipeline(df=df_train)
    df_test = run_pre_processing_pipeline(df=df_test)

    x_train = np.array(df_train["text"])
    y_train = np.array(df_train["label"])
    x_test = np.array(df_test["text"])
    y_test = np.array(df_test["label"])

    train_pool = Pool(x_train, y_train, text_features=[0])
    valid_pool = Pool(x_test, y_test, text_features=[0])

    logger.info(f"At {datetime.datetime.now()}, started training ...")

    model = CatBoostClassifier(**training_params)
    model.fit(train_pool, eval_set=valid_pool, plot=True)

    if kwargs.get("save"):
        out_file_path = os.path.join(get_root_path(), kwargs.get("model_path"))
        model.save_model(fname=out_file_path)
        logger.info(f"At {datetime.datetime.now()}, saved model to {out_file_path}")

    logger.info(f"At {datetime.datetime.now()}, finished training ...")
