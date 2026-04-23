#importar pandas para leitura de dados
import pandas as pd

#leitura do arquivo excel criado anteriormente
df_excel = pd.read_excel('C:\\Users\\48522445885\\Documents\\python petchuna\\estrutura de dados\\tipos de dados\\dados_estruturados.xlsx') #df_excel para armazenar o dataframe lido do arquivo excel, pd.read_excel para ler o arquivo excel, caminho do arquivo excel entre aspas, use duas barras invertidas para separar as pastas no caminho do arquivo

print(df_excel)