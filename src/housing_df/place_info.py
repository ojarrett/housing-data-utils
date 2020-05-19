from housing_df.registry import HousingDFRegistry
from housing_df.utils import build_housing_df_registry_for_all_regions

import pandas as pd

SAMPLE_DATE = 201012
PLACE_INFO_COLUMNS = ['Place Name','CBSA Code', 'Pop']

class PlaceInfo:
    def __init__(self, registry, sample_date=SAMPLE_DATE):
        self.df = None
        self.registry = registry
        self.sample_date = sample_date

    def build(self):
        registry = self.registry
        result = None
        if registry:
            for (df, label) in registry.df_list:
                sample = df[df['Survey Date'] == self.sample_date][PLACE_INFO_COLUMNS]
                sample['Region'] = label
                if result is None:
                    result = sample
                else:
                    result = pd.concat([result, sample])
            self.df = result
