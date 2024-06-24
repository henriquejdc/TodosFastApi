import os
import pymongo

from dotenv import load_dotenv

from tests.conftest import MockCollection

load_dotenv()

# Get credentials from environment variables
MONGO_USERNAME = os.getenv('MONGO_USERNAME')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
MONGO_CLUSTER = os.getenv('MONGO_CLUSTER')
APP_NAME = os.getenv('APP_NAME')
DATABASE = os.getenv('DATABASE')
ENV_MODE = os.getenv('ENV_MODE', 'prod')
collection_name = MockCollection()

if ENV_MODE != 'test':
    # Construct the MongoDB URL
    MONGO_URL = (
        f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER}/"
        f"?retryWrites=true&w=majority&appName={APP_NAME}"
    )

    client = pymongo.MongoClient(MONGO_URL)

    DB = client[DATABASE]

    collection_name = DB['todo_collection']
