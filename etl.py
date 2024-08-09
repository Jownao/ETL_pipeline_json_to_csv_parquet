import pandas as pd
import os
import glob
from utils_log import log_decorator

# Função extract que lê e consolida os JSON
@log_decorator
def extrair_dados(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_concat = pd.concat(df_list, ignore_index=True)
    return df_concat

# Função que transforma
@log_decorator
def calcular_kpi_total_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

# Carrega em CSV ou Parquet
@log_decorator
def carregar_dados(df: pd.DataFrame, formato_saida: list):
    if 'csv' in formato_saida:
        df.to_csv("dados.csv", index=False)
    if 'parquet' in formato_saida:
        df.to_parquet("dados.parquet")

# Pipeline final
@log_decorator
def pipeline_calculo_final(path: str, formato: list):
    pasta = path
    dataframe = extrair_dados(pasta)
    dataframe_total = calcular_kpi_total_vendas(dataframe)
    carregar_dados(dataframe_total, formato)
