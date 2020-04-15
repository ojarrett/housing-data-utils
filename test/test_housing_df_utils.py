from housing_df_utils import get_housing_df_for_region

def test_get_housing_df_for_region():
    df = get_housing_df_for_region('we')
    assert len(df[df['Place Name'] == 'San Francisco']) > 0
