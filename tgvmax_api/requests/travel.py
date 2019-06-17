from tgvmax_api.models.station import Station

class Travel:

    def __init__(self, data={}):
        self.data = data

    @property
    def origin(self) -> Station:
        "Return station object of travel origin"
        if 'origin' not in self.data:
            raise ValueError('No origin key in travel data')
        if 'station' not in self.data['origin']:
            raise ValueError('No station key in travel data[origin]')
        if 'metaData' not in self.data['origin']['station']:
            raise ValueError('No metaData key in travel data[origin][station]')
        if 'MI' not in self.data['origin']['station']['metaData']:
            raise ValueError('No MI key in travel data[origin][station][metaData]')
        if 'code' not in self.data['origin']['station']['metaData']['MI']:
            raise ValueError('No MI key in travel data[origin][station][metaData][MI]')
        return Station(self.data['origin']['station']['metaData']['MI']['code'])
    
    @property
    def destination(self) -> Station:
        "Return station object of travel destination"
        if 'destination' not in self.data:
            raise ValueError('No destination key in travel data')
        if 'station' not in self.data['destination']:
            raise ValueError('No station key in travel data[destination]')
        if 'metaData' not in self.data['destination']['station']:
            raise ValueError('No metaData key in travel data[destination][station]')
        if 'MI' not in self.data['destination']['station']['metaData']:
            raise ValueError('No MI key in travel data[destination][station][metaData]')
        if 'code' not in self.data['destination']['station']['metaData']['MI']:
            raise ValueError('No MI key in travel data[destination][station][metaData][MI]')
        return Station(self.data['destination']['station']['metaData']['MI']['code'])

    @property
    def duration(self) -> int:
        "return duration in second"
        if 'duration' not in self.data:
            raise ValueError('No duration key in travel data')
        return int(self.data['duration'])

    @property
    def functional_id(self) -> str:
        "return functionalId of the travel"
        if 'functionalId' not in self.data:
            raise ValueError('No functionalId key in travel data')
        return int(self.data['functionalId'])

    @property
    def uuid(self) -> str:
        "return uuid of the travel"
        if 'id' not in self.data:
            raise ValueError('No id key in travel data')
        return int(self.data['id'])
    
    