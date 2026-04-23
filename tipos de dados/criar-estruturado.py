# dados estruturados
# criacao de arquivos estruturados

#pip install pandas
#pip install openpyxl

from csv import writer

import pandas as pd

#estrutura de dicionario
dados_planilha = {
    'nome': ['João', 'Maria', 'Pedro', 'Ana', 'Carlos'],
    'idade': [25, 30, 22, 28, 35],
    'cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília', 'Salvador']
}

#criacao do dataframe
df_planilha = pd.DataFrame(dados_planilha)

print(df_planilha)

#criacao do arquivo excel
with pd.ExcelWriter('dados_estruturados.xlsx') as writer: #criando o arquivo e definindo o nome do arquivo
    df_planilha.to_excel(writer, index=False, sheet_name='planilha de dados estruturados') #escrevendo o dataframe no arquivo excel, index=False para nao incluir o indice, sheet_name para definir o nome da aba



