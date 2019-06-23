from tgvmax_api.models.station import Station
from tgvmax_api.models.travel_offer import TravelOffer
from tgvmax_api.models.fare import Fare
from tgvmax_api.models.travel_offer import TravelOffer
from tgvmax_api.models.generic import from_dict
import datetime

class Travel:

    def __init__(self, data={}):
        self._data = data

    @property
    def origin(self) -> Station:
        "Return station object of travel origin"
        return Station(from_dict(self._data, ['origin', 'station', 'metaData', 'MI', 'code']))
    
    @property
    def destination(self) -> Station:
        "Return station object of travel destination"
        return Station(from_dict(self._data, ['destination', 'station', 'metaData', 'MI', 'code']))

    @property
    def duration(self) -> int:
        "return duration in second"
        return from_dict(self._data, ['duration'])

    @property
    def functional_id(self) -> str:
        "return functionalId of the travel"
        return from_dict(self._data, ['functionalId'])

    @property
    def arrival_date(self) -> datetime.datetime:
        "return arrival date of the travel in datetime format"
        return datetime.datetime.strptime(from_dict(self._data, ['arrivalDate']), "%Y-%m-%dT%H:%M:%S")

    @property
    def departure_date(self) -> datetime.datetime:
        "return arrival date of the travel in datetime format"
        return datetime.datetime.strptime(from_dict(self._data, ['departureDate']), "%Y-%m-%dT%H:%M:%S")

    @property
    def id(self) -> str:
        "return uuid of the travel"
        return from_dict(self._data, ['id'])
    
    @property
    def first_class_offers(self):
        if not from_dict(self._data, ['firstClassOffers']):
            return []
        offer_list = []
        for offer in from_dict(self._data, ['firstClassOffers', 'offers']):
            if offer != None:
                offer_list.append(TravelOffer(offer, self))
        return offer_list

    @property
    def second_class_offers(self):
        if not from_dict(self._data, ['secondClassOffers']):
            return []
        offer_list = []
        for offer in from_dict(self._data, ['secondClassOffers', 'offers']):
            if offer != None:
                offer_list.append(TravelOffer(offer, self))
        return offer_list

    def __repr__(self):
        return f'<Travel {self.id}: {self.origin.code}->{self.destination.code}>'
