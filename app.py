from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()


@app.get("/health")
def root():
    return {"message": "Hello World"}


if __name__ == "__main__":

    uvicorn.run("app:app", host="0.0.0.0", port=8000)
