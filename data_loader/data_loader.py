import logging
import os
from pathlib import Path
import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataLoader:

    def __init__(self,path):
        self.metadataFromPodcasts=None
        self.path=path
        self.file_path = Path(str(self.path))
        print(self.file_path)
        # print(file_path.stat())


    def set_path(self,path):
        self.path=path




    def extract_metadata(self):

        metadata=[]
        if  self.file_path.is_dir():
            logger.info(f"Extract from folder {self.file_path}")

            for item in  self.file_path.iterdir():
                stats = item.stat()
                file={
                     "path":self.path,
                     "Name":item.name,
                     "Size":stats.st_size,
                     "Creation time" :str(datetime.datetime.fromtimestamp(stats.st_ctime)),
                     "Last modified":str(datetime.datetime.fromtimestamp(stats.st_mtime))

                }
                metadata.append(file)
                self.metadataFromPodcasts=metadata



        else:
            logger.error(f"The path '{ self.file_path}' is not a valid folder.")










