from housing_df.utils import get_housing_df_for_region
from housing_df.specific import HousingUnitCountDF, PlaceDF
from housing_df.csv import get_header_lines_from_file

import numpy as np

def test_get_housing_df_for_region():
    df = get_housing_df_for_region('we', csv_dir='test/data')
    assert len(df[df['Place Name'] == 'San Francisco']) > 0

def test_get_housing_df_for_region_yearly():
    df = get_housing_df_for_region('we', csv_dir='test/data', from_yearly_data=True)
    assert len(df[df['Place Name'] == 'San Francisco']) > 0

def test_place_df():
    df = get_housing_df_for_region('we', csv_dir='test/data')
    place_df = PlaceDF(df, 'Seattle')

    assert len(place_df.df[place_df.df['Place Name'] == 'San Francisco']) == 0
    assert np.all(place_df.df['Place Name'] == 'Seattle')

def test_get_header_lines_from_file():
    expected_header_lines = [
         'Survey Date',
         'State Code',
         '6-Digit ID',
         'County Code',
         'Census Place Code',
         'FIPS Place Code',
         'FIPS MCD Code',
         'Pop ',
         'CSA Code',
         'CBSA Code',
         'Footnote Code',
         'Central City',
         'Zip Code',
         'Region Code',
         'Division Code',
         'Source Code',
         'Place Name',
         '1-unit Bldgs',
         '1-unit Units',
         '1-unit Value',
         '2-units Bldgs',
         '2-units Units',
         '2-units Value',
         '3-4 units Bldgs',
         '3-4 units Units',
         '3-4 units Value',
         '5+ units Bldgs',
         '5+ units Units',
         '5+ units Value'
    ]

    actual_header_lines = get_header_lines_from_file('test/data/we1510c.txt')
    assert expected_header_lines == actual_header_lines

    expected_header_lines = expected_header_lines + [
         '1-unit rep Bldgs',
         '1-unit rep Units',
         '1-unit rep Value',
         '2-units rep Bldgs',
         '2-units rep Units',
         '2-units rep Value',
         '3-4 units rep Bldgs',
         '3-4 units rep Units',
         '3-4 units rep Value',
         '5+ units rep Bldgs',
         '5+ units rep Units',
         '5+ units rep Value'
    ]

    actual_header_lines = get_header_lines_from_file('test/data/we1512y.txt')
