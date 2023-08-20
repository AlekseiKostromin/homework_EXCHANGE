import requests

url = "https://api.apilayer.com/exchangerates_data/latest?symbols={symbols}&base={base}"

payload = {}
headers= {
  "apikey": "AIhlWtVlORMtBwO1JwhixuKk2wsNnWQK"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text


