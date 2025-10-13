# This program prints out the bank holiddays that happen in Northen Ireland
# Author: Hewa Orang

import requests

url =" https://www.gov.uk/bank-holidays.json" 
response = requests.get(url)
data = response.json()
print (data)

for event in data['northern-ireland']['events']:
    print(f"{event['title']} on {event['date']}")

