import ftplib
from ftplib import FTP
from ftp_downloader import FtpDownloader
from ftp_crawler import FtpCrawler

class FtpSync:
    DEFAULT_FTP_TIMEOUT = 5
    DEFAULT_FTP_CONNECT_RETRIES = 10
    def __init__(self, host, dest_dir, ftp_timeout=DEFAULT_FTP_TIMEOUT, ftp_connect_retries=DEFAULT_FTP_CONNECT_RETRIES):
        self.host = host
        self.dest_dir = dest_dir
        # Lazy init
        self.connection = None
        self.ftp_timeout = ftp_timeout
        self.ftp_connect_retries = ftp_connect_retries

    def __try_ftp_connect(self):
        attempt = 0
        while attempt < self.ftp_connect_retries:
            attempt = attempt + 1
            try:
                connection = FTP(host=self.host, timeout=self.ftp_timeout)
                return connection
            except ftplib.all_errors as e:
                print("Timed out connecting to %s, retrying. Exception thrown:%s", self.host, str(e))
                if attempt == self.ftp_connect_retries: raise e

    def sync_path(self, path):
        if self.connection is None:
            self.connection = self.__try_ftp_connect()

        ftp_crawler = FtpCrawler(ftplib=self.connection, base_path=path)
        ftp_downloader = FtpDownloader(ftplib=self.connection,
                dest_path=self.dest_dir)

        ftp_downloader.download_all(path_list=ftp_crawler.get_all_entries())
