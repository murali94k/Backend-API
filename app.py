from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()


@app.get("/health")
def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)
    uvicorn.run("app:app", host="localhost", port=port)
