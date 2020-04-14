from ftp_crawler import FtpCrawler
import unittest

class FakeFtpLib:
    file_structure = {
        "Dir1": {
            "children": {
                "Subdir1": [
                    "Entry1",
                    "Entry2",
                ]
            },
            "dirent" : "drwxrwsr-x    2 1815     3502        36864 Aug 24 07:48 Dir1"
        },
        "Dir2": {
            "Subdir1": [
                "Entry1",
            ],
            "Subdir2": [
                "Entry1",
            ]
        }
    }

    def __init__(self, host):
        self.working_dir = self.file_structure

    def login(self):
        pass

    def cwd(self, path):
        self.working_dir = self.file_structure[path]

    def dir(self, cmd):
        return [entry for entry in self.working_dir]

class FtpCrawlerTest(unittest.TestCase):
    def setUp(self):
        self.ftp_lib = FakeFtpLib("fake_host")

    def test_init(self):
        ftp = FtpCrawler("/base/path", self.ftp_lib)
        self.assertIsNotNone(ftp)

    def test_get_all_entries(self):
        ftp = FtpCrawler("/Dir1", self.ftp_lib)
        expected_result = {
            "Subdir1": [
                "Entry1",
                "Entry2",
            ]
        }

        actual_result = ftp.get_all_entries()
        self.assertDictEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()
