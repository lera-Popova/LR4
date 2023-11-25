from Config import db


class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)

    # функция для получения айди региона из бд
    def get_id(self):
        return self.id

    # функция для получения айди и названия региона из бд
    def __repr__(self):
        return f'<Region ID: {self.id}; Region name: {self.name}>'

    # функция для внесения айди региона в бд
    def __init__(self, id, name):
        self.id = id
        self.name = name


class CarTaxParam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, nullable=False)
    from_hp_car = db.Column(db.Integer, nullable=False)
    to_hp_car = db.Column(db.Integer, nullable=False)
    from_production_year_car = db.Column(db.Integer, nullable=False)
    to_production_year_car = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Numeric, nullable=False)

    # функция для внесения данных автоналога в бд
    def __init__(self, id, city_id, from_hp_car, to_hp_car, from_production_year_car, to_production_year_car, rate):
        self.id = id
        self.city_id = city_id
        self.from_hp_car = from_hp_car
        self.to_hp_car = to_hp_car
        self.from_production_year_car = from_production_year_car
        self.to_production_year_car = to_production_year_car
        self.rate = rate

    # функция для получения структурированных данных автоналога из бд
    def __repr__(self):
        return f'< Tax ID: {self.id}; City ID {self.city_id}; From HP car: {self.from_hp_car}; To HP car: {self.to_hp_car}; From production year car {self.from_production_year_car}; To production year car: {self.to_production_year_car}; Rate {self.rate}>'

    # функция для получения сухих данных автоналога из бд
    def get_data_for_rate(self):
        return self.id, self.city_id, self.from_hp_car, self.to_hp_car, self.from_production_year_car, self.to_production_year_car, self.rate

    # функция для получения айди автоналога из бд
    def get_id(self):
        return self.id
