import os
from dotenv import load_dotenv
from openai import OpenAI
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

# MongoDB
uri = os.getenv('MONGO_DB_URI')
client = MongoClient(uri, server_api=ServerApi('1'))
db = client[os.getenv('DATABASE_NAME')]

# Specify your OpenAI API key and embedding model
API_KEY = os.getenv("OPENAI_API_KEY")
model = "text-embedding-3-small"
openai_client = OpenAI()


# Define a function to generate embeddings
def get_embedding(text):
    """Generates vector embeddings for the given text."""

    embedding = openai_client.embeddings.create(
        input=[text], model=model).data[0].embedding
    return embedding


# Generate an embedding
# embedding = get_embedding("foo")
# print(embedding)

def concatName():

    # defining the collection
    collection = db["People"]

    # creating aggregation pipeline to update the fullName field
    collection.update_many(
        {},
        [
            {'$set': {"fullName": {"$concat": [
                "$nameFirst", " ", "$nameLast"]}}}
        ]
    )


print(concatName())
