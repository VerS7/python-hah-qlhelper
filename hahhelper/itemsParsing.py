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

    # Not working rn
    def write_variables(self):
        """Write variables dict to json file"""
        self.fl['variables'] = self.variables
        with open(self.filename, 'w') as json_raw:
            json.dump(json_raw, self.fl)

    # Not working rn
    def write_stats(self):
        """Write stats dict to json file"""
        self.fl['stats'] = self.stats
        with open(self.filename, 'w') as json_raw:
            json.dump(json_raw, self.fl)


# fl = ItemsParser(r'D:\Python Projects\python-hah-qlhelper\items data\Unfired TreePot.json')
# print(fl.variables)
# print(fl.formula)
# print(fl.stats)
# print(fl.name)
# print(fl.wiki)
# print(fl.count_result())
