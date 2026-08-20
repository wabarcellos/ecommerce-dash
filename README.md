# Ecommerce Dashboard

Dashboard interativo desenvolvido em **Python, Dash e Plotly** para análise e visualização de dados de um e-commerce.

O projeto foi desenvolvido como parte do módulo de **Visualização de Dados** do curso de Análise de Dados, com o objetivo de transformar dados de vendas em informações visuais que facilitem a análise do comportamento dos produtos e clientes.

## 🎯 Objetivo

Criar uma aplicação web interativa capaz de apresentar diferentes análises sobre os dados de um e-commerce, permitindo ao usuário explorar os resultados por meio de filtros.

O dashboard apresenta informações relacionadas a:

- Quantidade de produtos vendidos;
- Avaliações dos produtos;
- Notas atribuídas pelos clientes;
- Preços dos produtos;
- Categorias;
- Gênero;
- Distribuição e relacionamento entre as principais variáveis.

## 🛠️ Tecnologias utilizadas

- **Python**
- **Pandas** — tratamento e manipulação dos dados
- **Plotly** — criação das visualizações interativas
- **Dash** — desenvolvimento da aplicação web
- **Dash Bootstrap Components** — estilização e organização da interface

## 📊 Visualizações

O dashboard possui **7 gráficos interativos**:

1. **Quantidade de produtos vendidos por gênero**
2. **Distribuição das avaliações**
3. **Relação entre avaliações e quantidade de produtos vendidos**
4. **Quantidade de produtos vendidos por categoria**
5. **Distribuição das notas**
6. **Distribuição dos preços**
7. **Relação entre preço e quantidade de produtos vendidos**

As visualizações podem ser atualizadas de acordo com os filtros selecionados no dashboard.

## 🔎 Filtros

A aplicação possui filtros que permitem analisar os dados de diferentes perspectivas.

Entre as opções disponíveis está o filtro de **gênero**, incluindo a opção **Todos**, selecionada por padrão ao abrir o dashboard.

Dessa forma, o usuário pode visualizar inicialmente todos os dados e, posteriormente, selecionar um grupo específico para realizar uma análise mais direcionada.

## 📁 Estrutura do projeto

```text
ecommerce-dash/
│
├── app.py
├── layout.py
├── callbacks.py
├── ecommerce_estatistica.csv
├── requirements.txt
└── README.md
```

### `app.py`

Arquivo responsável pela inicialização da aplicação Dash e pela execução do servidor.

### `layout.py`

Contém a estrutura visual do dashboard, incluindo filtros, gráficos e componentes da interface.

### `callbacks.py`

Contém as funções responsáveis pela interatividade da aplicação e atualização dos gráficos conforme os filtros selecionados.

### `ecommerce_estatistica.csv`

Base de dados utilizada para as análises e visualizações.

### `requirements.txt`

Lista das bibliotecas e dependências necessárias para executar o projeto.

## ▶️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/wabarcellos/ecommerce-dash.git
```

### 2. Acesse a pasta do projeto

```bash
cd ecommerce-dash
```

### 3. Crie um ambiente virtual

No Windows:

```bash
python -m venv .venv
```

Ative o ambiente:

```bash
.venv\Scripts\activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute a aplicação

```bash
python app.py
```

Após executar, o Dash disponibilizará o endereço local da aplicação no terminal. Acesse o endereço pelo navegador para visualizar o dashboard.

## 📚 Aprendizados

Durante o desenvolvimento deste projeto foram aplicados conceitos de:

- Manipulação e análise de dados com Pandas;
- Criação de visualizações com Plotly;
- Desenvolvimento de dashboards interativos com Dash;
- Utilização de callbacks;
- Criação de filtros interativos;
- Organização de aplicações Python;
- Análise exploratória de dados;
- Visualização e interpretação de informações;
- Estruturação de projetos para publicação no GitHub.

## 🚀 Próximos passos

Como possíveis melhorias futuras, o projeto pode receber:

- Novos indicadores e métricas;
- Mais filtros para exploração dos dados;
- Cards com KPIs;
- Melhorias no layout e responsividade;
- Publicação do dashboard em uma plataforma de hospedagem;
- Novas análises para apoiar a tomada de decisão.

## 👩‍💻 Autora

**Walessa Barcellos**

Projeto desenvolvido durante a formação em **Análise de Dados**, como prática de Python, visualização de dados e desenvolvimento de dashboards interativos.
