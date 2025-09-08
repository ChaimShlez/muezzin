import pymongo
from pymongo import MongoClient
import os
import logging

logging.basicConfig( level=logging.INFO)
logger = logging.getLogger(__name__)

class ConfigMongo:

    @staticmethod
    def connection_mongo(db_name, collection_name):
        mongo_user = os.getenv("MONGODB_USER", "admin")
        mongo_password = os.getenv("MONGODB_PASSWORD", "secretpassword")
        mongo_db = os.getenv("MONGODB_DATABASE", db_name)
        client = pymongo.MongoClient(
            f"mongodb://{mongo_user}:{mongo_password}@localhost:27017/"
        )


        # db_name_env = os.getenv("MONGODB_DATABASE", mongo_db)
        collection_name_env = os.getenv("MONGO_COLLECTION", collection_name)

        logger.info(f"Connecting to MongoDB at {os.getenv('MONGODB_HOST', 'localhost')}:{os.getenv('MONGODB_PORT', '27017')}")
        logger.info(f"Using database: {mongo_db}, collection: {collection_name_env}")

        db = client[mongo_db]
        collection = db[collection_name_env]

        logger.info("MongoDB connection established successfully!")
        return collection






