

class Currency:
    def __init__(self, currency, rate, multiplier):
        self.__currency = currency
        self.__rate = rate
        self.__multiplier = multiplier

    @property
    def rate(self):
        return self.__rate

    @property
    def multiplier(self):
        return self.__multiplier

    @property
    def currency(self):
        return self.__currency








