# Previsão de Consumo de Produtos - Projeto End-to-End com XGBoost e Flask

# 1. Descrição

Este é um projeto end-to-end de previsão de consumo de produtos para o ano de 2025, baseado em dados históricos de 2023 e 2024. O objetivo é construir um modelo de Machine Learning que, a partir do consumo anual de um produto, seja capaz de prever sua demanda para o ano seguinte.

Para a construção da solução, foi aplicada uma metodologia análoga ao CRISP-DM, abrangendo desde a coleta e limpeza de dados até a criação de um modelo preditivo em produção, disponibilizado via **aplicação web com Flask**.

# 2. Problema de Negócio

## 2.1 Contexto da Empresa

A empresa Colliers International Group Inc. possui um estoque de milhares de produtos. A gestão eficiente desse estoque é crucial para evitar falta de produtos ou excesso (aumento de custos). Atualmente, a previsão de compra é baseada em estimativas, o que gera ineficiências.

## 2.2 Questão de Negócio

O setor de compras precisa de uma ferramenta confiável e de fácil acesso para prever, com antecedência, qual será o consumo de cada produto no próximo ano. O desafio é migrar de um método reativo (baseado em demanda passada) para um método preditivo, baseado em dados e acessível para tomadores de decisão. A pergunta central é:

> **Com base no consumo de 2023, qual será o consumo de um produto em 2025?**

# 3. Entendimento do Negócio

O gerente de suprimentos precisa de um orçamento prévio e de uma previsão de demanda para planejar as compras do próximo ano, otimizar o nível de serviço e negociar com fornecedores. Caracteriza-se, portanto, como um problema clássico de **predição de séries temporais** (regressão), onde a variável alvo é o `consumo_2025` (inferido a partir de `consumo_2024`), e a variável de entrada mais importante é o `consumo_2023`.

A solução precisa ser **interativa e amigável**, permitindo que qualquer usuário do setor de compras possa obter previsões sem precisar escrever código.

# 4. Coleta dos Dados

Os dados foram fornecidos em arquivos `.csv` e representam os registros de movimentação de estoque (entradas e saídas) dos anos de 2023 e 2024.

**Arquivos utilizados:**
- `DADOS 2023.csv`: Dados históricos de consumo referentes ao ano de 2023.
- `DADOS 2024.csv`: Dados históricos de consumo referentes ao ano de 2024.

**Principais colunas originais:**
- `codigo`: Identificador único do produto.
- `produto`: Nome/descrição do produto.
- `movimentacao`: Tipo de movimentação ("saida" ou "entrada").
- `qtd.`: Quantidade movimentada.
- `categoria`, `vl. unitario`: Informações complementares.

# 5. Limpeza e Preparação dos Dados

Nesta etapa, realizada inteiramente em Python com Pandas, os dados foram preparados para análise e modelagem. Os passos principais foram:

1.  **Correção de Encoding:** Foi criada uma função para tratar o encoding (`latin1` para `utf-8`) tanto nos nomes das colunas quanto nos textos, prevenindo erros com caracteres especiais (ex.: "TUBO DE DESCARGA").
2.  **Padronização de Colunas:** Os nomes das colunas foram:
    - Limpos de espaços em branco.
    - Normalizados (removendo acentos e convertendo para ASCII).
    - Convertidos para letras minúsculas (ex.: `vl. unitario` -> `valor_unitario`).
3.  **Tratamento de Números:** A coluna `quantidade` (original `qtd.`) e `valor_unitario` foram convertidas para o tipo numérico, tratando a vírgula como separador decimal.
4.  **Filtragem Essencial**: Foram mantidos **apenas os registros de "saida"** (consumo). As entradas são irrelevantes para a previsão de consumo.
5.  **Agregação:** Os dados foram agrupados por `codigo` e `produto`, somando o consumo total anual. Isso gerou as bases `consumo_2023` e `consumo_2024`.
6.  **Merge Final:** As duas bases foram unidas em um único DataFrame (`df_final`), onde cada linha representa um produto com seus consumos em 2023 e 2024. Valores ausentes (`NaN`) foram preenchidos com `0`.

# 6. Análise Exploratória dos Dados (EDA)

Embora sucinta no notebook, a EDA foi implícita nas etapas de agregação e validação. As principais ações foram:

- **Validação de Colunas:** Garantia de que as colunas necessárias (`codigo`, `produto`, `movimentacao`, `quantidade`) existiam em ambos os DataFrames.
- **Distribuição do Consumo:** O foco foi se preparar para entender como o consumo de 2023 (feature) se relaciona com o consumo de 2024 (target).

# 7. Modelagem dos Dados e Machine Learning

## 7.1 Feature Engineering

A feature utilizada foi simples e direta, derivada diretamente do dado bruto:
- **`consumo_2023` (Feature):** Quantidade total consumida do produto no ano de 2023.
- **`consumo_2024` (Target):** Quantidade total consumida do produto no ano de 2024.

## 7.2 Algoritmo de Machine Learning

Foi escolhido o modelo **XGBoost Regressor**, conhecido por sua alta performance em problemas de regressão estruturada e robustez a outliers.

**Hiperparâmetros configurados:**
- `n_estimators=200`: Número de árvores no ensemble.
- `max_depth=5`: Profundidade máxima de cada árvore.
- `learning_rate=0.1`: Taxa de aprendizado.
- `random_state=42`: Garantir reprodutibilidade.

## 7.3 Treinamento e Avaliação

Os dados foram divididos em treino (80%) e teste (20%) usando `train_test_split`. O modelo foi treinado para aprender a relação `consumo_2023` -> `consumo_2024`.

**Métricas de desempenho no conjunto de teste:**
- **MAE (Erro Absoluto Médio):** 34.02
- **RMSE (Raiz do Erro Quadrático Médio):** 193.06
- **R² (Coeficiente de Determinação):** 0.72

> **Interpretação:** O modelo explica 72% da variância do consumo de 2024 a partir do consumo de 2023. O RMSE de 193 indica que, para produtos com alto consumo, o erro absoluto pode ser grande, mas o R² demonstra uma boa capacidade preditiva.

# 8. Previsão para 2025

O modelo final foi treinado com os dados de 2023 (feature) e 2024 (target). Para prever **2025**, o modelo é aplicado aos dados de consumo de 2024, gerando a `previsao_2025`.

**Exemplo de previsão para um produto específico (código 1010078 - PAPEL TOALHA):**

```python
prever_produto(1010078)
Resultado:
python
{'produto': 'PAPEL TOALHA',
 'consumo_2023': 10247.0,
 'previsao_2025': 10963.41}
Para este produto, a previsão de consumo para 2025 é de ~10.963 unidades.
9. Modelo em Produção - Deploy com Flask
Para tornar o modelo acessível a usuários não técnicos e demonstrar habilidades completas de deploy, foi criada uma aplicação web com Flask.
9.1 Funcionalidades da API Web
A aplicação Flask oferece uma interface simples e intuitiva para consulta de previsões:
•	Interface web amigável: Formulário HTML para entrada de dados.
•	Busca por código do produto: Usuário digita o código e obtém a previsão.
•	Busca por nome do produto: Opção alternativa para encontrar produtos.
•	Resultados em tempo real: Retorno imediato da previsão de consumo para 2025.
9.2 Exemplo de Uso
Conforme demonstrado na interface da aplicação:
text
🔍 Buscar Produto

Código: [1010078]
Nome: [________________]

[Prever]

─────────────────────────

📊 Resultados:

• 1010078 - PAPEL TOALHA → Previsão: 12638.46
9.3 Tecnologias do Deploy
•	Framework Web: Flask (micro-framework Python)
•	Front-end: HTML5, CSS3 (interface responsiva)
•	Serialização do Modelo: Pickle (para salvar/carregar o modelo treinado)
•	Servidor Local: Desenvolvido e testado localmente
9.4 Como Executar a Aplicação
bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Execute a aplicação Flask
python app.py

# 4. Acesse no navegador
http://localhost:5000
10. Conclusão e Resultados de Negócio
O projeto atingiu seu objetivo principal: criar um modelo preditivo de consumo de produtos com um desempenho satisfatório (R² de 0.72) e disponibilizá-lo através de uma aplicação web acessível. Isso permite que o setor de compras:
•	Planeje com mais antecedência: Pode-se prever a demanda para 2025 enquanto ainda se coleta dados de 2024.
•	Baseie decisões em dados: As previsões substituem estimativas manuais.
•	Identifique produtos de alto consumo: O modelo destaca itens críticos (como o "PAPEL TOALHA") que merecem atenção especial no planejamento de estoque.
•	Acessibilidade democrática: Qualquer pessoa do setor pode usar a interface web, sem necessidade de conhecimento em programação.
•	Tomada de decisão mais rápida: Respostas imediatas através da API Flask.
11. Próximos Passos e Melhorias
Para evoluir o projeto e melhorar a precisão, as seguintes ações são sugeridas:
1.	Incluir mais features: Adicionar informações como categoria, valor_unitario e sazonalidade (mês a mês, em vez de total anual).
2.	Testar outros modelos: Comparar o XGBoost com Random Forest, LightGBM ou uma regressão linear simples.
3.	Tratar a sazonalidade interna: Separar o consumo por trimestre/semestre para capturar padrões.
4.	Melhorar a interface web: Adicionar gráficos de evolução do consumo e dashboard interativo.
5.	Deploy em nuvem: Hospedar a aplicação no Heroku, Render ou AWS para acesso global.
6.	Criar uma API REST: Disponibilizar endpoints para integração com sistemas da empresa.
7.	Adicionar autenticação: Controle de acesso para usuários autorizados.
8.	Realizar validação cruzada: Para uma avaliação mais robusta do modelo.
12. Ferramentas Utilizadas
12.1 Linguagem e Ambiente
•	Linguagem: Python 3.14
•	Ambiente: Jupyter Notebook (desenvolvimento) + Ambiente Python (produção)
12.2 Principais Bibliotecas
•	Manipulação de Dados: pandas, numpy
•	Machine Learning: xgboost, scikit-learn
•	Web App: flask, pickle
•	Processamento de Texto: unicodedata
12.3 Estrutura do Projeto
text
├── app.py                 # Aplicação Flask
├── model.pkl              # Modelo treinado serializado
├── requirements.txt       # Dependências do projeto
├── templates/
│   └── index.html        # Interface web
├── static/
│   └── style.css         # Estilos da aplicação
├── DADOS 2023.csv         # Dados históricos
├── DADOS 2024.csv         # Dados históricos
└── Untitled.ipynb         # Notebook de desenvolvimento
Sobre o Projeto
Este projeto foi desenvolvido como parte de um portfólio de Ciência de Dados, demonstrando a capacidade de construir um pipeline de Machine Learning end-to-end completo, desde a leitura de dados csv "sujos" até a criação de um modelo preditivo funcional e seu deploy em uma aplicação web com Flask.
Diferenciais do projeto:
•	✅ Tratamento robusto de dados reais (encoding, padronização)
•	✅ Modelagem com XGBoost (alta performance)
•	✅ Métricas claras de avaliação (MAE, RMSE, R²)
•	✅ Interface web amigável para usuários finais
•	✅ Código comentado e organizado
•	✅ Projeto pronto para deploy em produção
________________________________________
Status do Projeto: ✅ Concluído (com deploy funcional). Pronto para iterações e melhorias futuras.
Autor: Tulio Silva dos Santos
LinkedIn: https://www.linkedin.com/in/túlio-santos-b65720a4/
GitHub: tuliosannttos
