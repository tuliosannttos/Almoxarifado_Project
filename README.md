# 🚀 Previsão de Consumo de Produtos com XGBoost + Flask

> Projeto real desenvolvido no almoxarifado corporativo da empresa Colliers International Group Inc., com foco em previsão de demanda e otimização do controle de estoque.

## 📌 Sobre o Projeto

Este é um projeto real de Ciência de Dados aplicado ao setor de almoxarifado corporativo da empresa Colliers International Group Inc.

O projeto foi desenvolvido com o objetivo de prever o consumo futuro de materiais e produtos utilizados nas operações internas da empresa, utilizando dados históricos reais de movimentações de estoque.

A solução foi construída utilizando técnicas de Machine Learning e Engenharia de Dados, permitindo transformar dados operacionais em previsões estratégicas de demanda.

O modelo foi treinado com dados históricos de consumo dos anos de 2023 e 2024, sendo capaz de prever automaticamente a demanda de produtos para 2025.

Além do desenvolvimento do modelo preditivo, também foi realizado o deploy da aplicação utilizando Flask, disponibilizando o modelo em ambiente web/API para consultas de previsão em tempo real.

Este projeto demonstra uma aplicação prática e corporativa de Ciência de Dados voltada para:

* Controle de estoque
* Planejamento de compras
* Logística interna
* Gestão operacional
* Redução de desperdícios
* Tomada de decisão baseada em dados

---

# 🎯 Objetivos do Projeto

* Realizar tratamento e padronização de dados históricos
* Identificar padrões de consumo de produtos
* Construir um modelo de Machine Learning para previsão de demanda
* Disponibilizar o modelo através de deploy com Flask
* Auxiliar processos logísticos e controle de estoque

---

# 🛠 Tecnologias Utilizadas

## 📚 Bibliotecas Python

* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Flask
* Unidecode / UnicodeData

---

# 📊 Pipeline do Projeto

## 🔹 1. Carregamento dos Dados

Os dados utilizados no projeto foram importados a partir de arquivos CSV contendo informações de movimentações de estoque dos anos de 2023 e 2024.

python
pd.read_csv()

---

## 🔹 2. Tratamento e Padronização

Foi realizado um processo completo de limpeza e padronização dos dados:

* Correção de encoding
* Padronização de colunas
* Remoção de caracteres especiais
* Conversão de tipos numéricos
* Normalização dos nomes das colunas

Exemplo:

python
unicodedata.normalize() 


---

## 🔹 3. Filtragem de Consumo

O projeto considera apenas movimentações de saída de produtos, representando efetivamente o consumo.

```python
df[df["movimentacao"] == "saida"]
```

---

## 🔹 4. Engenharia de Features

Os dados foram agrupados por:

* Código do produto
* Nome do produto
* Quantidade consumida

Posteriormente foi realizado o merge das bases de 2023 e 2024 para criação das variáveis utilizadas no treinamento.

---

# 🤖 Machine Learning

## 🔹 Modelo Utilizado

O algoritmo escolhido foi o XGBoost Regressor, um dos modelos mais eficientes para problemas de regressão e previsão.

### Configurações do modelo:

```python
XGBRegressor(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.1,
    random_state=42
)
```

---

## 🔹 Divisão dos Dados

Os dados foram divididos entre treino e teste utilizando:

```python
train_test_split()
```

* 80% treino
* 20% teste

---

## 📈 Métricas de Avaliação

Por se tratar de um problema de regressão, o desempenho do modelo foi avaliado utilizando métricas estatísticas apropriadas para previsão numérica.

## 🔹 Métricas utilizadas

### ✅ MAE — Mean Absolute Error

Mede o erro médio absoluto entre os valores previstos e os valores reais.

📌 Resultado obtido no projeto:

```python
MAE: 34.02
```

Isso significa que, em média, o modelo apresentou um erro aproximado de 34 unidades por previsão.

---

### ✅ RMSE — Root Mean Squared Error

Mede a raiz do erro quadrático médio.

Essa métrica penaliza erros maiores e ajuda a avaliar a estabilidade do modelo.

📌 Resultado obtido no projeto:

```python
RMSE: 193.06
```

---

### ✅ R² Score

Indica o quanto o modelo consegue explicar a variabilidade dos dados.

📌 Resultado obtido no projeto:

```python
R² Score: 0.72
```

Isso significa que o modelo conseguiu explicar aproximadamente 72% da variabilidade do consumo dos produtos, demonstrando boa capacidade preditiva para um cenário real de operação logística.

---

## 🔹 Funções utilizadas

```python
mean_absolute_error()
mean_squared_error()
r2_score()
```

As métricas demonstraram que o modelo conseguiu capturar padrões importantes de consumo, apresentando boa capacidade preditiva para utilização em cenários reais de operação e controle de estoque no almoxarifado da Colliers International Group Inc.

---

# 🔍 Sistema de Previsão

Foi criada uma função responsável por prever automaticamente o consumo futuro de um produto com base no código informado.

```python
prever_produto(codigo)
```

A função retorna:

* Nome do produto
* Consumo histórico
* Previsão futura de demanda

---

# 🌐 Deploy com Flask

Após o treinamento e validação do modelo de Machine Learning, foi realizado o deploy da aplicação utilizando Flask.

O Flask foi utilizado para transformar o modelo preditivo em uma aplicação web/API funcional, permitindo consultas de previsão em tempo real.

Essa etapa aproxima o projeto de um ambiente corporativo real, demonstrando não apenas a construção do modelo, mas também sua disponibilização para uso operacional.

## 🔹 Funcionalidades do Deploy

* Disponibilização do modelo em ambiente web
* Consulta de previsões em tempo real
* Estruturação de API para integração futura
* Simulação de ambiente de produção
* Integração entre Ciência de Dados e aplicações backend

## 🔹 Objetivos do Deploy

* Disponibilizar o modelo em produção
* Permitir previsões em tempo real
* Criar uma estrutura de API para integração
* Simular um ambiente real de aplicação de Machine Learning

---

# 📁 Estrutura do Projeto

```bash
📦 projeto-previsao-consumo
 ┣ 📂 data
 ┃ ┣ 📄 DADOS 2023.csv
 ┃ ┗ 📄 DADOS 2024.csv
 ┣ 📄 app.py
 ┣ 📄 modelo.pkl
 ┣ 📄 requirements.txt
 ┣ 📄 notebook.ipynb
 ┗ 📄 README.md
```

---

# ▶ Como Executar o Projeto

## 🔹 1. Clonar o Repositório

```bash
git clone <URL_DO_REPOSITORIO>
```

---

## 🔹 2. Criar Ambiente Virtual

```bash
python -m venv venv
```

---

## 🔹 3. Ativar Ambiente Virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## 🔹 4. Instalar Dependências

```bash
pip install -r requirements.txt
```

---

## 🔹 5. Executar Flask

```bash
python app.py
```

---

# 📊 Resultados do Projeto

O modelo foi capaz de identificar padrões históricos de consumo e gerar previsões automatizadas para os produtos analisados.

A solução permitiu transformar dados operacionais do almoxarifado em informações estratégicas para apoio à tomada de decisão.

## 🔹 Benefícios da solução

* Maior previsibilidade de consumo
* Apoio ao planejamento de compras
* Melhor controle de estoque
* Redução de desperdícios
* Apoio à gestão logística
* Otimização operacional

O projeto demonstra uma aplicação prática de Machine Learning em ambiente corporativo real, utilizando dados reais de operação da Colliers International Group Inc.

---

# 📌 Diferenciais do Projeto

✅ Projeto real aplicado em ambiente corporativo

✅ Dados reais de movimentação de estoque

✅ Aplicação prática no almoxarifado da Colliers International Group Inc.

✅ Pipeline completo de Ciência de Dados

✅ Tratamento e padronização de dados

✅ Engenharia de Features

✅ Machine Learning com XGBoost

✅ Avaliação com métricas de regressão

✅ Deploy do modelo com Flask

✅ Estrutura pronta para produção

---

# 📚 Aprendizados

Durante o desenvolvimento deste projeto foram aplicados conhecimentos em:

* Engenharia de Dados
* Limpeza e tratamento de dados
* Machine Learning
* Regressão
* Deploy de modelos
* APIs com Flask
* Estruturação de projetos de Ciência de Dados

---

# 👨‍💻 Autor

Desenvolvido por Tulio Santos.

📌 Projeto desenvolvido para fins de estudo, portfólio e demonstração prática de habilidades em Ciência de Dados e Machine Learning.

