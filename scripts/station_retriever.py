import logg
import requests
import json
import datetime
import time

class StationRetriever:

    @staticmethod
    def requests(keyword: str) -> list:
        headers: dict = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
            'Referer': 'https://www.oui.sncf/',
            'Origin': 'https://www.oui.sncf',
        }
        params: dict = (
            ('uc', 'fr-FR'),
            ('searchField', 'origin'),
            ('searchTerm', str(keyword)),
        )
        response: requests.models.Response = requests.get('https://booking.oui.sncf/booking/autocomplete-d2d', headers=headers, params=params)
        if response.status_code != 200:
            time.sleep(60)
            response = requests.get('https://booking.oui.sncf/booking/autocomplete-d2d', headers=headers, params=params)
        return json.loads(response.text)

    @staticmethod
    def get_stations(keyword: str) -> dict:
        response: requests.models.Response = StationRetriever.requests(keyword)
        stations: dict = {}
        for r in response:
            if r['category'] == 'station':
                stations[r['id']] = r
        return stations

    @staticmethod
    def fetch_all_stations():
        stations_dict: dict = {}
        alphabet: str = 'abcdefghijklmnopqrstuvwxyz'
        keyword_list: list = [f'{x}{y}{z}'
                              for x in alphabet 
                              for y in alphabet
                              for z in alphabet]
        size: int = len(keyword_list)
        progress = logg.ProgressBar(size, fmt=logg.ProgressBar.FULL)
        for key in keyword_list:
            retrieved_stations = StationRetriever.get_stations(key)
            for k, v in retrieved_stations.items():
                stations_dict[k] = v
            progress.current += 1
            progress()
        progress.done()
        return stations_dict

    @staticmethod
    def save_stations(station_list: dict) -> None:
        hashtime: int = int(datetime.datetime.now().timestamp())
        with open(f'stations-{hashtime}.json', 'w') as outfile:
            json.dump(station_list, outfile)

StationRetriever.save_stations(StationRetriever.fetch_all_stations())