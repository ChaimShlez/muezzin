
from utils.confin_kafka import KafkaConfigurations


from utils.logger import Logger

logger = Logger.get_logger()

class Producer:
    def __init__(self):
        self.connect_kafka=KafkaConfigurations.producer_connect()

    def send_data(self, metadata):
        self.publish_message("metadata_podcasts", metadata)


    def publish_message(self, topic, message):
        try:
            logger.info(f"Message sent to topic {topic}: {message}")
            self.connect_kafka.send(topic, message)
            self.connect_kafka.flush()


        except Exception as e:
            logger.error(f"Error publishing message to topic {topic}: {e}")




