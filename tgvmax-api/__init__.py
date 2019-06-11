from models.station import Station
from tgvmax import TGVMax
from models.tgvmax_passenger import TGVMaxPassenger
from requests.wish_request import WishRequest
import datetime

origin = Station.search_station('FRADI')[0]
destination = Station.search_station('FRPAR')[0]
date_departure = datetime.date(2019, 6, 12)
p = TGVMaxPassenger('', datetime.date(1996, 9, 13))
w = WishRequest(origin, destination, date_departure, p)
print(w)
t = TGVMax.search(origin, destination, date_departure)
