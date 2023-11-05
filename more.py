from datetime import datetime
import requests
import json

API_KEY = "dtktEwzWDFHVDWe2DMvSKhEpSBkWb7cgxHdAPLGG"


# Get the current date and time
current_datetime = datetime.utcnow()

# Format the current date and time as "YYYY-MM-DDT00:00:00Z"
formatted_datetime = current_datetime.strftime('%Y-%m-%dT00:00:00Z')

print("Formatted datetime:", formatted_datetime)

# hearing = requests.get('https://api.congress.gov/v3/bill/118/hr/423/actions', params={
#     "congress": '118', "billType": 'hr', "billNumber": '3672', "format": 'json', "api_key": API_KEY})

# data = hearing.json()
# json_string = json.dumps(data, sort_keys=True, indent=4)
# print(json_string)

re = requests.get('https://api.congress.gov/v3/nomination',
                  params={"congress": "118", "offset": '10', "format": 'json', "api_key": API_KEY})
data = re.json()
json_string = json.dumps(data, sort_keys=True, indent=4)
print(json_string)

# r = requests.get('https://api.congress.gov/v3/bill', params={
#     "format": 'json', "api_key": API})
# data = r.json()
# json_string = json.dumps(data, sort_keys=True, indent=4)
# print(json_string)

# hearing = requests.get('https://api.congress.gov/v3/bill/118/s/1409/text',
#                        params={"congress": '118', "format": 'Formatted Text', "api_key": API_KEY})
