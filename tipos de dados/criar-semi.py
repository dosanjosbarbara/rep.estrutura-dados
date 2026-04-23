#importando a biblioteca pandas para criar um DataFrame
import pandas as pd

#nome do meu dicionario
dados_json = { #estrutura de dicionario
    'nome': ['João', 'Maria', 'Pedro', 'Ana', 'Carlos'],
    'idade': [25, 30, 22, 28, 35],
    'cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília', 'Salvador']
}

df_json = pd.DataFrame(dados_json) #criacao do dataframe a partir do dicionario

#exportando o dataframe para um arquivo json
df_json.to_json('dados_semi_estruturados.json', orient='records', lines=True) #exportando o dataframe para um arquivo json, orient='records' para criar um array de objetos, lines=True para escrever cada objeto em uma linha


