from consumer import Consumer
# from connect_elastic import ConnectElastic
from generte_id import generate_id_from_data


class Manager:
    def __init__(self):
        self.consumer = Consumer()
        self.data = None




    def run(self):
        self.data = self.consumer.consume_data()





if __name__ == "__main__":
    m = Manager()
    m.run()

