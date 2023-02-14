from fastapi import FastAPI
import uvicorn
from config import config
from logger import get_logger
from fastapi.responses import HTMLResponse

app = FastAPI()
logger = get_logger(__name__)


@app.get("/")
def root():
    logger.debug("Fetching Root Endpoint")
    return {"message": "Hello World"}


@app.get("/version")
def version():
    logger.debug("Fetching Version Endpoint")
    return {"message": "App Version : {}".format(config["BUILD_VERSION"])}

