import os
import utils.secret_files
from config.confin_kafka import KafkaConfigurations
from processing.analyzer import Analyzer
from processing.connect_elastic import ConnectElastic
from processing.decoding import Decoding
from logs.logger import Logger


logger = Logger.get_logger()


class Processing_manager:

    def __init__(self):
        self.connect_kafka_consumer = KafkaConfigurations.consumer_connect(os.getenv("TOPIC_CONSUMER"))
        self.connect_elastic = ConnectElastic(os.getenv("ELASTIC_INDEX"))


        self.analyzer=Analyzer()



    def run_processing(self):
        hostile = Decoding.code_decoding(utils.secret_files.hostile)
        print(hostile)
        self.analyzer.set_hostile(hostile)
        no_hostile = Decoding.code_decoding(utils.secret_files.no_hostile)
        self.analyzer.set_no_hostile(no_hostile)
        data = self.connect_kafka_consumer
        for record in data:
            logger.info(f"run_pipeline on record {record}")

            self.analyzer.set_text(record.value['text'])
            analyzer=self.analyzer.manager_analyzer()
            # print(analyzer)
            self.connect_elastic.update_data(analyzer[0],analyzer[1],analyzer[2],record.value['id'])
            self.connect_elastic.get_all()



if __name__ == "__main__":
    d = Processing_manager()
    d.run_processing()
