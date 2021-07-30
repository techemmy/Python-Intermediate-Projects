import requests
import sys

url = 'https://api.exchangerate.host/convert'
response = requests.get(url, params={"from": sys.argv[1],
									 "to": sys.argv[2],
									 "amount": sys.argv[3]})
data = response.json()['result']
print(data)
