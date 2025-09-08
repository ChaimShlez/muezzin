
from utils.config_elastic import ConfigElastic
from utils.logger import Logger

logger = Logger.get_logger()


class ConnectElastic:

    def __init__(self,index_name):
        self.es=ConfigElastic.connection_elastic()
        self.index_name=index_name
        self.create_index()




    def create_index(self):

        mappings = {
                "properties": {
                    "PodcastID": {
                        "type": "keyword"
                    },
                    "Name":{
                        "type":"keyword"

                    },
                    "Text": {
                        "type": "text"

                    },
                    "CreationTime": {
                        "type": "date"
                    },
                    "LastModified": {
                        "type": "date"
                    },

                }
        }

        try:
            logger.info(f" Create index in elastic {self.index_name}")

            if not self.es.indices.exists(index=self.index_name):
                res=self.es.indices.create(index=self.index_name, mappings=mappings)
                print(res)
        except Exception as e:
            logger.error(f"Creation failed: {e}")

    def insert_data(self, data,podcast_id,text):
        try:
            logger.info(f" insert metadata to elastic {data}")
            document = {
                'metadata': data,
                'podcast_text': text

            }

            response = self.es.index(index=self.index_name, body=document, id=podcast_id)
            self.es.indices.refresh(index=self.index_name)
            print("res",response)
        except Exception as e:
            logger.error(f"Insertion failed: {e}")






