import pandas as pd
import src.csv_utils as csv_utils

class HousingDFBuilder:

    def __init__(self):
        self.csv = None
        self.filter_fields = None

    def set_csv(self, csv):
        self.csv = csv

    def set_filter_fields(self, filter_fields):
        self.filter_fields = filter_fields

    def build(self):
        header = None
        with open(self.csv, "r") as input_file:
            header_lines = [input_file.readline().strip().split(csv_utils.CSV_DELIMITER) for line in csv_utils.CSV_HEADER_LINES]

            header = csv_utils.merge_header_lines(header_lines)

        if header is None:
            print("Failed to extract header lines. Exiting...")
            exit(1)

        print(pd.read_csv(self.csv, header=None, skiprows=csv_utils.CSV_HEADER_LINES, names=header))
