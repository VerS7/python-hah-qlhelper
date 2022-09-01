import json
from math import *
from functools import reduce
from operator import mul


class ItemsParser:
    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, 'r') as json_raw:
            self.fl = json.load(json_raw)
        self.name = self.fl['name']
        self.wiki = self.fl['wiki-link']
        self.formula = self.fl['formula']
        self.variables = self.fl['variables']
        self.stats = self.fl['stats']

    def count_result(self):
        """Count result with quality on formula"""
        """Returns rounded eval result of formula"""
        formula = self.formula
        for elem in self.variables:
            formula = formula.replace(str(elem), str(self.variables.get(elem)))
        if len(self.stats) > 0:
            """if stats exist"""
            if self.softcap() >= eval(formula) or self.softcap() == 0:
                return round(eval(formula))
            elif self.softcap() <= eval(formula):
                return round((eval(formula) + self.softcap())/2)
        elif len(self.stats) == 0:
            """if stats isnt exist"""
            return round(eval(formula))

    def softcap(self):
        """Count softcap from stats"""
        return pow(reduce(mul, self.stats.values()), 1/(len(self.stats)))


x = ItemsParser(r'D:\Python Projects\python-hah-qlhelper\items data\Bow Damage.json')
print(x.count_result())