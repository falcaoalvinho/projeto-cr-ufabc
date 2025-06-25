import requests

url = input('Insira a URL do repositório: ')

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(data)