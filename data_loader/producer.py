
from utils.confin_kafka import KafkaConfigurations
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Producer:
    def __init__(self):
        self.connect_kafka=KafkaConfigurations.producer_connect()

    def send_data(self, metadata):
        self.publish_message("metadata_podcasts", metadata)


    def publish_message(self, topic, message):
        try:
            self.connect_kafka.send(topic, message)
            self.connect_kafka.flush()

            logger.info(f"Message sent to topic {topic}: {message}")
        except Exception as e:
            logger.error(f"Error publishing message to topic {topic}: {e}")




