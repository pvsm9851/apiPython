import requests
import pandas

#pip3 install requests
#pip3 install pandas


url_request='https://indian-cities-api-nocbegfhqg.now.sh/cities'

response = requests.get(url_request)
print(response)
pandas.read_json(response.text).to_csv('teste.csv')

#####Para pegar os dados que estão sendo salvos no csv#######
# data_csv = pandas.read_json(response.text).to_csv()

#arquivo sepomex.db.csv pode ser usado como massa do segundo exemplo

#NAO PRINTA RESPONSE.TEXT SENAO SUA MAQUINA VAI SAIR VOANDO PFVR






