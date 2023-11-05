import requests
import CONSTANTS
import json

response = requests.get(url=CONSTANTS.ENACTED_URL, headers=CONSTANTS.header)
data = response.json()['results'][0]['bills']
json_string = json.dumps(data, sort_keys=True, indent=4)
print(json_string)
