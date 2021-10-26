from lab1.import_courses import ImportCourses
from dict_currency import DictCurrency


class Cantor:
    def __init__(self):
        self.__exchange_status = True
        self.__currency_from = None
        self.__currency_to = None
        self.__value = None
        ImportCourses()
        self.__courses = DictCurrency()
        while self.__exchange_status:
            self.currency_input_from()
            self.money_input()
            print(self.__value)
            self.currency_input_to()
            self.exchange_process(self.__courses.currency_dict[self.__currency_from], self.__courses.currency_dict[self.__currency_to],
                                  self.__value)
            self.__exchange_status = self.status()


    def print_courses(self):
        for key in self.__courses.currency_dict:
            print(key, end=" ")
        print()

    def currency_input_from(self):
        print("choose your currency from the list")
        self.print_courses()
        self.__currency_from = input()
        if self.__currency_from not in self.__courses.currency_dict.keys():
            print("try again")
            self.currency_input_from()


    def currency_input_to(self):
        print("enter currency you want to get")
        self.print_courses()
        self.__currency_to = input()
        if self.__currency_to not in self.__courses.currency_dict.keys():
            print("try again")
            self.currency_input_to()

    def money_input(self):
        print("enter your money")
        self.__value = float(input())
        if self.__value <= 0:
            print("try again")
            self.money_input()

    def exchange_process(self, currency_1, currency_2, money_input):
        result_zl = money_input * (currency_1.multiplier * currency_1.rate)
        # print(result_zl)
        result = result_zl / (currency_2.multiplier * currency_2.rate)
        print("%.2f" % result)

    def status(self):
        print("press C to continue or X to exit")
        inputed_v = str(input())
        if inputed_v == "C":
            return True
        elif inputed_v== "X":
            return False
        else:
            print("try again")
            self.status()
