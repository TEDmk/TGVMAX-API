from tgvmax_api import Station, TGVMaxPassenger, WishRequest, Schedule, TrainRequest
import datetime
import json

origin = Station.search_station('FRADI')[0]
destination = Station.search_station('FRPAR')[0]
schedule = Schedule(datetime.datetime(2019, 6, 18, 12))
p = TGVMaxPassenger('200083240', datetime.date(1996, 9, 13))
w = WishRequest(origin, destination, schedule, p)
wish_resp = w.send()
train_req = TrainRequest(wish_resp)
json.dump(train_req.send()._json, open('stations.json', 'w'))
