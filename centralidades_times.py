'''
    SOBRE ESTE ARQUIVO

    O objetivo desse arquivo e compilar algumas informações sobre as centralidades do grafo, e
    através disso propor uma análise desses dados
'''
# Import do networkx
import networkx as nx
import os

# Import da função que usamos para construir o grafo, e instância
from grafo import montar_grafo
grafo = montar_grafo()

# Centralidades do grafo (cent_* = centralidade de *)
cent_vertices       = nx.degree_centrality(grafo)
cent_proximidade    = nx.closeness_centrality(grafo)
cent_intermediacao  = nx.betweenness_centrality(grafo)
cent_autovetor      = nx.eigenvector_centrality(grafo)
cent_out_dregree    = nx.out_degree_centrality(grafo)
cent_in_dregree     = nx.in_degree_centrality(grafo)

# Pagerank dos clubes
pagerank = nx.pagerank(grafo)

# Ordenamento dos valores encontrados
cent_vertices       = dict(sorted(cent_vertices.items(), key=lambda item: item[1], reverse=True ))
cent_proximidade    = dict(sorted(cent_proximidade.items(), key=lambda item: item[1], reverse=True ))
cent_intermediacao  = dict(sorted(cent_intermediacao.items(), key=lambda item: item[1], reverse=True ))
cent_autovetor      = dict(sorted(cent_autovetor.items(), key=lambda item: item[1], reverse=True ))
cent_out_dregree    = dict(sorted(cent_out_dregree.items(), key=lambda item: item[1], reverse=True))
cent_in_dregree     = dict(sorted(cent_in_dregree.items(), key=lambda item: item[1], reverse=True))
pagerank            = dict(sorted(pagerank.items(), key=lambda item: item[1], reverse=True))

# Impressão dos dados
print('\nCENTRALIDADE: VÉRTICES (NODES)')
for chave, valor in cent_vertices.items():
    print(f'    {chave} : {valor}')
print('FINAL DA LISTA PARA VÉRTICES (NODES)')

input('\nAPERTE [ENTER] PARA CONTINUAR...')
os.system('cls')

print('\nCENTRALIDADE: PROXIMIDADE (CLOSENESS)')
for chave, valor in cent_proximidade.items():
    print(f'    {chave} : {valor}')
print('FINAL DA LISTA PARA PROXIMIDADE (CLOSENESS)')

input('\nAPERTE [ENTER] PARA CONTINUAR...')
os.system('cls')

print('\nCENTRALIDADE: INTERMEDIAÇÃO (BETWEENNESS)')
for chave, valor in cent_intermediacao.items():
    print(f'    {chave} : {valor}')
print('FINAL DA LISTA PARA INTERMEDIAÇÃO (BETWEENNESS)')

input('\nAPERTE [ENTER] PARA CONTINUAR...')
os.system('cls')

print('\nCENTRALIDADE: AUTOVETOR (EIGENVECTOR)')
for chave, valor in cent_autovetor.items():
    print(f'    {chave} : {valor}')
print('FINAL DA LISTA PARA AUTOVETOR (EIGENVECTOR)')

input('\nAPERTE [ENTER] PARA CONTINUAR...')
os.system('cls')

print('\nCENTRALIDADE: GRAU DE SAÍDA (OUT DEGREE)')
for chave, valor in cent_autovetor.items():
    print(f'    {chave} : {valor}')
print('FINAL DA LISTA PARA GRAU DE SAÍDA (OUT DEGREE)')

input('\nAPERTE [ENTER] PARA CONTINUAR...')
os.system('cls')

print('\nCENTRALIDADE: GRAU DE ENTRADA (IN DEGREE)')
for chave, valor in cent_autovetor.items():
    print(f'    {chave} : {valor}')
print('FINAL DA LISTA PARA GRAU DE ENTRADA (IN DEGREE)')

input('\nAPERTE [ENTER] PARA CONTINUAR...')
os.system('cls')

print('\nPAGERANK DOS CLUBES:')
for chave, valor in pagerank.items():
    print(f'    {chave} : {valor}')
print('FINAL DA LISTA PARA PAGERANK')

input('\nEXECUÇÃO FINALIZADA COM SUSCESSO, APERTE [ENTER] PARA ENCERRAR...')

'''
    ANÁLISE PRELIMINAR DOS DADOS DE CENTRALIDADE

    Observamos fortes tendências entre alguns clubes, que de maneira consistente aparecem nas posições mais elevadas dos
    rankings de centralidade, como por exemplo o Chelsea, entretanto também percebemos que diferentemente do que imaginavamos,
    não se pode afirmar de maneira concisa a existência de uma hegemonia europeia. Para além disso percebemos que por mais
    que seja possível aferir a existência de 'protagonistas', não necesseriamente os times mais relevantes na midia,
    são os times mais relevantes dentro da lógica do mercado de atletas.
'''