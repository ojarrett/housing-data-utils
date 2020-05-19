import flask
from flask import request, jsonify, Flask
from housing_df.registry import HousingDFRegistry
from housing_df.utils import build_housing_df_registry_for_all_regions
from housing_df.place_info.PlaceInfo

app = Flask(__name__)
reg = None
place_info = None

@app.route('/city', methods=['GET'])
def get_city_info():
    if place_info is None:
        place_info = PlaceInfo()
        place_info.build()
    args = request.args
    df = place_info.df
    if 'name' in args:


if __name__ == '__main__':
    build_housing_df_registry_for_all_regions()
    reg = HousingDFRegistry.get_instance()
    app.run()
