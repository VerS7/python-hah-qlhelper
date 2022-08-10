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
        if self.softcap() >= eval(formula) or self.softcap() == 0:
            return round(eval(formula))
        else:
            return round((eval(formula) + self.softcap())/2)

    def softcap(self):
        """Count softcap from stats"""
        return pow(reduce(mul, self.stats.values()), 1/(len(self.stats)))

    def write_variables(self, _variables):
        """Write variables dict to json file"""
        self.fl['variables'] = _variables
        with open(self.filename, 'w') as json_raw:
            json.dump(json_raw, self.fl)

    def write_stats(self, _stats):
        """Write stats dict to json file"""
        self.fl['stats'] = _stats
        with open(self.filename, 'w') as json_raw:
            json.dump(json_raw, self.fl)


# fl = ItemsParser(r'D:\Python Projects\python-hah-qlhelper\items data\Unfired TreePot.json')
# print(fl.variables)
# print(fl.formula)
# print(fl.name)
# print(fl.wiki)
# print(fl.count_result())
