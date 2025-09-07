import json
import os
import logging
from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import KafkaError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class KafkaConfigurations:

    @staticmethod
    def producer_connect():
        try:
            producer = KafkaProducer(
                bootstrap_servers=os.getenv("KAFKA_BROKER", "localhost:9092"),
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
            logger.info("Kafka producer connected successfully")
            return producer
        except KafkaError as e:
            logger.error(f"Error connecting to Kafka producer: {e}")
            return None

    @staticmethod
    def consumer_connect(group_id, *topics):
        try:
            consumer = KafkaConsumer(
                *topics,
                bootstrap_servers=os.getenv("KAFKA_BROKER", "localhost:9092"),
                auto_offset_reset='earliest',
                group_id=group_id,
                enable_auto_commit=True,
                value_deserializer=lambda v: json.loads(v.decode('utf-8'))
            )
            logger.info(f"Kafka consumer connected to topics: {topics}")
            return consumer
        except KafkaError as e:
            logger.error(f"Error connecting to Kafka consumer: {e}")
            return None

    @staticmethod
    def publish_message(producer, topic, message):
        try:
            producer.send(topic, message)
            producer.flush()
            logger.info(f"Message sent to topic {topic}: {message}")
        except KafkaError as e:
            logger.error(f"Error publishing message to topic {topic}: {e}")
