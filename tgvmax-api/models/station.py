import json
import os 


dir_path = os.path.dirname(os.path.realpath(__file__))


class Station:

    stations_list = json.load(open(f'{dir_path}/../resources/stations.json', 'r'))

    def __init__(self, code):
        if code not in Station.stations_list:
            raise ValueError('Station code doesn\'t exist')
        self.code = code
        self.data = Station.stations_list[code]

    def get_code(self):
        return self.code

    def get_label(self):
        if 'label' not in self.data:
            return None
        return self.data['label']

    def get_latitude(self):
        if 'latitude' not in self.data:
            return None
        return self.data['latitude']

    def get_longitude(self):
        if 'longitude' not in self.data:
            return None
        return self.data['longitude']

    def get_ouibus(self):
        if 'ouiBusCode' not in self.data:
            return None
        return self.data['ouiBusCode']

    def get_tess(self):
        if 'tessCode' not in self.data:
            return None
        return self.data['tessCode']

    def get_resarail(self):
        if 'rrCode' not in self.data:
            return None
        return self.data['rrCode']

    @staticmethod
    def get_json(self):
        data = {}
        data['address'] = {'country': 'FR'}
        data['code'] = self.get_code()
        data['codes'] = {
            'GEOHASH': {},
            'OUIBUS': {'code':self.get_ouibus()},
            'RESARAIL': {'code':self.get_resarail()},
            'TESS': {'code':self.get_tess()}
        }
        data['label'] = self.get_label()
        data['latitude'] = self.get_latitude()
        data['longitude'] = self.get_longitude()
        return data

    def __repr__(self):
        return f'<Station {self.get_code()}: \'{self.get_label()}\'>'

    @staticmethod
    def search_station(keywords):
        returned_station = []
        for code, data in Station.stations_list.items():
            if keywords.lower() in data['label'].lower() or keywords.lower() in code.lower():
                returned_station.append(Station(data['id']))
        return returned_station