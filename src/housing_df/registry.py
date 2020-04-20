import numpy as np
import pandas as pd

class HousingDFRegistry:
    instance = None
    def __init__(self):
        self.place_to_df = {}
        self.cbsa_to_df = {}
        self.df_list = []
        if HousingDFRegistry.instance is None:
            HousingDFRegistry.instance = self

    def get_instance():
        return HousingDFRegistry.instance

    def add(self, df, label):
        for place in np.unique(df['Place Name'].values):
            self.place_to_df[place] = df

        for cbsa in np.unique(df['CBSA Code'].values):
            self.cbsa_to_df = df

        self.df_list.append((df, label))

    def get_df_for_place(self, place):
        if place in self.place_to_df:
            return self.place_to_df[place]

        return None

    def get_df_for_cbsa(self, cbsa):
        if cbsa in self.cbsa_to_df:
            return self.cbsa_to_df[cbsa]

        return None

    def save_all(self, data_dir="", prefix=None):
        for (df,label) in self.df_list:
            df.to_pickle("{0}/{1}_saved.pkl".format(data_dir, label))
