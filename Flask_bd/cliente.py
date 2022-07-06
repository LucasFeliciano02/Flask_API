"""
Fazer requisição
"""

import requests


# data = {'username':'Carlos', 'secret':'@dmin456' ,'info':'cargo', 'value':'analista'}
# data = {'username':'Carlos', 'secret':'@dmin456' ,'cargo':'Engenheiro', 'nome':'Reynaldo', 'salario': '5000'}

# response = requests.post("http://0.0.0.0:5000/register", data=data)
# response = requests.post("http://0.0.0.0:5000/:5000/informations", data=data)

# response = requests.get("http://127.0.0.1:5000/:5000/empregados/cargo/analista")
# response = requests.get('http://0.0.0.0:5000/empregados/salario/4000')
response = requests.get('http://0.0.0.0:5000/empregados')


if response.status_code == 200:
    message = response.json()
    print(message['empregados'])
else:
    print(response.status_code)

