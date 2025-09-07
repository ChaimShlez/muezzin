from utils.confin_kafka import KafkaConfigurations


class Consumer:
    def __init__(self):
        self.connect_kafka=KafkaConfigurations.consumer_connect(
            "metadata_podcasts")




    def consume_data(self):
        data=self.connect_kafka

        return data



