import datetime
import re


class TGVMaxPassenger:

    ADULT = 'ADULT'
    YOUNG = 'YOUNG'
    
    def __init__(self, hc_number: str, date_of_birth:datetime.date):
        if type(hc_number) != str:
            raise ValueError(f'HC Number "{str(hc_number)}" has not a valid type')
        if not re.match('^[0-9]{9}$', hc_number):
            raise ValueError(f'HC Number "{str(hc_number)}" is not valid')
        if type(date_of_birth) != datetime.date:
            raise ValueError(f'Please pass a datetime.date for date_of_birth')
        if date_of_birth > datetime.date.today():
            raise ValueError(f'Please pass a date_of_birth prior to today')
        self._hc_number = hc_number
        self._date_of_birth = date_of_birth

    def json(self) -> dict:
        data = {}
        data['bicycle'] = None
        data['customerId'] = ''
        data['discountCard'] = {}
        data['discountCard']['code'] = 'HAPPY_CARD'
        data['discountCard']['dateOfBirth'] = self.date_of_birth
        data['discountCard']['number'] = self.hc_number
        data['fidelityCard'] = {'type':'NONE', 'number':''} 
        data['firstname'] = ''
        data['lastname'] = ''
        data['promoCode'] = ''
        data['topology'] = self.age_category
        return data

    @property
    def hc_number(self) -> str:
        return self._hc_number

    @property
    def date_of_birth(self) -> str:
        return self._date_of_birth

    @property
    def age(self) -> int:
        today = datetime.date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

    @property
    def age_category(self) -> str:
        if self.age < 26:
            return TGVMaxPassenger.YOUNG
        return TGVMaxPassenger.ADULT