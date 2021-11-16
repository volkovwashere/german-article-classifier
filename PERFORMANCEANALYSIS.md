# Model comparison

<!-- Introduction -->
## Introduction
For the classifier training two model was used. The first one used was catboost (CatGnad) which is based on gradient boosted decision trees. The other model was a very basic Bi-LSTM with two classifier layer at the end. The training parameters for the CatGnad model can be found under properties/dev.yaml config file and for the NN model used parameters for the training will be provided in this .md file.

<!-- Tech stack -->
## Tech stack
__CatGnad__
- https://catboost.ai/
- scikit-learn
__Bi-Gnad__
- PyTorch 1.10 with CUDA 11.3

<!-- Training method -->
## Training method
### CatGnad
CatGnad was trained on a GPU for over 500 epochs with early stopping used. The model fitted pre-processed text data with provided labels. The data was introduced in the DATANALYIS.md and README.md.
</br > K-fold cross validation was also performed to see if it should be used or not, but different data sets did not provide much different results so for the comparisons sake I did not use it.
### Bi-Gnad
The Bi lstm model was trained and implemented with the PyTorch framework using CUDA enabled GPU. The training parameters were the following:
- embedding dimension: 64
- hidden dimension 128
- 2 layers for Bi LSTM
- output dimension: 10
- vocab_size: 186366
- objective function: CrossEntropyLoss
- optimizer: AdamW
- num epochs: 32
- Early stopping: True, patiance: 4
- learning rate: 1e-2

</br > Model pseudo architecture:
```
x = embedding_layer(x)
lstm_output, (hidden_state, cell_state) = bi_lstm(x)
x = dense_layer(x)
x = gelu(x)
x = dropout(p=0.3, x)
x = dense_output_layer(x)
```

### Pre-processing the data
For CatGnad standard text preprocessing was applied, and no numerical features were calculated (catboost does this job for us). The same text preprocessing steps were applied as discussed in the Dataanalyis.md.
</br > For the Bi-Gnad model two additional steps were applied to the standard pipeline. Tokenization and replacing strings with corresponding numerical indexes. After the pre-processing I created a custom Pytorch dataloader were the sequences were padded to the max length in the given batch (dynamic padding), thus reducing memory footprint and increasing training efficiency.



<!-- Results and comparison -->
## Results and comparison
### Recall, Precision, F1-score, Accuracy comparison per category
![bi-gnad classification](https://user-images.githubusercontent.com/57996039/142039366-4589eb36-87a3-42b4-b630-a3973053c90e.png)
![catgnad clfreport](https://user-images.githubusercontent.com/57996039/142039466-46243f32-d458-4a69-9c61-335db5e89fe1.png)

### Confusion matrix comparison

![bi gnad confusion](https://user-images.githubusercontent.com/57996039/142039534-d29ae566-8af7-4d4c-9706-adabf0559966.png)
![catgnad confusion](https://user-images.githubusercontent.com/57996039/142039586-e6f92b04-ad8e-46d1-a5a3-f3de2fec6cc1.png)


### Additional plots and training curves can be seen under /notebooks/training_pytorch.ipynb and notebooks/training_catboost.ipynb

<!-- Summary -->
## Summary
Overall CatGnad outperformed Bi-Gnad, both in inference performance and computationnally, therefore for the rest api the best performing CatGnad model was used.


