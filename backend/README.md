# Baseball Queries with RAG Backend

by Anthony Micco

## Installation

**Prerequisites**

To run this project, you will need to create accounts in or install the following:

-   [Python 3.11+](https://www.python.org/downloads/)
-   [MongoDB Account](https://www.mongodb.com/)
-   [OpenAI API Key](https://platform.openai.com/api-keys)

### Setup Virtual Environment and Install Libraries

You must also create a Python virtual environment using the following steps: 

1. Create virtual environment named venv:

    ```shell
    python venv venv
    ```

2. Active the virtual environment in your backend directory:

    ```shell
    ./venv/Scripts/activate
    ```

Additionally, you must install all the required Python libraries using the requirements.txt file
 ```shell
    pip install -r requirements.txt
 ```

Finally, to run the API, you enter the following command: 
```shell
    fastapi dev main.py
```
---

### MongoDB Database

To create the database, you must go to [MongoDB](https://www.mongodb.com/) and generate a database using the following [instructions](https://www.mongodb.com/docs/). When the database is created you can connect to it using Python by adding your MongoDB database uri to the .env.example file and using the format found in the data_cleaning.py file. The data_cleaning.py file has three functions that populate the database with data from a Kaggle baseball dataset [found here](https://www.kaggle.com/datasets/open-source-sports/baseball-databank/data). 


### Viewing the Interactive API Docs

**For Documentation**

-   http://localhost:8000/docs

**For ReDoc**

-   http://localhost:8000/redoc
