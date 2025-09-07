import logging
import os
from pathlib import Path
import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataLoader:

    def __init__(self):
        self.podcasts=None
        self.file_path = Path("C:\podcasts")
        # print(file_path.stat())


    def extract_metadata(self):

        metadata=[]
        if  self.file_path.is_dir():
            logger.info(f"Extract from folder {self.file_path}")

            for item in  self.file_path.iterdir():
                stats = item.stat()
                file={
                     "Name":item.name,
                     "Size":stats.st_size,
                     "Creation time" :str(datetime.datetime.fromtimestamp(stats.st_ctime)),
                     "Last modified":str(datetime.datetime.fromtimestamp(stats.st_mtime))

                }
                metadata.append(file)
                self.podcasts=metadata


        else:
            logger.error(f"The path '{ self.file_path}' is not a valid directory.")











if __name__ == "__main__":
    d=DataLoader()
    d.extract_metadata()
    # d.fetcher_from()

