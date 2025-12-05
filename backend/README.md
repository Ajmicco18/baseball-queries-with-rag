# Baseball Queries with RAG Backend

by Anthony Micco

## Installation

**Prerequisites**

To run this project, you will need to create accounts or install the following:

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

### Connecting to MongoDB Database

To connect to the MongoDB database, clone the repository and change the directory

```sh
git clone https://github.com/Ajmicco18/baseball-queries-with-rag.git
cd backend
```

1. Copy `.env.example` to `.env`:

    ```shell
    cp .env.example .env
    ```

2. Retrieve OpenAI API Key:

   Go to [https://platform.openai.com/api-keys] (https://platform.openai.com/api-keys) to create an account and generate a key.

3. Copy OpenAI API Key to .env:

With these steps complete, you can connect to the database as well as utilize the OpenAI API to run the large language model. 


### Viewing the Interactive API Docs

**For Documentation**

-   http://localhost:8000/docs

**For ReDoc**

-   http://localhost:8000/redoc
