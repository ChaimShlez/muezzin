import os
import time

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError

from logs.logger import Logger

logger = Logger.get_logger()


class ConfigElastic:

    @staticmethod
    def connection_elastic():
        es_host = os.getenv("ELASTICSEARCH_HOSTS", "http://elasticsearch:9200")
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



