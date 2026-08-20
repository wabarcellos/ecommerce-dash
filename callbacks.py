import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from dash import Input, Output


# =========================================================
# FUNÇÕES AUXILIARES
# =========================================================

def figura_vazia(titulo, mensagem):
    """
    Cria uma figura vazia para situações em que não
    existem dados suficientes para gerar o gráfico.
    """

    fig = go.Figure()

    fig.update_layout(
        title=titulo,
        xaxis={
            "visible": False
        },
        yaxis={
            "visible": False
        },
        annotations=[
            {
                "text": mensagem,
                "xref": "paper",
                "yref": "paper",
                "x": 0.5,
                "y": 0.5,
                "showarrow": False
            }
        ]
    )

    return fig


# =========================================================
# 1. HISTOGRAMA
# =========================================================

def criar_histograma(df):

    fig = px.histogram(
        df,
        x="Nota",
        nbins=10,
        title="Distribuição das Notas dos Produtos"
    )

    fig.update_layout(
        xaxis_title="Nota",
        yaxis_title="Quantidade de Produtos",
        template="plotly_white"
    )

    return fig


# =========================================================
# 2. GRÁFICO DE DISPERSÃO
# =========================================================

def criar_dispersao(df):

    fig = px.scatter(
        df,
        x="N_Avaliações",
        y="Qtd_Vendidos_Cod",
        title=(
            "Relação entre Número de Avaliações "
            "e Quantidade Vendida"
        ),
        opacity=0.7
    )

    fig.update_layout(
        xaxis_title="Número de Avaliações",
        yaxis_title="Quantidade Vendida",
        template="plotly_white"
    )

    return fig


# =========================================================
# 3. MAPA DE CALOR
# =========================================================

def criar_heatmap(df):

    variaveis = [
        "Nota",
        "N_Avaliações",
        "Desconto",
        "Preço",
        "Qtd_Vendidos_Cod",
        "Marca_Freq",
        "Material_Freq"
    ]

    dados_corr = df[variaveis].dropna()

    # Verifica se existem dados suficientes
    if len(dados_corr) < 2:
        return figura_vazia(
            "Mapa de Calor das Correlações",
            "Dados insuficientes para calcular as correlações."
        )

    matriz_corr = dados_corr.corr()

    fig = go.Figure(
        data=go.Heatmap(
            z=matriz_corr.values,
            x=matriz_corr.columns,
            y=matriz_corr.index,
            zmin=-1,
            zmax=1,
            text=np.round(
                matriz_corr.values,
                2
            ),
            texttemplate="%{text}",
            colorscale="RdBu",
            reversescale=True,
            colorbar={
                "title": "Correlação"
            }
        )
    )

    fig.update_layout(
        title="Mapa de Calor das Correlações entre Variáveis",
        template="plotly_white"
    )

    return fig


# =========================================================
# 4. GRÁFICO DE BARRAS
# =========================================================

def criar_barras(df):

    vendas_genero = (
        df.groupby("Gênero", as_index=False)[
            "Qtd_Vendidos_Cod"
        ]
        .mean()
        .sort_values(
            "Qtd_Vendidos_Cod",
            ascending=False
        )
    )

    fig = px.bar(
        vendas_genero,
        x="Gênero",
        y="Qtd_Vendidos_Cod",
        title="Quantidade Média Vendida por Gênero"
    )

    fig.update_layout(
        xaxis_title="Gênero",
        yaxis_title="Quantidade Média Vendida",
        template="plotly_white",
        xaxis_tickangle=-30
    )

    return fig


# =========================================================
# 5. GRÁFICO DE PIZZA
# =========================================================

def criar_pizza(df):

    contagem_genero = (
        df["Gênero"]
        .value_counts()
        .reset_index()
    )

    contagem_genero.columns = [
        "Gênero",
        "Quantidade"
    ]

    fig = px.pie(
        contagem_genero,
        names="Gênero",
        values="Quantidade",
        title="Distribuição dos Produtos por Gênero"
    )

    fig.update_layout(
        template="plotly_white"
    )

    return fig


# =========================================================
# 6. GRÁFICO DE DENSIDADE
# =========================================================

def criar_densidade(df):

    dados = (
        df["Preço"]
        .dropna()
        .astype(float)
        .values
    )

    # Precisamos de pelo menos dois valores diferentes
    if len(dados) < 2 or np.ptp(dados) == 0:

        return figura_vazia(
            "Distribuição de Densidade dos Preços",
            "Dados insuficientes para calcular a densidade."
        )

    try:

        # Implementação de KDE usando numpy
        media = np.mean(dados)
        desvio = np.std(dados, ddof=1)

        # Regra de Silverman
        largura = (
            1.06
            * desvio
            * len(dados) ** (-1 / 5)
        )

        # Evita largura igual a zero
        if largura <= 0:
            largura = 1.0

        x = np.linspace(
            dados.min(),
            dados.max(),
            300
        )

        # Matriz para cálculo da densidade
        diferencas = (
            x[:, None] - dados[None, :]
        )

        densidade = (
            np.exp(
                -0.5
                * (
                    diferencas / largura
                ) ** 2
            )
            / (
                largura
                * np.sqrt(2 * np.pi)
            )
        ).mean(axis=1)

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=x,
                y=densidade,
                mode="lines",
                fill="tozeroy",
                name="Densidade"
            )
        )

        fig.update_layout(
            title="Distribuição de Densidade dos Preços",
            xaxis_title="Preço",
            yaxis_title="Densidade",
            template="plotly_white"
        )

        return fig

    except Exception:

        return figura_vazia(
            "Distribuição de Densidade dos Preços",
            "Não foi possível calcular a densidade."
        )


# =========================================================
# 7. GRÁFICO DE REGRESSÃO
# =========================================================

def criar_regressao(df):

    dados = df[
        [
            "N_Avaliações",
            "Qtd_Vendidos_Cod"
        ]
    ].dropna()

    # É necessário ter pelo menos dois pontos
    if len(dados) < 2:

        return figura_vazia(
            "Regressão Linear",
            "Dados insuficientes para calcular a regressão."
        )

    x = dados["N_Avaliações"].values
    y = dados["Qtd_Vendidos_Cod"].values

    # Verifica se x possui variação
    if np.ptp(x) == 0:

        return figura_vazia(
            "Regressão Linear",
            "Não é possível calcular a regressão."
        )

    # Calcula a regressão linear
    coeficiente_angular, intercepto = np.polyfit(
        x,
        y,
        1
    )

    x_linha = np.linspace(
        x.min(),
        x.max(),
        100
    )

    y_linha = (
        coeficiente_angular
        * x_linha
        + intercepto
    )

    fig = go.Figure()

    # Pontos
    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="markers",
            name="Produtos",
            opacity=0.6
        )
    )

    # Linha de regressão
    fig.add_trace(
        go.Scatter(
            x=x_linha,
            y=y_linha,
            mode="lines",
            name="Regressão Linear"
        )
    )

    fig.update_layout(
        title=(
            "Regressão Linear: Número de Avaliações "
            "x Quantidade Vendida"
        ),
        xaxis_title="Número de Avaliações",
        yaxis_title="Quantidade Vendida",
        template="plotly_white"
    )

    return fig


# =========================================================
# CRIAÇÃO DOS 7 GRÁFICOS
# =========================================================

def criar_graficos(df):

    return (
        criar_histograma(df),
        criar_dispersao(df),
        criar_heatmap(df),
        criar_barras(df),
        criar_pizza(df),
        criar_densidade(df),
        criar_regressao(df)
    )


# =========================================================
# CALLBACK
# =========================================================

def registrar_callbacks(app, df):

    @app.callback(
        [
            Output(
                "grafico-histograma",
                "figure"
            ),

            Output(
                "grafico-dispersao",
                "figure"
            ),

            Output(
                "grafico-heatmap",
                "figure"
            ),

            Output(
                "grafico-barras",
                "figure"
            ),

            Output(
                "grafico-pizza",
                "figure"
            ),

            Output(
                "grafico-densidade",
                "figure"
            ),

            Output(
                "grafico-regressao",
                "figure"
            )
        ],

        Input(
            "dropdown-genero",
            "value"
        )
    )

    def atualizar_graficos(
        genero_selecionado
    ):

        # =====================================================
        # FILTRO
        # =====================================================

        if (
            genero_selecionado is None
            or genero_selecionado == "Todos"
        ):

            df_filtrado = df.copy()

        else:

            df_filtrado = df[
                df["Gênero"]
                == genero_selecionado
            ].copy()

        # =====================================================
        # ATUALIZA OS 7 GRÁFICOS
        # =====================================================

        return criar_graficos(
            df_filtrado
        )