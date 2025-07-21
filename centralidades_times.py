'''
    SOBRE ESTE ARQUIVO

    O objetivo desse arquivo e compilar algumas informações sobre as centralidades do grafo, e
    através disso propor uma análise desses dados
'''
# Import do networkx
import networkx as nx
import os

# Import da função que usamos para construir o grafo, e instanciamento de um modelo
from grafo import montar_grafo
grafo = montar_grafo()

# Centralidades do grafo (cent_* = centralidade de *)
cent_vertices       = nx.degree_centrality(grafo)
cent_proximidade    = nx.closeness_centrality(grafo)
cent_intermediacao  = nx.betweenness_centrality(grafo)
cent_autovetor      = nx.eigenvector_centrality(grafo)
cent_out_dregree    = nx.out_degree_centrality(grafo)
cent_in_dregree     = nx.in_degree_centrality(grafo)

# Ordenamento dos valores encontrados
cent_vertices       = dict(sorted(cent_vertices.items(), key=lambda item: item[1], reverse=True ))
cent_proximidade    = dict(sorted(cent_proximidade.items(), key=lambda item: item[1], reverse=True ))
cent_intermediacao  = dict(sorted(cent_intermediacao.items(), key=lambda item: item[1], reverse=True ))
cent_autovetor      = dict(sorted(cent_autovetor.items(), key=lambda item: item[1], reverse=True ))
cent_out_dregree    = dict(sorted(cent_out_dregree.items(), key=lambda item: item[1], reverse=True))
cent_in_dregree     = dict(sorted(cent_in_dregree.items(), key=lambda item: item[1], reverse=True))

# Print dos valores para cada um dos casos usando loops de chave, valor
print('\nCENTRALIDADE: VÉRTICES (NODE)')
for chave, valor in cent_vertices.items():
    print(f'{chave} : {valor}')

input('\nAPERTE [ENTER] PARA CONTINUAR...')
os.system('cls')

print('\nCENTRALIDADE: PROXIMIDADE (CLOSENESS)')
for chave, valor in cent_proximidade.items():
    print(f'{chave} : {valor}')

input('\nAPERTE [ENTER] PARA CONTINUAR...')
os.system('cls')

print('\nCENTRALIDADE: INTERMEDIAÇÃO (BETWEENNESS)')
for chave, valor in cent_intermediacao.items():
    print(f'{chave} : {valor}')

input('\nAPERTE [ENTER] PARA CONTINUAR...')
os.system('cls')

print('\nCENTRALIDADE: AUTOVETOR (EIGENVECTOR)')
for chave, valor in cent_autovetor.items():
    print(f'{chave} : {valor}')

input('\nAPERTE [ENTER] PARA CONTINUAR...')
os.system('cls')

print('\nCENTRALIDADE: GRAU DE SAÍDA (OUT DEGREE)')
for chave, valor in cent_autovetor.items():
    print(f'{chave} : {valor}')

input('\nAPERTE [ENTER] PARA CONTINUAR...')
os.system('cls')

print('\nCENTRALIDADE: GRAU DE ENTRADA (IN DEGREE)')
for chave, valor in cent_autovetor.items():
    print(f'{chave} : {valor}')

input('\nEXECUÇÃO FINALIZADA COM SUSCESSO, APETE [ENTER] PARA ENCERRAR...')
os.system('cls')

'''
    OBSERVAÇÕES:

    Tivemos um problema na geração de dados sobre o 'pagerank' do gráfico, se possível (e/ou) necessário
    correr atrás de resolver, fora isso aparentemente tudo bem
'''

'''
    ANÁLISE PRELIMINAR DOS DADOS DE CENTRALIDADE

    Observamos fortes tendências entre alguns clubes, que de maneira consistente aparecem nas posições mais elevadas dos
    rankings de centralidade, como por exemplo o Chelsea, entretanto também percebemos que diferentemente do que imaginavamos,
    não se pode afirmar de maneira concisa a existência de uma hegemonia europeia. Para além disso percebemos que por mais
    que seja possível aferir a existência de 'protagonistas', não necesseriamente os times mais relevantes na midia,
    são os times mais relevantes dentro da lógica do mercado de atletas.
'''