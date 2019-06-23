from tgvmax_api.models.generic import from_dict

class Fare:

    def __init__(self, data):
        self._data = data

    @property
    def fare_code(self):
        return from_dict(self._data, ['metaData', 'MI', 'code'])

    @property
    def return_mandatory(self):
        return from_dict(self._data, ['returnMandatory'])

    @property
    def id(self):
        return from_dict(self._data, ['id'])

    @property
    def mi_id(self):
        try:
            return from_dict(self._data, ['metaData', 'MI', 'miId'])
        except ValueError:
            return from_dict(self._data, ['metaData', 'MI', 'id'])

    def json(self):
        data = {}
        data['activableByCode'] = False
        data['fareConditions'] = None
        data['fareName'] = None
        data['fareSequence'] = None
        data['fareSpecificRule'] = None
        data['id'] = self.mi_id
        data['fareCode'] = self.fare_code
        data['returnMandatory'] = self.return_mandatory
        return data

    def __repr__(self):
        return f'<Fare {self.mi_id}:{self.fare_code}>'