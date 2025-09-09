from connect_mongo import ConnectMongo
from connect_elastic import ConnectElastic
from transcription import Transcription
from utils.confin_kafka import KafkaConfigurations
from utils.logger import Logger

logger = Logger.get_logger()
class Manager:

    def __init__(self):
        self.connect_kafka = KafkaConfigurations.consumer_connect( "podcasts_id")
        self.connect_mongo = ConnectMongo("muezzin", "podcasts")
        self.connect_elastic = ConnectElastic("podcasts")
        # self.connect_elastic.es.indices.delete(index="podcasts")


    def run_pipeline(self):
        data = self.connect_kafka
        for record in data:
            logger.info(f"run_pipeline on record {record}")

            data=self.connect_mongo.get_by_id(record.value)
            text=Transcription.speach_to_text(data)

            self.connect_elastic.update_data(text, record.value)
            self.connect_elastic.get_all()




if __name__ == "__main__":
    d = Manager()
    d.run_pipeline()
