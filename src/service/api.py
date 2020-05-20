import flask
from flask import request, jsonify, Flask
from housing_df.registry import HousingDFRegistry
from housing_df.utils import build_housing_df_registry_for_all_regions
from housing_df.place_info import PlaceInfo

app = Flask(__name__)
reg = None
place_info = None

@app.route('/city', methods=['GET'])
def get_city_info():
    place_info = PlaceInfo(reg)
    place_info.build()
    df = place_info.df

    # Pandas to_json does not include the index for record format JSON
    df['id'] = df.index

    return df.to_json(orient='records')

if __name__ == '__main__':
    reg = build_housing_df_registry_for_all_regions()
    reg.save_all()

    app.run()
