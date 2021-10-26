import requests
import xml.etree.ElementTree as ET
from currency import Currency
from dict_currency import DictCurrency


class ImportCourses:
    def __init__(self):
        self.__dict_c = DictCurrency()
        self.__root = self.things_with_xml()
        print(type(self.__root))
        self.update_dict(self.__root)

    def things_with_xml(self):
        URL = "https://www.nbp.pl/kursy/xml/lasta.xml"

        response = requests.get(URL)
        response.raise_for_status()
        with open('../feed.xml', 'wb') as file:
            file.write(response.content)

        tree = ET.parse('../feed.xml')
        root = tree.getroot()
        return root

    def update_dict(self,root):
        self.__dict_c.currency_dict.update({"PLN": Currency("PLN", 1.0, 1.0)})
        for country in root.findall('pozycja'):
            name = country.find('kod_waluty').text
            rate = country.find('kurs_sredni').text
            rate = rate.replace(',', '.')
            multiplier = country.find('przelicznik').text
            multiplier = multiplier.replace(',', '.')
            # print(name, rate, multiplier)
            self.__dict_c.currency_dict.update({name: Currency(name, float(rate), float(multiplier))})
