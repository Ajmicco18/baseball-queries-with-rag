import os
from langchain_community.utilities import SQLDatabase
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
import mysql.connector


def sql_llm_retrieval(question):

    # Define OpenAI API Key
    api_key = ""

    # Loading our database in
    mysql_uri = ''

    db = SQLDatabase.from_uri(mysql_uri)

    def get_schema(_):
        return db.get_table_info()

    get_schema(None)

    # Creating prompt to convert user question to SQL query
    template = """Based on the table schema below, write a SQL query that would answer the user's question:
    {schema}

    Question: {question}
    SQL Query:
    """
    prompt = ChatPromptTemplate.from_template(template)

    prompt.format(schema="my schema",
                  question=question)

    # Creating LLM chain for our query
    llm = ChatOpenAI()

    sql_chain = (
        RunnablePassthrough.assign(schema=get_schema)
        | prompt
        | llm.bind(stop="\nSQL Result:")
        | StrOutputParser()
    )

    # Creating a template for our full LLM chain
    template = """
    Based on the table schema below, question, sql query, and sql response, write a natural language response: 
    {schema}

    Question: {question}
    SQL Query: {query}
    SQL Response: {response}"""

    prompt = ChatPromptTemplate.from_template(template)

    def run_query(query):
        return db.run(query)

    # Creating full LLM chain for our question and query
    full_chain = (
        RunnablePassthrough.assign(query=sql_chain).assign(
            schema=get_schema,
            response=lambda variables: run_query(variables["query"])
        )
        | prompt
        | llm
        | StrOutputParser()
    )

    print(full_chain.invoke({"question": question}))


if __name__ == '__main__':
    """sql_llm_retrieval(
     "What software feature map items are in the CAM category?")"""
    mydb = mysql.connector.connect(
        host="18.221.113.0",
        user="brayant",
        password="Drive^YT_24"
    )

    print(mydb)
