import json

class Storage():
    def ValueOutput(self):
        with open('../Utils/test_data.json') as f:
            slov = json.load(f)
        return slov

    def ConfigOutput(self):
        with open('../Utils/config.json') as f:
            slov = json.load(f)
        return slov

    def ValueStorage(self, outerkey = None, innerkey = None, keyvalue = None):
        with open('../Utils/test_data.json') as f:
            l = json.load(f)
        if innerkey == None: l[outerkey] = keyvalue
        else: l[outerkey][innerkey] = keyvalue

        with open('../Utils/test_data.json', 'w') as f:
            f.write(json.dumps(l))