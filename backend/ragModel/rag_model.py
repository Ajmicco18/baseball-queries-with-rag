from dataCleaning.vector_embedding_gen import get_query_results
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openAiKey = os.getenv("OPEN_API_KEY")

llm_model = "gpt-4o"
openai_client = OpenAI()


def generate_model(query):

    # Specify search query, retrieve relevant documents, and convert to string
    # query = "What awards did Jake Arrietta win?"
    context_docs = get_query_results(query)
    context_string = " ".join([doc["fullName"] for doc in context_docs])

    # Construct prompt for the LLM using the retrieved documents as the context
    prompt = f"""Use the following pieces of context to answer the question at the end.
        {context_string}
        Question: {query}
    """

    completion = openai_client.chat.completions.create(
        model=llm_model,
        messages=[{"role": "user",
                   "content": prompt
                   }]
    )
    return completion.choices[0].message.content


if __name__ == '__main__':
    print("Hello World")
