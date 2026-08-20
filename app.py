import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# ============================================================
# 1. LEITURA DOS DADOS
# ============================================================

df = pd.read_csv('ecommerce_estatistica.csv')
df = df.dropna()

# ============================================================
# 2. CRIAÇÃO DOS GRÁFICOS
# ============================================================

# ------------------------------------------------------------
# Histograma - Distribuição das notas
# ------------------------------------------------------------

fig_histograma = px.histogram(
    df,
    x='Nota',
    nbins=10,
    title='Distribuição das Notas dos Produtos',
    labels={
        'Nota': 'Nota',
        'count': 'Quantidade de Produtos'
    }
)

fig_histograma.update_layout(
    template='plotly_white'
)


# ------------------------------------------------------------
# Dispersão - Avaliações x Quantidade Vendida
# ------------------------------------------------------------

fig_dispersao = px.scatter(
    df,
    x='N_Avaliações',
    y='Qtd_Vendidos_Cod',
    title='Número de Avaliações x Quantidade Vendida',
    labels={
        'N_Avaliações': 'Número de Avaliações',
        'Qtd_Vendidos_Cod': 'Quantidade Vendida'
    }
)

fig_dispersao.update_layout(
    template='plotly_white'
)


# ------------------------------------------------------------
# Mapa de calor - Correlação
# ------------------------------------------------------------

variaveis = [
    'Nota',
    'N_Avaliações',
    'Desconto',
    'Preço',
    'Qtd_Vendidos_Cod',
    'Marca_Freq',
    'Material_Freq'
]

matriz_corr = df[variaveis].corr()

fig_heatmap = px.imshow(
    matriz_corr,
    text_auto='.2f',
    color_continuous_scale='RdBu_r',
    title='Mapa de Calor das Correlações'
)

fig_heatmap.update_layout(
    template='plotly_white'
)


# ------------------------------------------------------------
# Gráfico de barras - Vendas por gênero
# ------------------------------------------------------------

vendas_genero = (
    df.groupby('Gênero')['Qtd_Vendidos_Cod']
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

fig_barras = px.bar(
    vendas_genero,
    x='Gênero',
    y='Qtd_Vendidos_Cod',
    title='Quantidade Média Vendida por Gênero',
    labels={
        'Gênero': 'Gênero',
        'Qtd_Vendidos_Cod': 'Quantidade Média Vendida'
    }
)

fig_barras.update_layout(
    template='plotly_white'
)


# ------------------------------------------------------------
# Gráfico de pizza - Distribuição por gênero
# ------------------------------------------------------------

contagem_genero = (
    df['Gênero']
    .value_counts()
    .reset_index()
)

contagem_genero.columns = ['Gênero', 'Quantidade']

fig_pizza = px.pie(
    contagem_genero,
    names='Gênero',
    values='Quantidade',
    title='Distribuição dos Produtos por Gênero'
)

fig_pizza.update_layout(
    template='plotly_white'
)


# ------------------------------------------------------------
# Gráfico de densidade - Preços
# ------------------------------------------------------------

fig_densidade = px.histogram(
    df,
    x='Preço',
    nbins=30,
    histnorm='probability density',
    title='Distribuição de Densidade dos Preços',
    labels={
        'Preço': 'Preço'
    }
)

fig_densidade.update_layout(
    template='plotly_white'
)


# ------------------------------------------------------------
# Gráfico de regressão
# ------------------------------------------------------------

fig_regressao = px.scatter(
    df,
    x='N_Avaliações',
    y='Qtd_Vendidos_Cod',
    trendline='ols',
    title='Regressão Linear: Avaliações x Quantidade Vendida',
    labels={
        'N_Avaliações': 'Número de Avaliações',
        'Qtd_Vendidos_Cod': 'Quantidade Vendida'
    }
)

fig_regressao.update_layout(
    template='plotly_white'
)


# ============================================================
# 3. CRIAÇÃO DA APLICAÇÃO DASH
# ============================================================

app = Dash(__name__)

app.layout = html.Div(
    children=[

        html.H1(
            'Dashboard de Análise de E-commerce',
            style={
                'textAlign': 'center'
            }
        ),

        html.P(
            'Visualização interativa dos principais indicadores '
            'e relações encontradas nos dados de e-commerce.',
            style={
                'textAlign': 'center'
            }
        ),

        html.H2('Distribuição das Notas'),

        dcc.Graph(
            id='grafico-histograma',
            figure=fig_histograma
        ),

        html.H2('Avaliações x Quantidade Vendida'),

        dcc.Graph(
            id='grafico-dispersao',
            figure=fig_dispersao
        ),

        html.H2('Correlação entre as Variáveis'),

        dcc.Graph(
            id='grafico-heatmap',
            figure=fig_heatmap
        ),

        html.H2('Quantidade Média Vendida por Gênero'),

        dcc.Graph(
            id='grafico-barras',
            figure=fig_barras
        ),

        html.H2('Distribuição dos Produtos por Gênero'),

        dcc.Graph(
            id='grafico-pizza',
            figure=fig_pizza
        ),

        html.H2('Distribuição dos Preços'),

        dcc.Graph(
            id='grafico-densidade',
            figure=fig_densidade
        ),

        html.H2('Regressão Linear'),

        dcc.Graph(
            id='grafico-regressao',
            figure=fig_regressao
        )
    ],

    style={
        'maxWidth': '1200px',
        'margin': 'auto',
        'padding': '20px'
    }
)


# ============================================================
# 4. EXECUÇÃO DA APLICAÇÃO
# ============================================================

if __name__ == '__main__':
    app.run(debug=True)