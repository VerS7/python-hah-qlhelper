import json


class ItemsParser:
    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, 'r') as json_raw:
            self.fl = json.load(json_raw)
        self.name = self.fl['name']
        self.wiki = self.fl['wiki-link']
        self.formula = self.fl['formula']
        self.variables = self.fl['variables']

    def count_result(self):
        """Count result with quality on formula"""
        """Returns eval result of formula string"""
        for elem in self.variables:
            self.formula = self.formula.replace(str(elem), str(self.variables.get(elem)['quality']))
        return eval(self.formula)

    def write_variables(self, _variables):
        """Write variables dict to json file"""
        self.fl['variables'] = _variables
        with open(self.filename, 'w') as json_raw:
            json.dump(json_raw, self.fl)
            return True

#fl = ItemsParser('D:\Python Projects\python-hah-qlhelper\items data\Tree quality.json')