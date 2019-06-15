from tgvmax_api.models.wish_response import WishResponse
from tgvmax_api.models.station import Station
from tgvmax_api.models.schedule import Schedule
from tgvmax_api.models.passenger import Passenger
import requests
import json


class WishRequest:
    "Wish request allows to ask for a wish ID, used in the train request"

    base_wish_request = {
        'checkBestPrices': False,
        'CodeFce': None,
        'directTravel': False,
        'mainJourney': {
            'via': None,
        },
        'pets': [],
        'salesMarket': 'fr-FR',
        'travelClass': 'SECOND'
    }
    "Base of the Wish request"

    headers = {
        'Origin': 'https://www.oui.sncf',
        'Accept-Encoding': 'gzip, deflate, br',
        'x-oui-search-canal': 'web',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Referer': 'https://www.oui.sncf/',
        'Connection': 'keep-alive',
    }
    "Header of the request"

    url = 'https://www.oui.sncf/wishes-api/wishes'
    "url of the request"

    def __init__(self, origin_station: Station, destination_station: Station, schedule: Schedule, passenger: Passenger):
        """
        Initiate WishRequest

        Arguments:
        origin_station -- origin station of the request
        destination_station -- destination station of the request
        schedule -- schedule of the request
        passenger -- passenger of the request
        """
        self.origin_station = origin_station
        self.destination_station = destination_station
        self.passenger = passenger
        self.schedule = schedule
        self.data = WishRequest.base_wish_request.copy()
        self.data['mainJourney']['origin'] = self.origin_station.json()
        self.data['mainJourney']['destination'] = self.destination_station.json()
        self.data['passengers'] = [self.passenger.json()]
        self.data['schedule'] = self.schedule.json()

    def send(self) -> WishResponse:
        "send the request and return the result"
        try:
            response = requests.post(WishRequest.url, headers=WishRequest.headers, data=json.dumps(self.data))
            return WishResponse(raw=response.text)
        except requests.exceptions.ConnectionError:
            return WishResponse(raw='', status='CONNECTION_ERROR')

    def __repr__(self):
        return f'<WishRequest [{str(self.schedule.date)}] {self.origin_station.code} -> {self.destination_station.code}>'
