import pandas

INCLUDED_COLUMNS = [
        'Survey Date',
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
        '5+ units Value',
]


class HousingSeriesBuilder:
    def __init__(self, df):
        self.df = df

    def build(self, place_name=None, start_date=None, end_date=None):
        df = self.df[INCLUDED_COLUMNS]
        filter_ = None
        if place_name:
            place_filter = df['Place Name'] == place_name
            filter_ = place_filter if filter_ is None else filter_ & place_filter
        if start_date:
            start_filter = df['Survey Date'] >= start_date
            filter_ = start_filter if filter_ is None else filter_ & start_filter
        if end_date:
            end_filter = df['Survey Date'] <= end_date
            filter_ = end_filter if filter_ is None else filter_ & end_filter

        return df if filter_ is None else df[filter_]
