import io
import soundfile as sf

from utils.config_mongo import ConfigMongo
from utils.logger import Logger
from io import BytesIO

logger = Logger.get_logger()

class ConnectMongo:
    def __init__(self,db_name,collection_name):
        self.con=ConfigMongo.connection_mongo(db_name,collection_name)



    def get_by_id(self,podcast_id):

        try:
            logger.info(f"get binary string by  {podcast_id}")

            date= self.con.find_one({"podcast_id":podcast_id},{"_id":0})
            date_binary=date['data']
            data_file=io.BytesIO(date_binary)

            return data_file

        except Exception as e:
            logger.error(f"An error occurred: {e}")
