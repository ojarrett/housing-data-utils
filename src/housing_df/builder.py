from housing_df import csv as csv_utils

import os
import pandas as pd
import numpy as np

FILE_NAME_SURVEY_DATE_INDEX_START = 2
FILE_NAME_SURVEY_DATE_INDEX_END=-5
COLUMN_DTYPES={
    'Survey Date' : np.int32,
    'State Code' : np.int32,
    '6-Digit ID' : np.int32,
    'County Code' : np.int32,
    'CSA Code' : np.int32,
    'CBSA Code' : np.int32,
    'Zip Code' : np.int32,
    'Region Code' : np.int32,
    'Place Name' : np.str,
    '1-unit Bldgs' : np.int32,
    '1-unit Units' : np.int32,
    ' Value' : np.int32,
    '2-units Bldgs' : np.int32,
    '2-units Units' : np.int32,
    '2-units Value' : np.int32,
    '3-4 units Bldgs' : np.int32,
    '3-4 units Units' : np.int32,
    '3-4 units Value' : np.int32,
    '5+ units Bldgs' : np.int32,
    '5+ units Units' : np.int32,
    '5+ units Value' : np.int32,
}

class HousingDFBuilder:

    def __init__(self):
        self.csv = None
        self.filter_fields = None
        self.csv_prefix = None
        self.csv_suffix = None
        self.csv_dir = None
        self.before_date = None
        self.after_date = None

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

    def set_before_date(self, before_date):
        self.before_date = before_date

    def set_after_date(self, after_date):
        self.after_date = after_date

    def __file_matches(self, file_name):
        if self.csv_prefix is not None:
            if not file_name.startswith(self.csv_prefix):
                return False

        if self.csv_suffix is not None:
            if not file_name.endswith(self.csv_suffix):
                return False

        survey_date = self.__get_survey_date_from_file_name(file_name)
        if self.before_date is not None:
            if survey_date >= self.before_date:
                return False

        if self.after_date is not None:
            if survey_date <= self.after_date:
                return False

        return True

    def __get_survey_date_from_file_name(self,file_name):
        date = int(file_name[2:-5])
        if date < 8800:
            date = 200000 + date
        else:
            date = 190000 + date

        return date

    def build(self):

        file_list = [self.csv_dir + "/" + file_name for file_name in os.listdir(self.csv_dir) if self.__file_matches(file_name)] if self.csv is None else [self.csv]

        temp_df = None
        for file_name in file_list:
            new_df = pd.read_csv(
                file_name,
                header=None,
                skiprows=csv_utils.CSV_HEADER_LINES,
                names=csv_utils.get_header_lines_from_file(file_name),
                dtype=COLUMN_DTYPES,
            )

            if temp_df is not None:
                temp_df = pd.concat([temp_df, new_df], ignore_index=True)
            else:
                temp_df = new_df

        temp_df.dropna(thresh=len(temp_df) // 2, axis=1, inplace=True)

        return temp_df if self.filter_fields is None else temp_df[self.filter_fields]
