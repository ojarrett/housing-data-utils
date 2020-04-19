from housing_df.builder import HousingDFBuilder
from housing_df.registry import HousingDFRegistry

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
        registry.add(get_housing_df_for_region(region))

    return registry
