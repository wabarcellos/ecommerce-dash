from dash import dcc, html
import dash_bootstrap_components as dbc


def criar_layout(df):

    # Lista de gêneros existentes no DataFrame
    generos = sorted(
        df["Gênero"]
        .dropna()
        .unique()
        .tolist()
    )

    # Adiciona a opção "Todos" no início
    opcoes_genero = [
        {
            "label": "Todos",
            "value": "Todos"
        }
    ]

    opcoes_genero.extend(
        [
            {
                "label": genero,
                "value": genero
            }
            for genero in generos
        ]
    )

    return dbc.Container(
        [

            # =========================================================
            # CABEÇALHO
            # =========================================================

            dbc.Row(
                dbc.Col(
                    [
                        html.H1(
                            "Dashboard de E-commerce",
                            className="text-center mt-4 mb-2"
                        ),

                        html.P(
                            "Explore os dados de vendas e utilize o filtro "
                            "por gênero para analisar os resultados.",
                            className="text-center text-muted mb-4"
                        )
                    ],
                    width=12
                )
            ),

            # =========================================================
            # FILTRO
            # =========================================================

            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [

                                html.Label(
                                    "Selecione um gênero:",
                                    className="fw-bold mb-2"
                                ),

                                dcc.Dropdown(
                                    id="dropdown-genero",
                                    options=opcoes_genero,
                                    value="Todos",
                                    clearable=False,
                                    searchable=True
                                )

                            ]
                        ),
                        className="mb-4"
                    ),
                    width=12
                )
            ),

            # =========================================================
            # LINHA 1 - HISTOGRAMA + DISPERSÃO
            # =========================================================

            dbc.Row(
                [

                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                dcc.Loading(
                                    dcc.Graph(
                                        id="grafico-histograma"
                                    )
                                )
                            ),
                            className="mb-4"
                        ),
                        width=12,
                        lg=6
                    ),

                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                dcc.Loading(
                                    dcc.Graph(
                                        id="grafico-dispersao"
                                    )
                                )
                            ),
                            className="mb-4"
                        ),
                        width=12,
                        lg=6
                    )

                ]
            ),

            # =========================================================
            # LINHA 2 - HEATMAP + BARRAS
            # =========================================================

            dbc.Row(
                [

                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                dcc.Loading(
                                    dcc.Graph(
                                        id="grafico-heatmap"
                                    )
                                )
                            ),
                            className="mb-4"
                        ),
                        width=12,
                        lg=6
                    ),

                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                dcc.Loading(
                                    dcc.Graph(
                                        id="grafico-barras"
                                    )
                                )
                            ),
                            className="mb-4"
                        ),
                        width=12,
                        lg=6
                    )

                ]
            ),

            # =========================================================
            # LINHA 3 - PIZZA + DENSIDADE
            # =========================================================

            dbc.Row(
                [

                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                dcc.Loading(
                                    dcc.Graph(
                                        id="grafico-pizza"
                                    )
                                )
                            ),
                            className="mb-4"
                        ),
                        width=12,
                        lg=6
                    ),

                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                dcc.Loading(
                                    dcc.Graph(
                                        id="grafico-densidade"
                                    )
                                )
                            ),
                            className="mb-4"
                        ),
                        width=12,
                        lg=6
                    )

                ]
            ),

            # =========================================================
            # LINHA 4 - REGRESSÃO
            # =========================================================

            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            dcc.Loading(
                                dcc.Graph(
                                    id="grafico-regressao"
                                )
                            )
                        ),
                        className="mb-4"
                    ),
                    width=12
                )
            ),

            # =========================================================
            # RODAPÉ
            # =========================================================

            dbc.Row(
                dbc.Col(
                    html.P(
                        "Projeto desenvolvido em Python utilizando "
                        "Pandas, Plotly, Dash e Dash Bootstrap Components.",
                        className="text-center text-muted mt-2 mb-4"
                    ),
                    width=12
                )
            )

        ],
        fluid=True
    )