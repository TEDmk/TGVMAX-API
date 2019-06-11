from tgvmax_api.models.tgvmax_passenger import TGVMaxPassenger
import datetime


def test_tgvmax_passenger_hc_number():
    try:
        TGVMaxPassenger('2000840', datetime.date(2000, 10, 2))
        assert False
    except ValueError:
        assert True
    except:
        assert False

    try:
        TGVMaxPassenger(859384933, datetime.date(2000, 10, 2))
        assert False
    except ValueError:
        assert True
    except:
        assert False

    try:
        TGVMaxPassenger('lolilol', datetime.date(2000, 10, 2))
        assert False
    except ValueError:
        assert True
    except:
        assert False


def test_tgvmax_passenger_date():
    try:
        TGVMaxPassenger('200082240', datetime.date(2020, 10, 2))
        assert False
    except ValueError:
        assert True
    except:
        assert False


def test_tgvmax_passenger():
    passenger = TGVMaxPassenger('200083240', datetime.date(2000, 10, 2))
    assert passenger.hc_number == '200083240'

def test_tgvmax_passenger_age():
    passenger = TGVMaxPassenger('200083240', datetime.date(2000, 10, 2))
    assert passenger.age == 18
    assert passenger.age_category == TGVMaxPassenger.YOUNG
    passenger2 = TGVMaxPassenger('200083241', datetime.date(1990, 10, 2))
    assert passenger2.age == 28
    assert passenger2.age_category == TGVMaxPassenger.ADULT


def test_tgvmax_passenger_getters():
    passenger = TGVMaxPassenger('200083240', datetime.date(2000, 10, 2))
    assert passenger.hc_number == '200083240'
    date_of_birth = passenger.date_of_birth
    assert date_of_birth.year == 2000
    assert date_of_birth.month == 10
    assert date_of_birth.day == 2