from sync.ftp_sync import FtpSync
import sys
import os

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python housing_data_sync.py <ftp-server> <base-path>")
        sys.exit(1)

    ftp_sync = FtpSync(host=sys.argv[1], dest_dir=(os.curdir + "/data"))
    ftp_sync.sync_path(path=sys.argv[2])
