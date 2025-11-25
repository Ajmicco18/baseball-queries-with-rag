import pprint
import os
from dotenv import load_dotenv
from openai import OpenAI
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo import UpdateOne

load_dotenv()

# MongoDB
uri = os.getenv('MONGO_DB_URI')
client = MongoClient(uri, server_api=ServerApi('1'))
db = client[os.getenv('DATABASE_NAME')]
collection = db["People"]

# Specify your OpenAI API key and embedding model
API_KEY = os.getenv("OPENAI_API_KEY")
embedding_model = "text-embedding-3-small"
llm_model = "gpt-4o"
openai_client = OpenAI()


# Define a function to generate embeddings
def get_embedding(text):
    """Generates vector embeddings for the given text."""

    embedding = openai_client.embeddings.create(
        input=[text], model=embedding_model).data[0].embedding
    return embedding


def generate_embedding():

    # Define a filter to exclude documents with null or empty 'summary' fields
    filter = {'$and': [{'fullName': {'$exists': True, "$nin": [
        None, ""]}}, {'embedding': {'$exists': False}}]}

    # Get a subset of documents in the collection
    documents = collection.find(
        filter,
        {'_id': 1, 'fullName': 1}
    ).limit(1000)

    # total = collection.count_documents(filter)
    # print(total)

    # Generate the list of bulk write operations
    operations = []
    for doc in documents:
        fullName = doc["fullName"]
        # Generate embeddings for this document
        embedding = get_embedding(fullName)

        # Add the update operation to the list
        operations.append(UpdateOne(
            {"_id": doc["_id"]},
            {"$set": {
                "embedding": embedding
            }}
        ))

    # Execute the bulk write operation
    if operations:
        result = collection.bulk_write(operations)
        updated_doc_count = result.modified_count

    print(f"Updated {updated_doc_count} documents.")


def generate_search_index():
    from pymongo.operations import SearchIndexModel

    # Create your index model, then create the search index
    search_index_model = SearchIndexModel(
        definition={
            "fields": [
                {
                    "type": "vector",
                    "path": "embedding",
                    "similarity": "dotProduct",
                    "numDimensions": 1536
                }
            ]
        },
        name="vector_index",
        type="vectorSearch"
    )

    collection.create_search_index(model=search_index_model)


def get_query_results(query):
    """Gets results from a vector search query."""

    query_embedding = get_embedding(query)
    pipeline = [
        {
            "$vectorSearch": {
                "index": "vector_index",
                "queryVector": query_embedding,
                "path": "embedding",
                "exact": True,
                "limit": 5
            }
        }, {
            "$project": {
                "_id": 0,
                "fullName": 1
            }
        }
    ]

    results = collection.aggregate(pipeline)

    array_of_results = []
    for doc in results:
        array_of_results.append(doc)
    return array_of_results


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


# generating the vector embeddings
# print(generate_embedding())


# generating the search indexes
# print(generate_search_index())

# Test the function with a sample query
pprint.pprint(get_query_results("Bird"))
