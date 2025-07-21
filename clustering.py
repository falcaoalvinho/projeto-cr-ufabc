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

print(f'\nCLUSTERING MÉDIO: {nx.average_clustering(grafo)}')

input(f'\nAPERTE [ENTER] PARA CONTINUAR...')
os.system('cls')

input(f'EXECUÇÃO CONCLUIDA COM SUCESSO, APERTE [ENTER] PARA ENCERRAR...')