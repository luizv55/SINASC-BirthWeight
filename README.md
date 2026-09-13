<div align="center">

# Predição do peso ao nascer em Minas Gerais com modelos de regressão (dados SINASC)

> Projeto end-to-end utilizando modelos de regressão para prever o peso de bebês recém-nascidos do estado de Minas Gerais, com dados do SINASC (2020–2024), comparação entre Linear Regression, Ridge, Lasso, Random Forest, XGBoost e LightGBM (tunados com Optuna), e com deploy via MLflow Model Registry, rastreamento de experimentos e serving em produção via FastAPI.
</div>

---

### Sobre este projeto
Peso ao nascer é um dos indicadores mais diretos de saúde neonatal, bebês fora da faixa esperada têm risco maior de complicações e exigem acompanhamento diferente logo na maternidade. Este projeto mostra como um pipeline de Machine Learning consegue prever o peso de recém-nascidos em Minas Gerais a partir de dados públicos de saúde, comparando seis modelos diferentes até chegar a um XGBoost como referência.

O modelo é treinado com dados do SINASC (Sistema de Informações sobre Nascidos Vivos), extraídos direto do FTP do DATASUS em formato .dbc e cobrindo o estado de Minas Gerais entre 2020 e 2024.

**O que este projeto cobre:**

- Ingestão de dados do DATASUS via pyreaddbc, direto do FTP público
- Análise exploratória com matplotlib e seaborn
- Engenharia de atributos: redução de multicolinearidade por VIF, one-hot encoding e padronização com StandardScaler
- Treinamento de seis modelos (Regressão Linear, Ridge, Lasso, Random Forest, XGBoost, LightGBM), com o LightGBM ajustado via Optuna
- Análise de resíduos e comparação de performance entre os modelos, com o XGBoost como referência
- Rastreamento de experimentos com MLflow
-Serviço de predições via API de model serving do próprio MLflow

## Como Funciona

```
Usuário Insere Dados da Gestante/Nascimento
   (idade da mãe, semanas de gestação,
     consultas pré-natal, etc.)
              │
              ▼
    Pré-processamento dos Dados
(One-Hot Encoding → Padronização com StandardScaler)
              │
              ▼
   Modelo Treinado (XGBoost) Servido via MLflow
              │
              ▼
    Peso Estimado do Recém-Nascido
         (em gramas)
              │
              ▼
  Resultado Exibido ao Usuário

```

---

## Dataset

| Propriedade | Detalhes |
|---|---|
| **Nome** | SINASC — Sistema de Informações sobre Nascidos Vivos |
| **Autor** | DATASUS (Ministério da Saúde) |
| **Fonte** | [FTP público do DATASUS](https://datasus.saude.gov.br/transferencia-de-arquivos/) |
| **Cobertura** | Nascidos vivos em Minas Gerais, 2020–2024 |
| **Alvo** | Peso ao nascer (gramas) |
| **Formato** | `.dbc` (DATASUS) → convertido via `pyreaddbc` |
| **Tarefa** | Regressão (predição de peso ao nascer) |

---

## Model Performance

| Modelo | MAE | RMSE | R² |
|---|---|---|---|
| **XGBoost** | **319.89** | **417.97** | **0.4000** |
| LightGBM | 319.99 | 418.08 | 0.4000 |
| Random Forest | 320.32 | 418.46 | 0.4000 |
| Regressão Linear | 328.46 | 428.58 | 0.3718 |
| Ridge | 328.43 | 428.59 | 0.3700 |
| Lasso | 328.44 | 428.60 | 0.3700 |
 
> **Por que XGBoost?** Os três modelos baseados em árvore (XGBoost, LightGBM, Random Forest) empatam tecnicamente em performance, com uma vantagem marginal e consistente sobre os modelos lineares. O XGBoost foi escolhido como referência por equilibrar essa performance com maior controle de overfitting via regularização e por ser o padrão de mercado em tarefas tabulares.
 
> **Por que o R² fica em torno de 0.40?** Peso ao nascer é influenciado por fatores não capturados nas variáveis do SINASC (genética, nutrição materna, condições intrauterinas), o que limita o quanto qualquer modelo consegue explicar só com dados administrativos de nascimento.

## Estrutura do projeto

```
SINASC-BIRTHWEIGHT/
│
├── data/                       # Dados brutos e processados do SINASC
│
├── dicionario.ipynb            # Dicionário de variáveis e códigos do SINASC
├── main.ipynb                  # Pipeline principal: EDA, feature engineering, treino e avaliação
├── transform.py                # Ingestão e transformação dos dados (.dbc → DataFrame)
│
├── .gitignore                  # Arquivos ignorados pelo Git
├── LICENSE                     # Licença do projeto
├── requirements.txt            # Dependências Python
└── README.md                   
```

---

## Introdução
### 1. Clone o repositório

```bash
git clone https://github.com/luizv55/SINASC-BirthWeight.git
cd "SINASC-BirthWeight/SINASC-BirthWeight"
```

### 2. Configure o ambiente

```bash
python3.11 -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

pip install -r requirements.txt
```
**Importante:** Para o pacote de conversão de arquivos .dbc, deve ser utilizado a versão 3.11 do python.

### 3. Download dos dados

Os dados brutos utilizados estão na pasta já transformados em .csv, se desejar baixa-los novamente, pode utilizar o transform.py

### 4. Treine o modelo

```bash
jupyter notebook notebooks/main.ipynb
```

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.10+ |
| Data Ingestion | `pyreaddbc` (leitura de arquivos `.dbc` do DATASUS) |
| Data / EDA | Pandas, NumPy, Matplotlib, Seaborn |
| Feature Engineering | scikit-learn (OneHotEncoder, StandardScaler), statsmodels (VIF) |
| Machine Learning | scikit-learn, XGBoost, LightGBM |
| Hyperparameter Tuning | Optuna |
| Experiment Tracking | MLflow |
| Model Serving | MLflow Serving |
| Notebook | Jupyter |

---
