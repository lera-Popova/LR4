from Config import app

from routes.region_route import edit_data
from routes.car_route import edit_data_car
# from routes.area_route import edit_data_area

app.register_blueprint(edit_data)
app.register_blueprint(edit_data_car)
# app.register_blueprint(edit_data_area)


if __name__ == '__main__':
    app.run(debug=True)
