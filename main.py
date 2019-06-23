from tgvmax_api import Station, TGVMaxPassenger, WishRequest, Schedule, TrainRequest
import datetime
import json

origin = Station.search_station('FRADI')[0]
destination = Station.search_station('FRPAR')[0]
schedule = Schedule(datetime.datetime(2019, 6, 24, 12))
p = TGVMaxPassenger('200083240', datetime.date(1996, 9, 13))
w = WishRequest(origin, destination, schedule, p)
wish_resp = w.send()
train_req = TrainRequest(wish_resp)
train_resp = train_req.send()
for travel in train_resp.travels:
    for offer in travel.second_class_offers:
        print(f'{offer}: {offer.amount}')
