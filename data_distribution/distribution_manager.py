import os

from data_distribution.connect_mongo import ConnectMongo

from config.confin_kafka import KafkaConfigurations
from data_distribution.generte_id import generate_id_from_data
from data_distribution.connect_elastic import ConnectElastic
from logs.logger import Logger

logger = Logger.get_logger()





class Distribution:
    def __init__(self):
        self.connect_kafka_consumer=KafkaConfigurations.consumer_connect(os.getenv("TOPIC_CONSUMER"))

        self.connect_elastic = ConnectElastic(os.getenv("ELASTIC_INDEX"))
        # self.connect_elastic.es.indices.delete(index="podcasts")
        self.connect_mongo=ConnectMongo(os.getenv("MONGODB_DATABASE"),os.getenv("MONGODB_COLLECTION"))
        self.connect_kafka = KafkaConfigurations.producer_connect()




    def split_data(self,data):
        data={
            "Name": data['Name'],
            "Size":data['Size'],
            "Creation_time":data['Creation_time'],
            "Last_modified": data['Last_modified']
        }

        return data

    def distribution_data(self):
        data=self.connect_kafka_consumer
        print(data)
        for record in data:
            print(record)
            logger.info(f"distribution on record {record}")
            podcast_id = generate_id_from_data(record.value)


            KafkaConfigurations.publish_message(self.connect_kafka,os.getenv("TOPIC_PRODUCER"),podcast_id)

            data=self.split_data(record.value)
            self.connect_elastic.insert_data(data,podcast_id)
            self.connect_mongo.insert_file(record.value['path'],podcast_id)





if __name__ == "__main__":
    d = Distribution()
    d.distribution_data()

