from housing_df.utils import get_housing_df_for_region
from housing_df.specific import HousingUnitCountDF, PlaceDF
from housing_df.csv import get_header_lines_from_file
from housing_df.place_info import PlaceInfo
from housing_df.registry import HousingDFRegistry
from housing_df.series_builder import HousingSeriesBuilder

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

def test_place_info():
    df = get_housing_df_for_region('we', csv_dir='test/data')
    registry = HousingDFRegistry()
    registry.add(df, 'we')

    place_info = PlaceInfo(registry, sample_date=201510)
    place_info.build()

    assert len(place_info.df[place_info.df['Place Name'] == 'San Francisco']) == 1

def test_place_info_lookup_index():
    df = get_housing_df_for_region('we', csv_dir='test/data')
    registry = HousingDFRegistry()
    registry.add(df, 'we')

    place_info = PlaceInfo(registry, sample_date=201510)
    place_info.build()

    ind = place_info.df.index[0]
    assert len(place_info.df.loc[ind]['Place Name']) > 0

def test_series_basic():
    df = get_housing_df_for_region('we', csv_dir='test/data')
    
    series_builder = HousingSeriesBuilder(df)
    series = series_builder.build()

    assert len(series.index) == len(df.index)

def test_series_one_filter():
    df = get_housing_df_for_region('we', csv_dir='test/data')
    
    series_builder = HousingSeriesBuilder(df)
    series = series_builder.build(start_date=201511)

    assert len(series.index) < len(df.index)

def test_series_two_filters():
    df = get_housing_df_for_region('we', csv_dir='test/data')
    
    series_builder = HousingSeriesBuilder(df)
    series = series_builder.build(start_date=201511, end_date=201511)

    assert len(series.index) < len(df.index)

def test_get_header_lines_from_file():
    expected_header_lines = [
         'Survey Date',
         'State Code',
         '6-Digit ID',
         'County Code',
         'Census Place Code',
         'FIPS Place Code',
         'FIPS MCD Code',
         'Pop',
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
