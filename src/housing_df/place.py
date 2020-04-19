from housing_df.specific import MetroDF

import pandas as pd
import numpy as np

class Place:
    def __init__(self, df, place_name):
        self.df = df
        self.place_name = place_name

    def get_cbsa_code(self):
        temp = self.df[self.df['Place Name'] == self.place_name]['CBSA Code'].values
        return temp[np.logical_not(np.isnan(temp))][0]

    def get_places_in_same_metro(self):
        cbsa_code = self.get_cbsa_code()
        return np.unique(self.df[self.df['CBSA Code'] == cbsa_code]['Place Name'].values)

    def get_metro_df(self):
        return MetroDF(self.df, self.get_cbsa_code())
