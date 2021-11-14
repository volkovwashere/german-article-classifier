from german_article_classifier.datapipeline.pre_processing_pipeline import run_pre_processing_pipeline

df_test = run_pre_processing_pipeline(dataset_level=2)
print(df_test.head(5))