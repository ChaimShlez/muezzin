import os
from data_loader.loader import DataLoader
from data_loader.producer import Producer
from logs.logger import Logger

logger = Logger.get_logger()
class Manager:
    def __init__(self):

        self.loader=DataLoader(os.getenv("PATH"))
        self.producer=Producer()
        self.metadata=None


    def run(self):
        logger.info("run manager data loader")
        self.loader.extract_metadata()
        self.metadata=self.loader.metadataFromPodcasts

        for item in self.metadata:
            logger.info(f"publish to kafka{item}")
            self.producer.send_data(item)


if __name__ == "__main__":
    m=Manager()
    m.run()





