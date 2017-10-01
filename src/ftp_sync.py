from ftplib import FTP
from ftp_downloader import FtpDownloader
from ftp_crawler import FtpCrawler

class FtpSync:
    def __init__(self, host, dest_dir):
        self.host = host
        self.dest_dir = dest_dir
        # Lazy init
        self.connection = None

    def sync_path(self, path):
        if self.connection is None:
            self.connection = FTP(host=self.host)

        ftp_crawler = FtpCrawler(ftplib=self.connection, base_path=path)
        ftp_downloader = FtpDownloader(ftplib=self.connection,
                dest_path=self.dest_dir)

        ftp_downloader.download_all(path_list=ftp_crawler.get_all_entries())
