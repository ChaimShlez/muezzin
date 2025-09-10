
from config.config_mongo import ConfigMongo
from bson.binary import Binary

from logs.logger import Logger

logger = Logger.get_logger()

class ConnectMongo:
    def __init__(self,db_name,collection_name):
        self.con=ConfigMongo.connection_mongo(db_name,collection_name)



    def insert_file(self,path,podcast_id):

        try:

            logger.info(f" insert file to mongodb {path}")
            with open(path, 'rb') as f:
                audio_data = f.read()
            self.con.insert_one({

                "podcast_id": podcast_id,
                "data": Binary(audio_data)
            })
        except Exception as e:
            logger.error(f"An error occurred: {e}")
