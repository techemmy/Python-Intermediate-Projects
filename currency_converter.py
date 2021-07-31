import requests
import sys

url = 'https://api.exchangerate.host/convert'
if len(sys.argv) < 3:
    print("How to run code:")
    print("python currency_converter.py from_amount to_amount amount")
else:
    response = requests.get(url, params={"from": sys.argv[1],
									 "to": sys.argv[2],
									 "amount": sys.argv[3]})
    data = response.json()['result']
    print(data)
