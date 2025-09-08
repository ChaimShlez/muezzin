from data_distribution.connect_mongo import ConnectMongo
from utils.confin_kafka import KafkaConfigurations
from generte_id import generate_id_from_data
from connect_elastic import ConnectElastic
from utils.logger import Logger

logger = Logger.get_logger()
class Consumer:
    def __init__(self):
        self.connect_kafka=KafkaConfigurations.consumer_connect(
            "metadata_podcasts")
        self.connect_elastic = ConnectElastic("podcasts")
        self.connect_mongo=ConnectMongo("muezzin","podcasts")





    def consume_data(self):
        data=self.connect_kafka
        for record in data:
            logger.info(f"distribution on record {record}")
            podcast_id = generate_id_from_data(record.value)

            self.connect_elastic.insert_data(record.value,podcast_id)
            self.connect_mongo.insert_file(record.value['path'],podcast_id)





