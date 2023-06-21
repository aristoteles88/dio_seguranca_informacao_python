import re
import json
from urllib.request import urlopen

url = "https://ipinfo.io/json"

resp = urlopen(url, cafile=False)

data = json.load(resp)

ip = data['ip']
org = data['org']
city = data['city']
country = data['country']
region = data['region']

print("Detalhes do IP externo")
print(
    f'''
        IP: {ip}\n
        Regiao: {region}\n
        Pais: {country}\n
        Cidade: {city}\n
        Organização: {org}\n
    '''
)