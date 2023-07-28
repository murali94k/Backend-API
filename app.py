from fastapi import FastAPI
import uvicorn
from config import config
from logger import get_logger
from fastapi.responses import HTMLResponse

app = FastAPI()
logger = get_logger(__name__)


@app.get("/", response_class=HTMLResponse)
def root():
    logger.debug("Fetching Root Endpoint")
    return """
        <html>
            <head>
                <title>Devops Demo</title>
            </head>
            <body>
                <h1>Hello World ! </h1>
                <h3>Welcome to Devops Demo </h3
                <h4>Version {} </h4>
            </body>
        </html>
        """.format(config["BUILD_VERSION"])


@app.get("/version")
def version():
    logger.debug("Fetching Version Endpoint")
    return {"message": "App Version : {}".format(config["BUILD_VERSION"])}


if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8080)
