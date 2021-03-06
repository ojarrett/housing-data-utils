import pandas as pd

class SpecificDF:
    def __init__(self, df, start=201001, end=201912):
        new_df = df

        if self.filter_rows:
            # TODO: Figure out how to do this without a for loop
            for key in self.filter_rows:
                value = self.filter_rows[key]
                new_df = new_df[new_df[key] == value]

        if self.filter_fields:
            self.df = new_df[self.filter_fields]
        else:
            self.df = new_df

class PlaceDF(SpecificDF):
    def __init__(self, df, place_name):
        self.filter_rows = {'Place Name': place_name}
        self.filter_fields = None
        super().__init__(df)

    def get_unit_time_series(self, housing_type='5+ units Units', start=201001, end=201912):
        df = self.df
        return df[df['Survey Date'] <= end][df['Survey Date'] >= start][['Survey Date', housing_type]].sort_values(by="Survey Date")

class HousingUnitCountDF(SpecificDF):
    def __init__(self, df):
        self.filter_rows = None
        self.filter_fields = [
                'Survey Date',
                'Place Name',
                '1-unit Units',
                '2-units Units',
                '3-4 units Units',
                '5+ units Units',
        ]

        super().__init__(df)

class MetroDF(SpecificDF):
    def __init__(self, df, cbsa_code):
        self.filter_rows = {'CBSA Code': cbsa_code}
        self.filter_fields = None
        self.groupby_place = None
        super().__init__(df)

    def __group_by_place(self):
        if self.groupby_place is None:
            self.groupby_place = self.df.groupby('Place Name')

    def most_apartments(self, count=10):
        self.__group_by_place()
        return self.groupby_place['5+ units Units'].sum().sort_values(ascending=False).iloc[0:count]

    def most_duplexes(self, count=10):
        self.__group_by_place()
        return self.groupby_place['2-units Units'].sum().sort_values(ascending=False).iloc[0:count]

    def most_tri_quad_plexes(self, count=10):
        self.__group_by_place()
        return self.groupby_place['3-4 units Units'].sum().sort_values(ascending=False).iloc[0:count]

    def most_houses(self, count=10):
        self.__group_by_place()
        return self.groupby_place['1-unit Units'].sum().sort_values(ascending=False).iloc[0:count]

    def top_apartment_city(self):
        return self.most_apartments(count=1).index[0]

class RegionDF(SpecificDF):
    def __init__(self, df, region):
        self.filter_rows = None
        self.filter_fields = None
        self.groupby_cbsa = None
        super().__init__(df)

    def __group_by_cbsa(self):
        if self.groupby_cbsa is None:
            self.groupby_cbsa = self.df.groupby('CBSA Code')

    def most_apartments(self, count=10):
        self.__group_by_cbsa()
        return self.groupby_cbsa['5+ units Units'].sum().sort_values(ascending=False).iloc[0:count]

    def most_duplexes(self, count=10):
        self.__group_by_cbsa()
        return self.groupby_cbsa['2-units Units'].sum().sort_values(ascending=False).iloc[0:count]

    def most_tri_quad_plexes(self, count=10):
        self.__group_by_cbsa()
        return self.groupby_cbsa['3-4 units Units'].sum().sort_values(ascending=False).iloc[0:count]

    def most_houses(self, count=10):
        self.__group_by_cbsa()
        return self.groupby_cbsa['1-unit Units'].sum().sort_values(ascending=False).iloc[0:count]
