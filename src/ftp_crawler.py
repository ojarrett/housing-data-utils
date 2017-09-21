class FtpCrawler:
    def __init__(self, base_path, ftplib):
        self.base_path = base_path
        self.ftplib = ftplib

    def get_all_entries(self):
        return dict()
