import os

class FtpDownloader:
    def __init__(self, ftplib, dest_path):
        self.ftplib = ftplib
        self.dest_path = dest_path

    def __file_exists(self, name):
        return  os.path.exists(self.dest_path + "/" + name)

    def download_all(self, path_list, limit=10000):
        new_file_count = 0
        for path in path_list:
            if new_file_count >= limit:
                return
            self.download(path)
            new_file_count = new_file_count + 1

    def download(self, path, download_if_exists=False):
        # TODO: Handle name collisions (owen)
        name = path.split('/')[-1]

        if download_if_exists or not self.__file_exists(name):
            self.ftplib.retrbinary('RETR ' + path, open(self.dest_path + "/" + name, 'wb').write)
