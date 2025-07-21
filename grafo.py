'''
    SOBRE ESSE ARQUIVO

    O objetivo desse aquivo e armazenar a função que usaremos para gerar o grafo em outros arquivos, a 
    função montar_grafo() é essêncialmente idéntica ao bloco de código que plota o grafo em plotagem.ipynb,
    justamente para evitar dissonância entre as análises e conclusões referentes ao projeto.
'''

def montar_grafo():
    from dotenv import load_dotenv
    import os
    load_dotenv()

    # FETCH da API
    import requests
    response = requests.get(os.getenv('GET_TRANSFERENCIAS'))
    data = response.json()

    # Criação do grafo e plotagem dos dados
    import networkx as nx
    import matplotlib.pyplot as plt

    grafo = nx.DiGraph()

    if response.status_code == 200:
        conexoes_jogadores = {}

        for registro in data['transferências']:
            if registro['jogador'] not in conexoes_jogadores.keys():
                conexoes_jogadores[registro['jogador']] = []

            conexoes_jogadores[registro['jogador']].append(registro)
            grafo.add_edge(registro['de'], registro['para'], weight=1, transferencias=[], quantidade_transferencias=1) 

        for jogador, conexoes in  conexoes_jogadores.items():
            for conexao in conexoes:
                grafo[conexao['de']][conexao['para']]['transferencias'].append({
                        'data': conexao['data'],
                        'jogador': conexao['jogador'],
                        'valor': conexao['valor'],
                        'id': conexao['id']
                        })
                
                grafo[conexao['de']][conexao['para']]['quantidade_transferencias'] = len(grafo[conexao['de']][conexao['para']]['transferencias'])
    return grafo
    