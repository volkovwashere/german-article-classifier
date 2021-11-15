from german_article_classifier.utils.config import read_yaml, get_root_path
from german_article_classifier.mlpipeline.training import run_training_pipeline

CONFIG = read_yaml(root_path=get_root_path())

run_training_pipeline(
    data_path=CONFIG["data_path"],
    train_csv=CONFIG["train_csv"],
    test_csv=CONFIG["test_csv"],
    iterations=CONFIG["model_params"]["iterations"],
    lr=CONFIG["model_params"]["lr"],
    eval_metric=CONFIG["model_params"]["eval_metric"],
    task_type=CONFIG["model_params"]["task_type"],
    early_stopping_rounds=CONFIG["model_params"]["early_stopping_rounds"],
    use_best_model=CONFIG["model_params"]["use_best_model"],
    verbose=CONFIG["model_params"]["verbose"],
    model_path=CONFIG["model_out_path"],
    save=CONFIG["save"],
)
