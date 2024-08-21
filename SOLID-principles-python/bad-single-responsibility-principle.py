from pathlib import Path
from zipfile import ZipFile

# reads/writes files and compresses/decompresses file to zip archive
class Filemanager:
    def __init__(self, filename):
        self.path = Path(filename)
    
    # read text from file
    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)
    
    # write data into a file
    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

    # compress file to zip archive
    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    # extract zip archive
    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()

# no SRP because: does reading/writing files AND compressing/decompressing files to zip
# so it has more than one repsonsibility and should be split into two classes