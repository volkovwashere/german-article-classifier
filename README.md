# German Article Classifier
<!-- ABOUT THE PROJECT -->
## About The Project
There are many great text classifiers for english text, however for other languages there is less. For that reason, I created a gemrnal article classifier REST API based on the dataset: https://tblock.github.io/10kGNAD/. For the backend model two models was used, XGBoosted trees (with catboost) and a simple Bi-LSTM neural network with pytorch. The data analysis can be found in the DATAANALYSIS.md and the model comparison and training results can be found in the PERFORMANCEANALYSIS.md files. 

## Built with
The application was built with:
- Python
- Catboost
- FastAPI
- Docker

<!-- Getting started -->
## Getting started
### Prequisites
For the prequisites you need python 3.9 (3.7 at least) installed on your machine with anaconda preferred as environment management. Other than that you will need CUDA 11.3 as well. if you want to run the PyTorch or CatBoost training otherwise CUDA is not needed!
<br />https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html
<br />https://www.anaconda.com/products/individual

### Installation guide
#### From scratch only using the api
~~~
git clone https://github.com/volkovwashere/german-article-classifier.git
~~~
~~~
export PYTHONPATH=$PYTHONPATH:/home/<your_username>/german-article-classifier/src
~~~
~~~
cd german-article-classifier
~~~
~~~
pip install -r requirements.txt
~~~
~~~
uvicorn --reload --port=8000 src.german-article-classifier.main:app
~~~
__OPTIONAL if you want to build a docker image locally__
~~~
docker build -t your_docker_image_name .
~~~
~~~
docker run -p 8000:8000 --name docker_container_name your_docker_image_name
~~~
#### If you want to use the notebooks and training pipeline as well
~~~
conda env create -f environment.yml
~~~
Run these to install all the packages used in for the project, you might need nvidia cuda for pytorch to run.
#### Only docker
If you want to use the docker image only with the REST API, please go to the following repository and pull the fastapi image.
__URL__: https://hub.docker.com/repository/docker/krisztianvolkov/fastapi-classifier
~~~
docker pull krisztianvolkov/fastapi-classifier
~~~
~~~
docker run -p 8000:8000 krisztianvolkov/fastapi-classifier
~~~
Then go to: http://127.0.0.1:8000/docs and try it out!
<!-- Usage -->
## Usage
The usage is straight forward once the server is running. For interactive testing you can go to the /docs route and check out the available api endpoints and their documentations!
![image](https://user-images.githubusercontent.com/57996039/142024398-f96f1ded-9d71-4722-9a09-a05adc4148a7.png)
