import logging

from elasticsearch import helpers

from utils.config_elastic import ConfigElastic

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ConnectElastic:

    def __init__(self,index_name):
        self.es=ConfigElastic.connection_elastic()
        self.index_name=index_name
        self.create_index()




    def create_index(self):
        # self.con_elastic.es.indices.delete(index=index_name)
        mappings = {
                "properties": {
                    "PodcastID": {
                        "type": "keyword"
                    },
                    "Name":{
                        "type":"keyword"

                    },
                    "CreationTime": {
                        "type": "keyword"
                    },
                    "LastModified": {
                        "type": "keyword"
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

    def insert_data(self, data,podcast_id):
        try:
            logger.info(f" insert metadata to elastic {data}")

            response = self.es.index(index=self.index_name, body=data, id=podcast_id)
            self.es.indices.refresh(index=self.index_name)
            print("res",response)
        except Exception as e:
            logger.error(f"Insertion failed: {e}")






