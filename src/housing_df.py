import pandas as pd
import src.csv_utils as csv_utils
import os

class HousingDFBuilder:

    def __init__(self):
        self.csv = None
        self.filter_fields = None
        self.csv_prefix = None
        self.csv_suffix = None
        self.csv_dir = None

    def set_csv(self, csv):
        self.csv = csv

    def set_csv_prefix(self, csv_prefix):
        self.csv_prefix = csv_prefix

    def set_csv_suffix(self, csv_suffix):
        self.csv_suffix = csv_suffix

    def set_csv_dir(self, csv_dir):
        self.csv_dir = csv_dir

    def set_filter_fields(self, filter_fields):
        self.filter_fields = filter_fields

    def __file_matches(self, file_name):
        result = True

        if self.csv_prefix is not None:
            if not file_name.startswith(self.csv_prefix):
                return False

        if self.csv_suffix is not None:
            if not file_name.endswith(self.csv_suffix):
                return False

    def build(self):

        file_list = [self.csv_dir + "/" + file_name for file_name in os.listdir(self.csv_dir) if self.__file_matches(file_name)] if self.csv is None else [self.csv]

        temp_df = pd.concat([pd.read_csv(file_name, header=None, skiprows=csv_utils.CSV_HEADER_LINES, names=csv_utils.get_header_lines_from_file(file_name)) for file_name in file_list])
        return temp_df if self.filter_fields is None else temp_df[self.filter_fields]
