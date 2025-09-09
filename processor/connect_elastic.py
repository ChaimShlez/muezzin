
from utils.config_elastic import ConfigElastic
from utils.logger import Logger

logger = Logger.get_logger()


class ConnectElastic:

    def __init__(self,index_name):
        self.es=ConfigElastic.connection_elastic()
        self.index_name=index_name





    def q_weapon(self,hostile):
        query = {
            "query": {
                "bool": {
                    "should": [
                        {"match": {"text.keyword": w}
                         } for w in hostile
                    ],
                    "minimum_should_match": 0
                }
            },
            "highlight": {
                "fields": {
                    "text": {}
                }
            }
        }
        res=self.es.search(index=self.index_name,body=query)
        for hit in res['hits']['hits']:
            print("Document ID:", hit['_id'])
            print("Text:", hit['_source']['text'])
            print("Highlighted matches:", hit.get('highlight', {}).get('text', []))
    def insert_data(self, data,podcast_id):
        try:
            logger.info(f" insert metadata to elastic {data},{podcast_id}")

            response = self.es.index(index=self.index_name, body=data, id=podcast_id)
            self.es.indices.refresh(index=self.index_name)
            print("res",response)
        except Exception as e:
            logger.error(f"Insertion failed: {e}")






