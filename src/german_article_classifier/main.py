from fastapi import FastAPI, Request
from german_article_classifier.api import classifier
import uvicorn


async def catch_server_error_middleware(req: Request, call_next):
    try:
        return await call_next(req)
    except Exception:
        print("log")
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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
