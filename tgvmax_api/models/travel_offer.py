from typing import TypeVar
from tgvmax_api.models.generic import from_dict

Travel = TypeVar('Travel')

class TravelOffer:
    
    def __init__(self, data: dict, travel: Travel):
        self._data = data
        self._travel = travel

    @property
    def id(self) -> str:
        return from_dict(self._data, 'id')

    @property
    def amount(self) -> int:
        return from_dict(self._data, 'amount')

    @property
    def travelClass(self) -> int:
        if 'travelClass' not in self._data:
            raise ValueError('No travelClass key in travel offer data')
        if self._data['travelClass']=='1ère':
            return 1
        elif self._data['travelClass']=='2nde':
            return 2
        else:
            raise ValueError('TravelClass is neither first or second class')

    @property
    def fare_id(self):
        "return the fare id of the travel"
        return from_dict(self._data, ['passengerOfferBySegment', 0, 'idFare'])

    def __repr__(self):
        return f'<TravelOffer {self.id}>'