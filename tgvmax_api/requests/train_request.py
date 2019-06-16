from tgvmax_api.models.wish_response import WishResponse
import datetime
import json
import requests

class TrainRequest:
    "Train request which returns all trains"

    url = 'https://www.oui.sncf/proposition/rest/travels/outward/train'

    @staticmethod
    def _headers(id):
        headers = {
            'Origin': 'https://www.oui.sncf',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
            'X-VSD-LOCALE': 'fr-FR',
            'content-type': 'application/json',
            'Accept': '*/*',
            'Referer': f'https://www.oui.sncf/proposition/outward/train?wishId={id}',
            'Connection': 'keep-alive',
        }
        return headers

    def __init__(self, wish_response: WishResponse):
        if type(wish_response) != WishResponse:
            ValueError(f'WishRequest ("{wish_response}") is not valid')
        self._wish_response = wish_response
        self._wish_resquest = wish_response.request
        self.data = {}
        self.data['context'] = {}
        self.data['wish'] = self._wish_resquest.data
        self.data['wish'] = {**self.data['wish'], **{
            'channel': 'web',
            'asymmetricalJourney': None,
            'context': {
                'sumoForTrain': {
                    'eligible': True
                },
                'sumoForBus': {
                    'eligible': True
                }
            },
            'sellerParner': None
        }}
        for key, value in self._wish_response.json().items():
            if key in ['id', 'warnings']:
                self.data[key] = value
        self.data['wish']['created'] = datetime.datetime.now().isoformat()

    def send(self):
        "send the request and return the result"
        response = requests.post(TrainRequest.url, headers=TrainRequest._headers(self._wish_response.id), data=json.dumps(self.data))
        return response.text

    def __repr__(self):
        return f'<WishRequest [{str(self._wish_resquest.schedule.date)}] {self._wish_resquest.origin_station.code} -> {self._wish_resquest.destination_station.code}>'
