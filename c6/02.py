import json
from urllib.request import urlopen
from pprint import pprint

from collections import OrderedDict

#u = urlopen('https://docs.python.org/2/library/json.html')
#resp = json.loads(u.read().decode('utf-8'))

#pprint(resp)

s='{"name": "ACME", "shares": 50, "price": 490.1}'
data = json.loads(s, object_pairs_hook=OrderedDict)
#print(data)

class JSONObject:
    def __init__(self, d):
        self.__dict__ = d
        
data=json.loads(s, object_hook=JSONObject)
print(data.name)
#No difference for the following two format
print(json.dumps(s, sort_keys=True))
print(json.dumps(s, indent=4))
