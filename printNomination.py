# A file for printing the JSON file regarding nomination data.
import requests
import CONSTANTS
import json

response = requests.get(url=CONSTANTS.NOMINATION_URL, headers=CONSTANTS.header)
data = response.json()['results'][0]['votes']
json_string = json.dumps(data, sort_keys=True, indent=4)
print(json_string)
