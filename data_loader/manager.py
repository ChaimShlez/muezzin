from data_loader import DataLoader
from producer import Producer


class Manager:
    def __init__(self):
        self.loadr=DataLoader("C:\podcasts")
        self.producer=Producer()
        self.metadata=None


    def run(self):
        # self.loadr.set_path("C:\podcasts")
        self.loadr.extract_metadata()
        self.metadata=self.loadr.metadataFromPodcasts


        for item in self.metadata:
            self.producer.send_data(item)


if __name__ == "__main__":
    m=Manager()
    m.run()
    # d.fetcher_from()




