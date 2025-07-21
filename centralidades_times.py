'''
    SOBRE ESTE ARQUIVO

    O objetivo desse arquivo e compilar algumas informações sobre as centralidades do grafo, e
    através disso propor uma análise desses dados
'''
# Import do networkx
import networkx as nx

# Import da função que usamos para construir o grafo, e instanciamento de um modelo
from grafo import montar_grafo
grafo = montar_grafo()

# Centralidades do grafo (cent_* = centralidade de *)
cent_vertices       = nx.degree_centrality(grafo)
cent_proximidade    = nx.closeness_centrality(grafo)
cent_intermediacao  = nx.betweenness_centrality(grafo)
cent_autovetor      = nx.eigenvector_centrality(grafo)

# Ordenamento dos valores encontrados
cent_vertices       = dict(sorted(nx.degree_centrality(grafo).items(), key=lambda item: item[1], reverse=True ))
cent_proximidade    = dict(sorted(nx.closeness_centrality(grafo).items(), key=lambda item: item[1], reverse=True ))
cent_intermediacao  = dict(sorted(nx.betweenness_centrality(grafo).items(), key=lambda item: item[1], reverse=True ))
cent_autovetor      = dict(sorted(nx.eigenvector_centrality(grafo).items(), key=lambda item: item[1], reverse=True ))

print('CENTRALIDADE: VÉRTICES')
for chave, valor in cent_vertices.items():
    print(f'{chave} : {valor}')

input('\nAPERTE [ENTER] PARA CONTINUAR...')

print('\nCENTRALIDADE: PROXIMIDADE (CLOSENESS)')
for chave, valor in cent_proximidade.items():
    print(f'{chave} : {valor}')

input('\nAPERTE [ENTER] PARA CONTINUAR...')

print('\nCENTRALIDADE: INTERMEDIAÇÃO (BETWEENNESS)')
for chave, valor in cent_intermediacao.items():
    print(f'{chave} : {valor}')

input('\nAPERTE [ENTER] PARA CONTINUAR...')

print('\nCENTRALIDADE: AUTOVETOR (EIGENVECTOR)')
for chave, valor in cent_autovetor.items():
    print(f'{chave} : {valor}')


'''
    OBSERVAÇÕES:

    Tivemos um problema na geração de dados sobre o 'pagerank' do gráfico, se possível (e/ou) necessário
    correr atrás de resolver, fora isso aparentemente tudo bem
'''