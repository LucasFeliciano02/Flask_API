"""
Fazer requisição
"""

import requests


data = {'username':'Carlos', 'secret':'@dmin456' ,'info':'cargo', 'value':'desenvolvedor'}
 
# response = requests.get("http://127.0.0.1:5000/:5000/empregados/cargo/analista")
response = requests.post("http://127.0.0.1:5000/:5000/informations", data=data)

if response.status_code == 200:
    message = response.json()
    print(message['empregados'])
else:
    print(response.status_code)

