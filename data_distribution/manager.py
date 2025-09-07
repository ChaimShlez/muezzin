from consumer import Consumer
# from connect_elastic import ConnectElastic
from generte_id import generate_id_from_data


class Manager:
    def __init__(self):
        self.consumer = Consumer()
        # self.connect_elastic = ConnectElastic("podcasts")
        self.data = None
        self.data_podcast_with_id = None

    def distribution_from_db_and_generate_id(self):
        data_podcast = []
        for item in self.data:

            podcast_id = generate_id_from_data(item.value)

            podcast = {
                "Podcast_id": podcast_id,
                "Path": item.value['path'],
                "Name": item.value['Name'],
                "Size": item.value['Size'],
                "Creation time": item.value['Creation time'],
                "Last modified": item.value['Last modified']
            }

            data_podcast.append(podcast)



        return data_podcast

    def run(self):
        self.data = self.consumer.consume_data()
        data_podcast_with_id = self.distribution_from_db_and_generate_id()
        print(data_podcast_with_id)
        # self.connect_elastic.insert_data(self.data_podcast_with_id)


        # for item in self.data_podcast_with_id:
        #     print(item)


if __name__ == "__main__":
    m = Manager()
    m.run()

