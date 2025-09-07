import os
import time
import logging
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ConfigElastic:

    @staticmethod
    def connection_elastic():
        es_host = os.getenv("ELASTICSEARCH_HOSTS", "http://localhost:9200")
        logger.info(f"Connecting to Elasticsearch at {es_host}")

        es = Elasticsearch(es_host)

        for attempt in range(1, 11):
            try:
                es.info()
                logger.info("Connected to Elasticsearch successfully!")
                return es
            except ConnectionError:
                time.sleep(3)

        raise Exception("Elasticsearch connection failed")



r = ConfigElastic.connection_elastic()
