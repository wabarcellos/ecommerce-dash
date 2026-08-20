import pandas as pd
from dash import Dash
import dash_bootstrap_components as dbc

from layout import criar_layout
from callbacks import registrar_callbacks


def carregar_dados():
    """
    Carrega o arquivo CSV e realiza validações básicas.
    """

    try:
        df = pd.read_csv("ecommerce_estatistica.csv")

    except FileNotFoundError:
        raise FileNotFoundError(
            "O arquivo 'ecommerce_estatistica.csv' não foi encontrado. "
            "Verifique se ele está na mesma pasta do app.py."
        )

    except pd.errors.EmptyDataError:
        raise ValueError(
            "O arquivo 'ecommerce_estatistica.csv' está vazio."
        )

    except pd.errors.ParserError:
        raise ValueError(
            "Não foi possível interpretar o arquivo CSV. "
            "Verifique se o arquivo está corrompido."
        )

    except Exception as erro:
        raise RuntimeError(
            f"Erro inesperado ao carregar o arquivo CSV: {erro}"
        )

    # Colunas necessárias para os gráficos
    colunas_obrigatorias = [
        "Nota",
        "N_Avaliações",
        "Desconto",
        "Preço",
        "Qtd_Vendidos_Cod",
        "Marca_Freq",
        "Material_Freq",
        "Gênero"
    ]

    colunas_faltantes = [
        coluna
        for coluna in colunas_obrigatorias
        if coluna not in df.columns
    ]

    if colunas_faltantes:
        raise ValueError(
            "As seguintes colunas obrigatórias não foram encontradas "
            f"no arquivo: {colunas_faltantes}"
        )

    # Conversão das colunas numéricas
    colunas_numericas = [
        "Nota",
        "N_Avaliações",
        "Desconto",
        "Preço",
        "Qtd_Vendidos_Cod",
        "Marca_Freq",
        "Material_Freq"
    ]

    for coluna in colunas_numericas:
        df[coluna] = pd.to_numeric(
            df[coluna],
            errors="coerce"
        )

    # Remove registros sem dados essenciais
    df = df.dropna(
        subset=[
            "Nota",
            "N_Avaliações",
            "Desconto",
            "Preço",
            "Qtd_Vendidos_Cod",
            "Gênero"
        ]
    )

    return df


# Carrega os dados
df = carregar_dados()


# Criação da aplicação Dash
app = Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP
    ]
)

app.title = "E-commerce Dashboard"


# Layout
app.layout = criar_layout(df)


# Callbacks
registrar_callbacks(app, df)


if __name__ == "__main__":
    app.run(debug=True)
