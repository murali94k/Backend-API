from fastapi import FastAPI
import uvicorn
from config import config
from logger import get_logger

app = FastAPI()
logger = get_logger(__name__)


@app.get("/")
def root():
    logger.debug("Fetching Root Endpoint")
    return {"message": "Hello World"}


@app.get("/version")
def version():
    logger.debug("Fetching Version Endpoint")
    return {"App Name": config["APP_NAME"], "App Version": config["BUILD_VERSION"]}


if __name__ == "__main__":
    logger.debug("Starting App @ port 8000 .... ")
    uvicorn.run("app:app", host="localhost", port=8000)
