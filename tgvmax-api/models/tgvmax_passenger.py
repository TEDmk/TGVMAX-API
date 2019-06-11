import datetime

class TGVMaxPassenger:

    ADULT = 'ADULT'
    YOUNG = 'YOUNG'

    def __init__(self, hc_number, date_of_birth):   
        self.hc_number = hc_number
        self.date_of_birth = date_of_birth

    def get_json(self):
        data = {}
        data['bicycle'] = None
        data['customerId'] = ''
        data['discountCard'] = {}
        data['discountCard']['code'] = 'HAPPY_CARD'
        data['discountCard']['dateOfBirth'] = self.get_date_of_birth()
        data['discountCard']['number'] = self.get_hc_number()
        data['fidelityCard'] = {'type':'NONE', 'number':''} 
        data['firstname'] = ''
        data['lastname'] = ''
        data['promoCode'] = ''
        data['topology'] = self.get_age_category()
        return data

    def get_hc_number(self):
        return self.hc_number

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_age(self):
        today = datetime.date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

    def get_age_category(self):
        if self.get_age() < 26:
            return TGVMaxPassenger.YOUNG
        return TGVMaxPassenger.ADULT

