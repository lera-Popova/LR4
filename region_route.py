from flask import Blueprint, request, render_template
from routes.Objects import Region, CarTaxParam

from Config import db

edit_data = Blueprint('edit_data', __name__)


@edit_data.route('/web/region/add')
def render_add_new_region():
    return render_template('region-add.html')


@edit_data.route('/v1/add/tax', methods=['POST'])
def add_new_region():
    region_id = int(request.form['id'])
    region_name = request.form['name']
    regions = list(map(lambda x: x.get_id(), Region.query.all()))
    if region_id in regions:
        context = {
            'message': 'Регион уже существует',
            'status': 400
        }
        return render_template('region-add.html', **context)
    else:
        new_data = Region(region_id, region_name)
        db.session.add(new_data)
        db.session.commit()
        context = {
            'message': 'Регион добавлен',
            'status': 200
        }
        return render_template('region-add.html', **context)


@edit_data.route('/web/region/update')
def render_update_region():
    return render_template('region-update.html')


@edit_data.route('/v1/region/update', methods=['POST'])
def update_region():
    region_id = int(request.form['id'])
    print(region_id)
    region_name = request.form['name']
    region = list(map(lambda x: x.get_id(), Region.query.all()))
    print(region)
    if region_id in region:
        Region.query.filter_by(id=region_id).update({'name': region_name})
        db.session.commit()
        context = {
            'message': 'Регион обновлен',
            'status': 200
        }
        return render_template('region-update.html', **context)
    else:
        context = {
            'message': 'Регион с таким id не существует',
            'status': 400
        }
        return render_template('region-update.html', **context)


@edit_data.route('/web/region/region')
def render_delete_region():
    return render_template('region-delete.html')


@edit_data.route('/web/region/delete', methods=['POST'])
def delete_region():
    region_id = int(request.form['id'])
    region = list(map(lambda x: x.get_id(), Region.query.all()))

    if region_id in region:
        CarTaxParam.query.filter_by(city_id=id).delete()
        Region.query.filter_by(id=id).delete()
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


@edit_data.route('/web/region')
def fetch_region():
    # if id is None:
    #     error_body = {'reason': 'Не корректные данные'}
    #     return render_template('region-list.html', list=error_body)
    # else:
    region = list(map(lambda x: x.__repr__(), Region.query.filter_by().all()))
    return render_template('region-list.html', post=region)
