from tgvmax_api.models.station import Station

def test_station_exists():
    try:
        Station('FRPA')
        assert False
    except ValueError:
        assert True
    except:
        assert False

    s = Station('FRPAR')
    assert s.code == 'FRPAR'

def test_station_properties():
    s = Station('FRPAR')
    assert s.code == 'FRPAR'
    assert s.label == 'Paris (toutes gares intramuros)'
    assert s.resarail == 'FRPAR'
    assert s.tess == '5507'
    assert s.ouibus == 'PAR'
    assert s.latitude == 48.8568
    assert s.longitude == 2.35103

def test_station_search():
    s = Station.search_station('dunk')
    assert len(s) == 1
    assert s[0].code == 'FRADI'
