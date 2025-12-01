from ragModel.rag_model import generate_model
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from fastapi import FastAPI

# defining FastAPI application
app = FastAPI()

# setting our frontend origin
origins = ["http://localhost:5173"]

# setting permissions to allow for cross-origin communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatQuery(BaseModel):
    query: str

# endpoint to read in the API's root


@app.get("/")
def read_root():
    return {"Hello": "World"}


# endpoint to receive the response from the RAG model


@app.post("/chat")
async def generate_respone(req: ChatQuery):
    response = generate_model(req.query)
    return {"Response": response}
