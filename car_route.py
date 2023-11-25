from flask import Blueprint, request, render_template
from routes.Objects import CarTaxParam
from routes.region_route import Region
from Config import db

edit_data_car = Blueprint('edit_data_car', __name__)


@edit_data_car.route('/web/tax-param/add')
def render_add_new_tax():
    return render_template('tax-param-add.html')


@edit_data_car.route('/v1/car/tax-param/add', methods=['POST'])
def add_new_tax_auto():
    car_id = request.form['id']
    city_id = request.form['city_id']
    from_hp_car = request.form['from_hp_car']
    to_hp_car = request.form['to_hp_car']
    from_production_year_car = request.form['from_production_year_car']
    to_production_year_car = request.form['to_production_year_car']
    rate = request.form['rate']
    car = list(map(lambda x: x.get_id(), CarTaxParam.query.all()))
    regions = list(map(lambda x: x.get_id(), Region.query.all()))
    if car_id in car and city_id not in regions:
        error_body = {'reason': 'Регион с таким id не существует или автомобильный налог уже существует'}
        return error_body, 400
    else:
        new_data = CarTaxParam(car_id, city_id, from_hp_car, to_hp_car, from_production_year_car,
                               to_production_year_car, rate)
        db.session.add(new_data)
        db.session.commit()
        message = {'reason': 'Автомобильный налог добавлен'}
        return message, 200


@edit_data_car.route('/web/tax-param/update')
def render_update_tax():
    return render_template('tax-param-add.html')


@edit_data_car.route('/v1/car/tax-param/update', methods=['POST'])
def update_tax_auto():
    car_id = request.form['id']
    city_id = request.form['city_id']
    from_hp_car = request.form['from_hp_car']
    to_hp_car = request.form['to_hp_car']
    from_production_year_car = request.form['from_production_year_car']
    to_production_year_car = request.form['to_production_year_car']
    rate = request.form['rate']
    car = list(map(lambda x: x.get_id(), CarTaxParam.query.all()))

    if car_id in car:

        CarTaxParam.query.filter_by(id=car_id).update(
            {'city_id': city_id, 'from_hp_car': from_hp_car, 'to_hp_car': to_hp_car,
             'from_production_year_car': from_production_year_car, 'to_production_year_car': to_production_year_car,
             'rate': rate})
        db.session.commit()
        context = {
            'message': 'Налог обновлен',
            'status': 200
        }
        return render_template('tax-param-update.html', **context)
    else:
        context = {
            'message': 'Налог с таким id не существует',
            'status': 400
        }
        return render_template('tax-param-update.html', **context)


@edit_data_car.route('/web/tax-param/delete')
def render_delete_tax():
    return render_template('tax-param-delete.html')


@edit_data_car.route('/v1/car/delete', methods=['POST'])
def delete_tax_auto():
    car_id = request.form['id']
    car = list(map(lambda x: x.get_id(), CarTaxParam.query.all()))

    if car_id in car:

        CarTaxParam.query.filter_by(id=car_id).delete()
        db.session.commit()
        context = {
            'message': 'Регион удален',
            'status': 200
        }
        return render_template('region-delete.html', **context)
    else:
        context = {
            'message': 'Регион с таким id не существует',
            'status': 400
        }
        return render_template('region-delete.html', **context)


@edit_data_car.route('/web/tax-param')
def fetch_tax_auto(id):
    if id is None:
        error_body = {'reason': 'Не корректные данные'}
        return error_body, 400
    else:
        tax_auto = list(map(lambda x: x.__repr__(), CarTaxParam.query.filter_by(id=id, ).all()))
        return render_template('region-list.html', post=tax_auto)



