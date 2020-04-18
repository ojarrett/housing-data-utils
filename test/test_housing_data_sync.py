from sync.ftp_sync import FtpSync
import pytest
import os

def test_sync_from_census_server():
    SYNC_DEST_DIR = os.curdir + "/test/ftp_sync_test_new_data"
    CENSUS_HOST = "ftp2.census.gov"
    SYNC_PATH = "/econ/bps/Place/"

    census_sync = FtpSync(CENSUS_HOST, SYNC_DEST_DIR,new_file_limit=10)
    census_sync.sync_path(SYNC_PATH)

    assert len(os.listdir(SYNC_DEST_DIR)) == 10
