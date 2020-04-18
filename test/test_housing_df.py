from housing_df.utils import get_housing_df_for_region
from housing_df.specific import HousingUnitCountDF, PlaceDF

import numpy as np

def test_get_housing_df_for_region():
    df = get_housing_df_for_region('we', csv_dir='test/data')
    assert len(df[df['Place Name'] == 'San Francisco']) > 0

def test_place_df():
    df = get_housing_df_for_region('we', csv_dir='test/data')
    place_df = PlaceDF(df, 'Seattle')

    assert len(place_df.df[place_df.df['Place Name'] == 'San Francisco']) == 0
    assert np.all(place_df.df['Place Name'] == 'Seattle')
