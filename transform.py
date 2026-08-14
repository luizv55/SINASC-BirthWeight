import os
from dbfread import DBF
import pandas as pd
import pyreaddbc     # Pacote de leitura
import urllib.request    # Download

# Anos de dados
anos = [2020, 2021, 2022, 2023, 2024]


# Link ftp para download
nomes = []
for ano in anos:
    link = f"ftp://ftp.datasus.gov.br/dissemin/publicos/SINASC/1996_/Dados/DNRES/DNMG{ano}.dbc"
    nome = f'DNMG{ano}'
    nomes.append(nome)

    # Realiza o dowload e salva na pasta em formato .dbc
    urllib.request.urlretrieve(link, f'{nome}.dbc')

    # =============== Transforma o arquivo dbc para DF ===============
    pyreaddbc.dbc2dbf(f"{nome}.dbc", f"{nome}.dbf")  # Transforma arquivo .dbc para .dbf
    tabela = DBF(f"{nome}.dbf", encoding="iso-8859-1")  # Aplica encoding
    df = pd.DataFrame(iter(tabela))  # Transforma em dataframe

    # =============== Salva o df ===============
    df.to_csv(f"data/{nome}.csv", index=False)


# =============== Exclui arquivo .dbc e .dbf ===============
extensoes = ('.dbc', '.dbf')

for nome in nomes:
    for ext in extensoes:
        caminho = f'{nome}{ext}'
        if os.path.exists(caminho):
            os.remove(caminho)
            print(f'{caminho} apagado.')
        else:
            print(f'{caminho} não apagado.')