# This program reads json from internet to the consol
# Author: Hewa Orang

import requests

url =" https://www.gov.uk/bank-holidays.json" 
response = requests.get(url)
data = response.json()
print(data['northern-ireland']['events'][0])
