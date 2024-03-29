import json
from typing import TypeVar
from tgvmax_api.models.travel import Travel
from tgvmax_api.models.generic import from_dict
from tgvmax_api.models.fare import Fare

TrainRequest = TypeVar('TrainRequest')

class TrainResponse:
    "Object returned by the train_request.send method. This contains all info about train response"


    def __init__(self, raw: str='', status: str='', request: TrainRequest=None):
        """
        Initiate WishReponse

        Arguments:
        raw -- Raw data of the response
        status -- status of the TrainResponse. Use this when raw='' due to an error
        request -- request that received the response
        """
        if type(raw) != str:
            ValueError(f'Raw ("{raw}") is not a string')
        if type(raw) != str:
            ValueError(f'Status ("{raw}") is not a string')
        if type(request) != TrainRequest:
            ValueError(f'Request ("{raw}") is not a TrainRequest')
        self._request = request
        self._raw = raw
        self._json = json.loads(raw)
        self._status = status

    @property
    def request(self):
        "Return the request"
        return self._request

    @property
    def travels(self):
        travel_list = []
        for travel in from_dict(self._json, ['travelProposals']):
            travel_list.append(Travel(travel))
        return travel_list

    @property
    def fares(self):
        fare_list = []
        for fare in from_dict(self._json, ['fares']):
            fare_list.append(Fare(fare))
        return fare_list

    def json(self):
        "return the json of the response"
        return self._json

    @property
    def id(self) -> str:
        "Return the wish ID"
        if not self.succeed:
            None
        return self._json['id']

    @property
    def status(self) -> str:
        "Return the status"
        if self._status:
            return self._status
        return 'SUCCESS' if len(self._json['errors'])==0 else 'REQUEST_DATA_ERROR'

    @property
    def errors(self) -> str:
        "Return the errors"
        if 'errors' not in self._json:
            return None
        return json.dumps(self._json['errors'])

    @property
    def succeed(self) -> bool:
        "Return if the request succeed (there is a wish id)"
        return True if self.status=='SUCCESS' else False

    def __repr__(self):
        return f'<TrainResponse [status={self.status}]>'
