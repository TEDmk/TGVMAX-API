from tgvmax_api.models.station import Station
from tgvmax_api.models.travel_offer import TravelOffer

class Travel:

    def __init__(self, data={}):
        self._data = data

    @property
    def origin(self) -> Station:
        "Return station object of travel origin"
        if 'origin' not in self._data:
            raise ValueError('No origin key in travel data')
        if 'station' not in self._data['origin']:
            raise ValueError('No station key in travel data[origin]')
        if 'metaData' not in self._data['origin']['station']:
            raise ValueError('No metaData key in travel data[origin][station]')
        if 'MI' not in self._data['origin']['station']['metaData']:
            raise ValueError('No MI key in travel data[origin][station][metaData]')
        if 'code' not in self._data['origin']['station']['metaData']['MI']:
            raise ValueError('No MI key in travel data[origin][station][metaData][MI]')
        return Station(self._data['origin']['station']['metaData']['MI']['code'])
    
    @property
    def destination(self) -> Station:
        "Return station object of travel destination"
        if 'destination' not in self._data:
            raise ValueError('No destination key in travel data')
        if 'station' not in self._data['destination']:
            raise ValueError('No station key in travel data[destination]')
        if 'metaData' not in self._data['destination']['station']:
            raise ValueError('No metaData key in travel data[destination][station]')
        if 'MI' not in self._data['destination']['station']['metaData']:
            raise ValueError('No MI key in travel data[destination][station][metaData]')
        if 'code' not in self._data['destination']['station']['metaData']['MI']:
            raise ValueError('No MI key in travel data[destination][station][metaData][MI]')
        return Station(self._data['destination']['station']['metaData']['MI']['code'])

    @property
    def duration(self) -> int:
        "return duration in second"
        if 'duration' not in self._data:
            raise ValueError('No duration key in travel data')
        return int(self._data['duration'])

    @property
    def functional_id(self) -> str:
        "return functionalId of the travel"
        if 'functionalId' not in self._data:
            raise ValueError('No functionalId key in travel data')
        return int(self._data['functionalId'])

    @property
    def uuid(self) -> str:
        "return uuid of the travel"
        if 'id' not in self._data:
            raise ValueError('No id key in travel data')
        return int(self._data['id'])
    
    