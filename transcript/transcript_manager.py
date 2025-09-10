import os
from transcript.connect_mongo import ConnectMongo
from transcript.connect_elastic import ConnectElastic
from transcript.transcription import Transcription
from config.confin_kafka import KafkaConfigurations
from logs.logger import Logger

logger = Logger.get_logger()
class Manager:

    def __init__(self):
        self.connect_kafka_consumer = KafkaConfigurations.consumer_connect( os.getenv("TOPIC_CONSUMER"))
        self.connect_mongo = ConnectMongo(os.getenv("MONGODB_DATABASE"), os.getenv("MONGODB_COLLECTION"))
        self.connect_elastic = ConnectElastic(os.getenv("ELASTIC_INDEX"))
        self.connect_kafka = KafkaConfigurations.producer_connect()

        # self.connect_elastic.es.indices.delete(index="podcasts")


    def run_pipeline(self):
        data = self.connect_kafka_consumer
        for record in data:
            logger.info(f"run_pipeline on record {record}")

            data=self.connect_mongo.get_by_id(record.value)
            text=Transcription.speach_to_text(data)

            self.connect_elastic.update_data(text, record.value)
            self.connect_elastic.get_all()
            text={
                "id":record.value,
                "text":text
            }
            KafkaConfigurations.publish_message(self.connect_kafka, os.getenv("TOPIC_PRODUCER"), text)






if __name__ == "__main__":
    d = Manager()
    d.run_pipeline()
