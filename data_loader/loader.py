from pathlib import Path
import datetime

from logs.logger import Logger


logger = Logger.get_logger()


class DataLoader:

    def __init__(self,path):
        self.metadataFromPodcasts=None
        self.path=path
        self.file_path = Path(str(self.path))



    def set_path(self,path):
        self.path=path


    def extract_metadata(self):

        metadata=[]
        if  self.file_path.is_dir():
            logger.info(f"Extract from folder {self.file_path}")

            for item in  self.file_path.iterdir():

                stats = item.stat()


                file={
                     "path":str(item),
                     "Name":item.name,
                     "Size":stats.st_size,
                     "Creation_time" :str(datetime.datetime.fromtimestamp(stats.st_ctime)),
                     "Last_modified":str(datetime.datetime.fromtimestamp(stats.st_mtime)),


                }
                metadata.append(file)
        else:
            logger.error(f"The path '{ self.file_path}' is not a valid folder.")
        self.metadataFromPodcasts=metadata











