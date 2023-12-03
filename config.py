import os

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
CHARACTER_SPLITTER_CHUNK_SIZE = 1000
OPENAI_EMBEDDINGS_CHUNK_SIZE = 16
MONGODB_CONNECTION_STRING = os.environ['MONGODB_CONNECTION_STRING']
WEB_BASE_URL = "https://sportivefy.com"
