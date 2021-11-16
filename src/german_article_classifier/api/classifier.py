from fastapi import APIRouter
from german_article_classifier.mlpipeline.predictor import predict_text
from pydantic import BaseModel
from typing import List
import logging
import datetime

router = APIRouter()
classifier_route_logger = logging.getLogger("classifier.classifier")


class PredictReturnBody(BaseModel):
    text: str
    predicted_category: str


@router.get("/predict", tags=["Classifier"], response_model=PredictReturnBody)
async def predict(text: str) -> PredictReturnBody:
    """
    This GET endpoint takes a german sentence and returns a prediction (what type of article it corresponds to most
    likely).
    Args:
        text (str): German input sequence.

    Returns (PredictReturnBody): returns the text and the predicted class as a string

    """
    classifier_route_logger.info(f"At {datetime.datetime.now()} got GET request with param: {text}. to route: /predict")
    predicted_category = "".join(predict_text(text=text))
    return PredictReturnBody(text=text, predicted_category=predicted_category)


@router.post("/predict", tags=["Classifier"], response_model=List[str])
async def read_items(req: List[str]) -> List[str]:
    """
    This POST endpoint accepts a list of strings where the strings are german sentences or sequences and returns
    a prediction for each on what type of article that may be.
    Args:
        req List[str]: Request body.

    Returns List[str]: Returns a list of strings (predictions)

    """
    classifier_route_logger.info(f"At {datetime.datetime.now()} got POST request to route: /predict")
    return ["".join(predict_text(text=t)) for t in req]
