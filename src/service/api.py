import flask
from flask import abort, request, jsonify, Flask
from housing_df.registry import HousingDFRegistry
from housing_df.utils import build_housing_df_registry_for_all_regions
from housing_df.place_info import PlaceInfo

app = Flask(__name__)
reg = None
place_info = None

@app.route('/city', methods=['GET'])
def get_city_info():
    return place_info.df.to_json(orient='records')

@app.route('/city/<int:place_id>', methods=['GET'])
def get_specific_city_info(place_id):
    if place_id not in place_info.df.index:
        abort(404)

    return place_info.df.loc[place_id].to_json()

if __name__ == '__main__':
    reg = build_housing_df_registry_for_all_regions()
    reg.save_all()

    place_info = PlaceInfo(reg)
    place_info.build()

    # Pandas to_json does not include the index for record format JSON
    place_info.df['id'] = place_info.df.index
    app.run()
