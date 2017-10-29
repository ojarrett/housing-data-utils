from src.housing_df import HousingDFBuilder

VALID_REGIONS = ['mw', 'ne', 'so', 'we']
CURRENT_MONTH_CSV_SUFFIX = "c.txt"
DATA_DIR = "data"

class InvalidInputException(Exception):
    pass

def get_housing_df_for_region(region):
    if not region in VALID_REGIONS:
        raise InvalidInputException("Unrecognized region: " + str(region))

    housing_dfb = HousingDFBuilder()

    housing_dfb.set_csv_prefix(region)
    housing_dfb.set_csv_suffix(CURRENT_MONTH_CSV_SUFFIX)
    housing_dfb.set_csv_dir(DATA_DIR)

    df = housing_dfb.build()

    return df
