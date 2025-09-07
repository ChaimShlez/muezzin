from pymongo import MongoClient
import os
import logging

logging.basicConfig( level=logging.INFO)
logger = logging.getLogger(__name__)

class ConfigMongo:

    @staticmethod
    def connection_mongo(db_name, collection_name):
        client = MongoClient(
            host=os.getenv("MONGODB_HOST", "localhost"),
            port=int(os.getenv("MONGODB_PORT", "27017")),
            username=os.getenv("MONGODB_USER"),
            password=os.getenv("MONGODB_PASSWORD"),
            authSource="admin"
        )

        db_name_env = os.getenv("MONGODB_DATABASE", db_name)
        collection_name_env = os.getenv("MONGO_COLLECTION", collection_name)

        logger.info(f"Connecting to MongoDB at {os.getenv('MONGODB_HOST', 'localhost')}:{os.getenv('MONGODB_PORT', '27017')}")
        logger.info(f"Using database: {db_name_env}, collection: {collection_name_env}")

        db = client[db_name_env]
        collection = db[collection_name_env]

        logger.info("MongoDB connection established successfully!")
        return collection
