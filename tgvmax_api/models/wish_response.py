import json


class WishResponse:
    "Object returned by the wish_request.send method. This contains all info about wish response"


    def __init__(self, raw='', status=''):
        """
        Initiate WishReponse

        Arguments:
        raw -- Raw data of the response
        status -- status of the WishResponse. Use this when raw='' due to an error
        """
        self._raw = raw
        self._json = json.loads(raw)
        self._status = status
        
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
        return 'SUCCESS' if self._json['id'] else 'REQUEST_DATA_ERROR'

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
        return f'<WishResponse [status={self.status}]>'
