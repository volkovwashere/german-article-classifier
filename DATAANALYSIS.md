# Data analyis

<!-- Introduction -->
## Introduction
The initial dataset can be found here: 
</br > https://tblock.github.io/10kGNAD/
</br > I set it up based on the following github directory and some additional changes
</br > https://github.com/tblock/10kGNAD

</br > The dataset was splitted with a ratio of 8:2 to train and test sets as a csv. A csv was choosed out of convinience because the dataset was not huge and did not take much space, but overall using .parquet is recommended. The same train / test set was used during the two model's training. Out of curiosity I also checked training with k-fold cross-validation (which is also recommended), but did not see much difference between the model performances so for this project I used the originally split data. The data was split with sklearn train_test_split with random_state=200.
</br > The text data was pre-processed before data analyis and the following steps were applied:
- text lowercasing
- punctuation removel
- number removal
- umlaut mapping
- german stop word removel
</br > Lemmatization or stemming was not applied due to the lack of good quality german lemmatizers or stemming libraries.
<!-- Data analysis -->
## Data Analyis
For data analyis I used pandas, numpy, seaborn and matplotlib.
### Number of samples
![number of samples](https://user-images.githubusercontent.com/57996039/142027994-57151e45-ab66-438f-b511-4ce263405954.png)
### Category distribution

![train category distribution](https://user-images.githubusercontent.com/57996039/142028085-0f8fe699-dfee-43f1-b1a9-dba0b1e946b5.png)
![test category distribution](https://user-images.githubusercontent.com/57996039/142028092-e37ff38d-9e89-4a72-b663-243d53367d8c.png)

### Sequence lengths

![sequence length train](https://user-images.githubusercontent.com/57996039/142028195-766e063a-3d2f-4391-b0e3-881bf6763f4d.png)
![sequence length test](https://user-images.githubusercontent.com/57996039/142028201-5c97c596-b6d4-4ec0-8d7e-bb5336a90d41.png)
### Average length of seqences
![average length train](https://user-images.githubusercontent.com/57996039/142028301-0701c4d4-05e4-4011-9e35-c898df4fa222.png)
![avg length test](https://user-images.githubusercontent.com/57996039/142028329-14c947b0-c00d-4c47-9e88-fdd683eebf72.png)

### Most frequent words after pre-processing

![top 10 train](https://user-images.githubusercontent.com/57996039/142028824-6ae00d12-c620-47e0-89cb-59fc4687eb45.png)
![top 10 test](https://user-images.githubusercontent.com/57996039/142028856-dd2b18e3-77f4-4037-aa29-6f329b14572b.png)


### Top 10 bi-grams
![bigram train](https://user-images.githubusercontent.com/57996039/142028632-e957257f-d1c1-406d-9178-72e727cdf82e.png)


![bigram test](https://user-images.githubusercontent.com/57996039/142028609-ef33b95e-e02d-4951-9930-d5dc7227b795.png)

### Top 10 tri-grams
![tri gram train](https://user-images.githubusercontent.com/57996039/142028675-879c9ffc-b73e-46dc-a780-25127a9b42ae.png)
![tri gram test](https://user-images.githubusercontent.com/57996039/142028688-3fb99683-cf84-4e35-bda2-57c1570920ca.png)

<!-- Summary -->
## Summary
</br > The overall number of samples is around 10k with 8k for training and 2k for testing. The dataset has class imbalance as well as it can be seen on the diagrams. 
</br > From the third  and fourth plots it can be denoted that the sequence lengths are around 100 - 500 and the average length is around 8 - 9.
</br > In the rest of the diagrams and plots the bi-gram, tri-gram and word frequencies are displayed. For the bi-grams the words millionen - euro, new york (train) and for the test the most frequent co-occuring elements are are millionen euro and seit - jahren. For the tri-gram pairs the most occuring words together are: islamister staat ist, red-bull-salz. 
