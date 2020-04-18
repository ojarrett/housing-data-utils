import pandas as pd

class SpecificDF:
    def __init__(self, df):
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
