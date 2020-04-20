import numpy as np
import pandas as pd

class HousingDFRegistry:
    def __init__(self):
        self.place_to_df = {}
        self.cbsa_to_df = {}

    def add(self, df):
        for place in np.unique(df['Place Name'].values):
            self.place_to_df[place] = df

    def get_df_for_place(self, place):
        if place in self.place_to_df:
            return self.place_to_df[place]

        return None

    def get_df_for_cbsa(self, cbsa):
        if cbsa in self.cbsa_to_df:
            return self.cbsa_to_df[cbsa]

        return None
