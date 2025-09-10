from pprint import pprint

from config.config_elastic import ConfigElastic
from logs.logger import Logger

logger = Logger.get_logger()


class ConnectElastic:

    def __init__(self,index_name):
        self.es=ConfigElastic.connection_elastic()
        self.index_name=index_name






    def update_data(self, bds_percent,bds_threat_level,is_bds,podcast_id):

        try:
            logger.info(f" update metadata to elastic {podcast_id}")
            update_body = {
                "doc": {
                    "is_bds": is_bds,
                    "bds_percent":bds_percent,
                    "bds_threat_level":bds_threat_level
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
            pprint(hit)
        print("---------------------------------------------------------------------------------------------")





