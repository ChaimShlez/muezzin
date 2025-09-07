# from elasticsearch import helpers
#
# from utils.config_elastic import ConfigElastic
#
# class ConnectElastic:
#
#     def __init__(self,name_index):
#         self.es=ConfigElastic.connection_elastic()
#         self.name_index=name_index
#         self.create_index()
#
#
#
#
#     def create_index(self):
#         # self.con_elastic.es.indices.delete(index=index_name)
#         mappings = {
#                 "properties": {
#                     "PodcastID": {
#                         "type": "keyword"
#                     },
#                     "Name":{
#                         "type":"keyword"
#
#                     },
#                     "CreationTime": {
#                         "type": "keyword"
#                     },
#                     "LastModified": {
#                         "type": "keyword"
#                     },
#
#                 }
#         }
#
#         try:
#
#             res=self.es.indices.create(index=self.name_index, mappings=mappings)
#             print(res)
#         except Exception as e:
#             print(f"error{e}")
#
#     def insert_data(self, data):
#         print(data)
#         actions = [
#             {
#                 "_index": self.name_index,
#                 "_source": doc
#             } for doc in data
#         ]
#
#         response = helpers.bulk(self.es, actions)
#         print(response)
#
