import json
import os 


dir_path = os.path.dirname(os.path.realpath(__file__))


class Station:
    "Train station available in the SNCF rail network"

    stations_list = json.load(open(f'{dir_path}/../resources/stations.json', 'r'))
    "Static variable that contains a dict with all registered train station. The key is the station code (.i.e FRPAR for Paris)"

    def __init__(self, code: str) -> None:
        """Initiate Station
        
        Arguments:
        code -- The station code (i.e. FRPAR for Intramuros Paris)
        """
        if code not in Station.stations_list:
            raise ValueError('Station code doesn\'t exist')
        self._code = code
        self._data = Station.stations_list[code]

    @property
    def code(self) -> str:
        "Return station code"
        return self._code

    @property
    def label(self) -> str:
        "Return station label"
        if 'label' not in self._data:
            return None
        return str(self._data['label'])

    @property
    def latitude(self) -> float:
        "Return station latitude coordinate"
        if 'latitude' not in self._data:
            return None
        return float(self._data['latitude'])

    @property
    def longitude(self) -> float:
        "Return station longitude coordinate"
        if 'longitude' not in self._data:
            return None
        return float(self._data['longitude'])

    @property
    def ouibus(self) -> str:
        "Return the station ouibus code"
        if 'ouiBusCode' not in self._data:
            return None
        return str(self._data['ouiBusCode'])

    @property
    def tess(self) -> str:
        "Return the station tess code"
        if 'tessCode' not in self._data:
            return None
        return str(self._data['tessCode'])

    @property
    def resarail(self) -> str:
        "Return the station resarail code"
        if 'rrCode' not in self._data:
            return None
        return str(self._data['rrCode'])

    def json(self) -> dict:
        "Return station json information present in most of SNCF Api requests"
        data = {}
        data['address'] = {'country': 'FR'}
        data['code'] = self.code
        data['codes'] = {
            'GEOHASH': {},
            'OUIBUS': {'code':self.ouibus},
            'RESARAIL': {'code':self.resarail},
            'TESS': {'code':self.tess}
        }
        data['label'] = self.label
        data['latitude'] = self.latitude
        data['longitude'] = self.longitude
        return data

    def __repr__(self):
        return f'<Station {self.code}: \'{self.label}\'>'

    @staticmethod
    def search_station(keyword: str) -> list:
        """Search a station thanks to a keyword
        
        Arguments:
        keyword -- Keyword contained in the station label or code

        Returned:
        List of corresponding stations
        """
        returned_station = []
        for code, data in Station.stations_list.items():
            if keyword.lower() in data['label'].lower() or keyword.lower() in code.lower():
                returned_station.append(Station(data['id']))
        return returned_station