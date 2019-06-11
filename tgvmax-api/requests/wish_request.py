class WishRequest:

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

    def __init__(self, origin_station, destination_station, date_departure, passenger):
        self.origin_station = origin_station
        self.destination_station = destination_station
        self.date_departure = date_departure
        self.passenger = passenger
        self.data = {}

    def _set_data(self):
        self.data = Wish.base_wish_request.copy()
        self.data['mainJourney']['origin'] = self.origin_station.get_json()
        self.data['mainJourney']['destination'] = self.destination_station.get_json()
        self.data['passengers'] = [self.passenger.get_json()]

    def __repr__(self):
        return f'<WishRequest [{self.date_departure.strftime('%m/%d/%Y')}] {self.origin_station.get_code()} -> {self.destination_station.get_code()}>'
