import pandas as pd

_DATASETS = {
    'pib': 'https://raw.githubusercontent.com/rmcesarjr/iccd/main/data/ano-pib-pibpc-ipca.csv'
}

def dataload(nome):
    """
    Carrega um dataset padrão do ICCD.

    Parâmetros:
        nome (str): identificador do dataset (ex: 'inflacao').

    Retorna:
        pandas.DataFrame com os dados carregados.
    """
    if nome not in _DATASETS:
        raise ValueError(f"Dataset '{nome}' não encontrado. Disponíveis: {list(_DATASETS.keys())}")
    
    return pd.read_csv(_DATASETS[nome])
