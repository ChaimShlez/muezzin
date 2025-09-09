from processor.connect_elastic import ConnectElastic
from processor.decoding import Decoding


class Manager:
    def __init__(self):
        self.hostile=None
        self.no_hostile=None
        self.connect_elastic = ConnectElastic("podcasts")





    def run_processor(self):
        self.hostile=Decoding.code_decoding("R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT")
        self.no_hostile=Decoding.code_decoding(" RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ==")
        print(self.no_hostile)
        print(self.hostile)
        self.connect_elastic.q_weapon(self.no_hostile)



if __name__ == "__main__":
    m=Manager()
    m.run_processor()
