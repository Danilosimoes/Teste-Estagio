import json
import requests

'''
requets -> json
json - dicionario
trabalhar os dados -> dicionario final
dicionario final -> csv
   '''

r = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados/')
estados_list = r.json()

estados_str = json.dumps(estados_list, indent=2)

print(estados_str)


