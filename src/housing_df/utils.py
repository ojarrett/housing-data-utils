from housing_df.builder import HousingDFBuilder
from housing_df.place import Place
from housing_df.registry import HousingDFRegistry
from housing_df.specific import MetroDF

import os
import pandas as pd

VALID_REGIONS = ['mw', 'ne', 'so', 'we']
CURRENT_MONTH_CSV_SUFFIX = "c.txt"
DATA_DIR = "data"

class InvalidInputException(Exception):
    pass

def get_housing_df_for_region(region, csv_dir=DATA_DIR):
    if not region in VALID_REGIONS:
        raise InvalidInputException("Unrecognized region: " + str(region))

    housing_dfb = HousingDFBuilder()

    housing_dfb.set_csv_prefix(region)
    housing_dfb.set_csv_suffix(CURRENT_MONTH_CSV_SUFFIX)
    housing_dfb.set_csv_dir(csv_dir)
    housing_dfb.set_before_date(210001)
    housing_dfb.set_after_date(199912)

    df = housing_dfb.build()

    return df

def build_housing_df_registry_for_all_regions():
    registry = HousingDFRegistry()
    for region in VALID_REGIONS:
        saved_df_path = "{0}/{1}_saved.pkl".format(DATA_DIR,region)
        if os.path.exists(saved_df_path):
            df = pd.read_pickle(saved_df_path)
        else:
            df = get_housing_df_for_region(region)
        registry.add(df, region)

    return registry

def save_all_dfs_in_registry(DATA_DIR):
    instance = HousingDFRegistry.get_instance()
    if instance is None:
        return

    instance.save_all()

def get_metro_df_for_place(place_name, reg=None):
    if reg is None:
        reg = HousingDFRegistry.get_instance()
    place = Place(reg.get_df_for_place(place_name), place_name)
    return place.get_metro_df()
