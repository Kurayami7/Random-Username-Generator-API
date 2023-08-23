# Author: Areaf - 200531053

import requests

api_url = 'https://api.api-ninjas.com/v1/randomuser'
response = requests.get(api_url, headers={'X-Api-Key': 'ga7D1mQCQsBoU9ZaWKYcvA==XGIIDOxaYdVHHrjv'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)