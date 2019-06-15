import datetime

class Schedule:
    "Schedule"

    def __init__(self, date:datetime.datetime):
        """
        Initiate Schedule.

        Arguments:
        date -- Date of the schedule
        """
        self._date = date

    @property
    def date(self) -> datetime.datetime:
        "Date scheduled"
        return self._date

    def json(self) -> dict:
        "Return schedule json information present in most of SNCF Api requests"
        data = {}
        data['outward'] = self._date.isoformat()
        data['outwardType'] = 'DEPARTURE_FROM'
        data['inward'] = None
        data['inwardType'] = 'DEPARTURE_FROM'
        return data
