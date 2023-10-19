#pip install requests
import requests

retorno = requests.get("http://127.0.0.1:8000")

print(retorno.text) #{"mensagem":"home"} -> string

print(retorno.json()) #{'mensagem': 'home'} -> json /dict

print(retorno.json()['mensagem']) #home
