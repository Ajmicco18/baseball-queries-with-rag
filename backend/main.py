from typing import Union
from ragModel.rag_model import generate_model

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/chat")
def generate_respone(query: str):
    response = generate_model(query)
    return {"Response": response}
