'''
    SOBRE ESTE ARQUIVO

    O arquivo tem como objeto, coletar dados de nosso grafo direcional, e usando essas informações
    gerar dados referentes a clusterização do do grafo
'''

# Imports do arquivo
import networkx as nx
import os

# Import da e instância do grafo
from grafo import montar_grafo
grafo = montar_grafo()

# Cálculo e organização dos dados de clustering
clustering = nx.clustering(grafo, grafo.nodes)
clustering = dict(sorted(clustering.items(), key=lambda item: item[1], reverse=True))

# Impressão dos dados
print('CLUSTERING DOS VÉRTICES DO GRAFO')
for chave, valor in clustering.items():
    print(f'    {chave} : {valor}')

print(f'\nCLUSTERING MÉDIO: {nx.average_clustering(grafo)}')

input('EXECUÇÃO CONCLUIDA COM SUCESSO, APERTE [ENTER] PARA ENCERRAR...')
os.system('cls')
