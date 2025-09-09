from pprint import pprint

from utils.config_elastic import ConfigElastic
from utils.logger import Logger

logger = Logger.get_logger()


class ConnectElastic:

    def __init__(self,index_name):
        self.es=ConfigElastic.connection_elastic()
        self.index_name=index_name





    def update_index(self):

        mappings = {
                "properties": {
                    "PodcastID": {
                        "type": "keyword"
                    },
                    "Name":{
                        "type":"keyword"

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

    def update_data(self, text,podcast_id):
        try:
            logger.info(f" update metadata to elastic {text}")
            update_body = {
                "doc": {
                    "text": text
                }
            }
            response = self.es.update(index=self.index_name, id=podcast_id, body=update_body)
            print("res", response)
            self.es.indices.refresh(index=self.index_name)



        except Exception as e:
            logger.error(f"Insertion failed: {e}")

    def get_all(self):
        query = {
            "query": {
                "match_all": {}
            },
            "size": 10000

        }
        results = self.es.search(index=self.index_name, body=query)
        for hit in results['hits']['hits']:
            pprint(hit['_source'])
        print("---------------------------------------------------------------------------------------------")





