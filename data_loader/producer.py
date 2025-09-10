import os

from config.confin_kafka import KafkaConfigurations


from logs.logger import Logger

logger = Logger.get_logger()

class Producer:
    def __init__(self):
        self.connect_kafka=KafkaConfigurations.producer_connect()

    def send_data(self, metadata):
        try:
            logger.info(f"Message sent to topic ")
            KafkaConfigurations.publish_message(self.connect_kafka, os.getenv("TOPIC_PRODUCER"), metadata)

        except Exception as e:
            logger.error(f"Error publishing message to topic : {e}")







