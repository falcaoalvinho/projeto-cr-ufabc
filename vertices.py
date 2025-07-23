'''
    SOBRE ESTE ARQUIVO

    Este arquivo tem como objetivo analisar os dados de cada um dos vértices do grau
    de maneira individualizada, para além de algums dados globais do grafo
'''

# Imports do arquivo
import networkx as nx
import os

# Import da e instância do grafo
from grafo import montar_grafo
grafo = montar_grafo()

print(f'TOTAL DE ARESTAS: {grafo.number_of_edges}')
print(f'TOTAL DE VÉRTICES: {grafo.number_of_nodes}')

input('EXECUÇÃO CONCLUIDA COM SUCESSO, APERTE [ENTER] PARA ENCERRAR...')