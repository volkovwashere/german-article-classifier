from fastapi import FastAPI, Request
from german_article_classifier.api import classifier
from german_article_classifier.utils.custom_logger import CustomLogger
from german_article_classifier.utils.config import get_root_path
import uvicorn
import os
import datetime


async def catch_server_error_middleware(req: Request, call_next):
    try:
        return await call_next(req)
    except Exception as e:
        logger.info(f"At {datetime.datetime.now()}, exception {e} occurred.")
        pass


app = FastAPI(
    title="German Article Classifier",
    description="Categorizing german articles.",
    version="0.1.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(router=classifier.router, prefix="/classifier")
app.middleware("http")(catch_server_error_middleware)


@app.get("/", tags=["Root"])
async def get_root():
    return {"status_code": 200}


logger = CustomLogger.construct_logger(
    name="classifier", log_file_path=os.path.join(get_root_path(), "logs/app.log"), logger_level=20,
)
logger.log_info(f"At {datetime.datetime.now()} started running server at host: 127.0.0.0, port: 8000")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
