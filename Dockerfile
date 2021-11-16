FROM python:3.8-slim

WORKDIR /german-classifier/

COPY src /german-classifier/src/
COPY logs /german-classifier/logs/
COPY properties /german-classifier/properties/
COPY requirements.txt /german-classifier/requirements.txt
RUN pip install -r /german-classifier/requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/german-classifier/src"


CMD uvicorn --host=0.0.0.0 --port=8000 german_article_classifier.main:app
