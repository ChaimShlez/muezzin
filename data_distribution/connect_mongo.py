import logging
import os
from utils.config_mongo import ConfigMongo
from bson.binary import Binary

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ConnectMongo:
    def __init__(self,db_name,collection_name):
        self.con=ConfigMongo.connection_mongo(db_name,collection_name)



    def insert_file(self,path,podcast_id):

        try:

            logger.info(f" insert file to mongodb {path}")
            with open(path, 'rb') as f:
                audio_file = f.read()
                print("cswfvegfdasfvgdfdsqswf",audio_file)

            self.con.insert_one({

                "podcast_id": podcast_id,
                "data": Binary(audio_file)
            })
        except Exception as e:
            logger.error(f"An error occurred: {e}")
