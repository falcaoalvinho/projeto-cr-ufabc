import requests

url = input('Insira a URL do repositório: ')
response = requests.get(url)
data = response.json()

jogadores= []

repetidos = []
id_repetidos = []

repeticoes_jogadores = {}

data_list = list(data['transferências'])



print('\nLISTA DE TIMES:')
for registro in data_list:
    # print(f'{registro['jogador']}')

    if registro['jogador'] in jogadores:
        repetidos.append(registro['jogador'])
        id_repetidos.append(str(registro['id']))

    jogadores.append(registro['jogador'])

set(jogadores)
set(repetidos)
set(id_repetidos)
list((jogadores, repetidos, id_repetidos))

for jogador in jogadores:
    repeticoes_jogadores[str(jogador)] = jogadores.count(jogador)

# print('\nJOGADORES REPETIDOS: ')
# print(', '.join(repetidos))

# print('\nIDs DOS JOGADORES REPETIDOS')
# print(', '.join(id_repetidos))

print('\nREPETIÇÕES DE CADA JOGADOR: ')
for jogador, repeticoes in repeticoes_jogadores.items():
    if repeticoes > 1:
        print(f'{jogador}: {repeticoes}')
