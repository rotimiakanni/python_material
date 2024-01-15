from pymongo import mongo_client
from utils import logger
from config import settings


client = mongo_client.MongoClient(settings.MONGO_DB_CONNECTION_URI)
logger.info("Connected to MongoDB successfully")

# Get or create collection
accounts_collection = client["bankapp"]["accounts"]
users_collection = client["bankapp"]["users"]
