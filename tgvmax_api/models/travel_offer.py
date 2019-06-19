from typing import TypeVar


Travel = TypeVar('Travel')

class TravelOffer:
    
    def __init__(self, data: dict, travel: Travel):
        self._data = data
        self._travel = travel

    @property
    def id(self) -> str:
        if 'id' not in self._data:
            raise ValueError('No id key in travel offer data')
        return self._data['id']

    @property
    def amount(self) -> int:
        if 'amount' not in self._data:
            raise ValueError('No amount key in travel offer data')
        return self._data['amount']

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
