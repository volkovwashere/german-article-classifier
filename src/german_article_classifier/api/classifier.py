from fastapi import APIRouter
from german_article_classifier.mlpipeline.predictor import predict_text
from pydantic import BaseModel
from typing import List

router = APIRouter()


class PredictReturnBody(BaseModel):
    text: str
    predicted_category: str


@router.get("/predict", tags=["Classifier"], response_model=PredictReturnBody)
async def predict(text: str):
    predicted_category = "".join(predict_text(text=text))
    return PredictReturnBody(text=text, predicted_category=predicted_category)


@router.post("/predict", tags=["Classifier"], response_model=List[str])
async def read_items(req: List[str]):
    return ["".join(predict_text(t)) for t in req]
