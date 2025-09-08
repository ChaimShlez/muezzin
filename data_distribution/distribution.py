from datetime import datetime

from data_distribution.connect_mongo import ConnectMongo
from data_distribution.transcription import Transcription

from utils.confin_kafka import KafkaConfigurations
from generte_id import generate_id_from_data
from connect_elastic import ConnectElastic
from utils.logger import Logger

logger = Logger.get_logger()
class Distribution:
    def __init__(self):
        self.connect_kafka=KafkaConfigurations.consumer_connect(
            "metadata_podcasts")
        self.connect_elastic = ConnectElastic("podcasts")
        # self.connect_elastic.es.indices.delete(index="podcasts")
        self.connect_mongo=ConnectMongo("muezzin","podcasts")


    def convert_data(self,data_str):

        format_string = "%Y-%m-%d  %H:%M:%S"
        convert_creation_time = datetime.strptime(data_str, format_string)
        return convert_creation_time




    def consume_data(self):
        data=self.connect_kafka
        for record in data:
            logger.info(f"distribution on record {record}")
            podcast_id = generate_id_from_data(record.value)
            convert_creation_time=self.convert_data(record.value['Creation_time'])

            record.value['Creation_time'] = convert_creation_time

            text=Transcription.speach_to_text(record.value['path'])
            self.connect_elastic.insert_data(record.value,podcast_id,text)
            self.connect_mongo.insert_file(record.value['path'],podcast_id)





if __name__ == "__main__":
    d = Distribution()
    d.consume_data()

