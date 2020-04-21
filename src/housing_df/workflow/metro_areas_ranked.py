from housing_df.utils import build_housing_df_registry_for_all_regions, save_all_dfs_in_registry
from housing_df.specific import RegionDF, MetroDF
from housing_df.workflow.report import Report

import pandas as pd
import numpy as np

class MetroAreasRanked(Report):
    def __init__(self, housing_type):
        self.reg = build_housing_df_registry_for_all_regions(from_yearly_data=True)

    def show_top_apartments(self):
        temp_df = None
        for (df, label) in self.reg.df_list:
            region_df = RegionDF(df, label)
            top_10_for_region = region_df.most_apartments(count=10)

            if temp_df is None:
                temp_df = top_10_for_region
            else: 
                temp_df = temp_df.append(top_10_for_region)

        top_10 = temp_df.sort_values(ascending=False).iloc[0:10]
        for (i, metro) in enumerate(top_10.index):
            metro_name = MetroDF(self.reg.get_df_for_cbsa(metro), metro).top_apartment_city()
            print("{0}:{1} built {2} apartments".format(str(i), metro_name, str(top_10[metro])))

    def save_data_set(self):
        save_all_dfs_in_registry()

if __name__ == "__main__":
    my_report = MetroAreasRanked('5+ units Units')
    my_report.show_top_apartments()
    my_report.save_data_set()
