from flask import Blueprint, request, render_template
from routes.Objects import CarTaxParam
from Config import db

calc = Blueprint('calc', __name__)


@calc.route('/v1/calc/tax-param/')
def render_calc():
    return render_template('index.html')


@calc.route('/v1/car/tax/calc', methods=['POST'])
def auto_calc():
    id = request.form['id']
    year = request.form['year']
    hp = request.form['hp']
    if id is None or year is None or hp is None:
        error_body = {'reason': 'Не корректные данные'}
        return error_body, 400

    rate = list(map(lambda x: x.get_data_for_rate(), CarTaxParam.query.filter_by(city_id=id).all()))

    if rate is None:
        error_body = {'reason': 'Нет подходящего налога'}
        return error_body, 400
    else:
        for i in rate:
            if int(i[2]) < int(hp) <= int(i[3]) and int(i[4]) < int(year) <= int(i[5]):
                res = int(i[6]) * int(hp)
                context = {
                    'message': res,
                    'status': 200
                }
                return render_template('index.html', **context)
            else:
                context = {
                    'message': 'Нет налога с такими параметрами',
                    'status': 400
                }
                return render_template('index.html', **context)