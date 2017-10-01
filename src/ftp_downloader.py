class FtpDownloader:
    def __init__(self, ftplib, dest_path):
        self.ftplib = ftplib
        self.dest_path = dest_path

    def download_all(self, path_list):
        for path in path_list:
            self.download(path)

    def download(self, path):
        # TODO: Handle name collisions (owen)
        name = path.split('/')[-1]
        self.ftplib.retrbinary('RETR ' + path, open(self.dest_path + "/" + name, 'wb').write)
