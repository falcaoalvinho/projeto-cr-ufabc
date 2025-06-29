import requests

url = input('Insira a URL do repositório: ')
response = requests.get(url)
data = response.json()

repetidos = []
id_repetidos = []
jogadores = []

data_list = list(data['transferências'])

print('\nLISTA DE TIMES:')
for registro in data_list:
    print(f'{registro['jogador']}')

    if registro['jogador'] in jogadores:
        repetidos.append(registro['jogador'])
        id_repetidos.append(str(registro['id']))

    jogadores.append(registro['jogador'])

print('\nJOGADORES REPETIDOS: ')
print(', '.join(repetidos))

print('\nIDs DOS JOGADORES REPETIDOS')
print(', '.join(id_repetidos))

