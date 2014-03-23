import requests
from pprint import pprint
import json

r = requests.get("http://openstates.org/api/v1//legislators/?state=nv&active=true&apikey=d2d67bda8f124cbdb77636a4305c1196")
r = r.text
r = json.loads(r)
pprint(r)