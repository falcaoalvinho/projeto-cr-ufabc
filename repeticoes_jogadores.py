'''
    SOBRE O ESTE ARQUIVO

    O objetivo deste arquivo é avaliar como e se existem registros de transferências diferentes, nos
    nomes de jogadores únicos, o que poderia apontar para repetições nos registros da API, quanto
    para jogadores que de fato protagonizaram multiplas transferências num mesmo periódo.
'''

# Carregamento do arquivo .env
from dotenv import load_dotenv
import os
load_dotenv()

# FETCH da API
import requests
response = requests.get(os.getenv('GET_TRANSFERENCIAS'))
data = response.json()

# Variáveis do código
jogadores= []
repetidos = []
id_repetidos = []
repeticoes_jogadores = {}

# Dados da API convertidos de JSON para Lista (OBS: apenas os dados da folha trasnferências)
data_list = list(data['transferências'])

for registro in data_list:
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

print('\nJOGADORES COM MAIS DE UM REGISTRO E A QUANTIDADE DE REGISTROS NOS SEUS NOMES: ')
for jogador, repeticoes in repeticoes_jogadores.items():
    if repeticoes > 1:
        print(f'{jogador}: {repeticoes}')

'''
    SOBRE OS JOGADORES QUE APARECEM EM MAIS DE UM REGISTRO DE TRANSFERÊNCIA

    Durante nossas análises, percebemos que alguns dos jogadores apareciam em mais de um registro de trasferência,
    após uma minuciosa análise concluimos que existe um padrão neste tipo de caso dado a dinâmica dos ciclos de
    temporadas entre as ligas. Sabendo que as transferências normalmente só ocorrem em periódos especificos que variam
    em diferentes regiões, é que essa forma de relação entre instituições e atletas se dá por intermédio de contratos,
    o que em teoria dificulta a realização desse tipo de cenário. Observamos que existe uma excessão, que permite que os
    jogadores sejam vinculados a outros times sem quebrar seus contratos, essa exceção se dá na forma de empréstimos, que 
    em uma parte considerável dos casos de registros duplos no nomes de diferentes jogadores, poderia estar diretamente 
    vinculada a um periódo de experimentação dos clubes que recebem este empréstimo, uma vez que na maior parte dos casos,
    os jogadores acabam sendo transferidos para os clubes em que foram emprestados. Apesar de não ser uma verdade absoluta,
    podemos de maneira categorica afirmar de maneira categorica que este padrão, apesar de não ser o único, é uma forte
    tendência entre esses casos.
'''