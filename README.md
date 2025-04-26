# 🚀 ML Training Repository

Bem-vindo ao repositório **ML Training**! Este projeto foi criado com o objetivo de explorar, pré-processar e treinar modelos de machine learning em diversos datasets, comparando sua acurácia para identificar os melhores algoritmos para cada cenário.

---

## 📌 Objetivo

Este repositório é um ambiente organizado para:
- **Pré-processar dados** de forma eficiente, garantindo que estejam prontos para treinamento.
- **Treinar e avaliar modelos** de machine learning em diferentes datasets.
- **Comparar a acurácia** dos modelos para determinar qual algoritmo performa melhor em cada contexto.

---

## 🗂 Estrutura do Repositório

```
ML_training/
├── data/
│   ├── external/         # Dados brutos obtidos de fontes externas
│   └── processed/        # Dados após pré-processamento
│
├── notebooks/            # Jupyter Notebooks para análise e experimentação
│   ├── algorithms/       # Notebooks específicos para cada algoritmo
│   └── pre_processing/   # Notebooks dedicados ao pré-processamento
│
├── src/                  # Código fonte em Python
│   ├── utils/            # Utilitários e funções auxiliares
│   │   └── __pycache__/
│   ├── __init__.py       # Inicialização do módulo
│   ├── data_loader.py    # Script para carregar dados
│   └── .gitkeep          # Arquivo para manter a pasta no Git
│
└── requirements.txt      # Dependências do projeto
```

---

## 🛠 Como Usar

1. **Clone o repositório**:
   ```bash
   git clone [URL_DO_REPOSITORIO]
   ```

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Explore os notebooks**:
   - Utilize os notebooks em `notebooks/pre_processing/` para pré-processar seus dados.
   - Experimente os algoritmos em `notebooks/algorithms/` para treinar e avaliar modelos.

4. **Adicione seus datasets**:
   - Coloque os dados brutos em `data/external/`.
   - Após o pré-processamento, os dados limpos serão salvos em `data/processed/`.

5. **Contribua**:
   - Sinta-se à vontade para adicionar novos algoritmos, melhorar o pré-processamento ou sugerir melhorias!

---

## 📊 Modelos e Técnicas

O repositório é flexível para incluir diversos algoritmos de machine learning, como:
- Regressão Linear
- Decision Trees
- SVM (Support Vector Machines)
- Entre outros.

O foco é comparar sua performance em diferentes datasets.

---

