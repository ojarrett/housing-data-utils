import flask
from flask import abort, request, jsonify, Flask
from housing_df.registry import HousingDFRegistry
from housing_df.utils import build_housing_df_registry_for_all_regions
from housing_df.place_info import PlaceInfo
from housing_df.series_builder import HousingSeriesBuilder

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

@app.route('/city/<int:place_id>/housing', methods=['GET'])
def get_city_housing_data(place_id):
    if place_id not in place_info.df.index:
        abort(404)

    place_record = place_info.df.loc[place_id]
    place_name = place_record['Place Name']
    housing = reg.get_df_for_region(place_record['Region'])

    start = int(request.args['start']) if 'start' in request.args else None
    end = int(request.args['end']) if 'end' in request.args else None

    series_builder = HousingSeriesBuilder(housing)
    series = series_builder.build(place_name, start, end)
    print("Start: {0}, End: {1}".format(str(start), str(end)))

    return series.to_json(orient='records')

@app.route('/city/<int:place_id>/housing/<int:building_size>', methods=['GET'])
def get_city_housing_series(place_id, building_size):
    pass

if __name__ == '__main__':
    reg = build_housing_df_registry_for_all_regions()
    reg.save_all()

    place_info = PlaceInfo(reg)
    place_info.build()

    # Pandas to_json does not include the index for record format JSON
    place_info.df['id'] = place_info.df.index
    app.run()
