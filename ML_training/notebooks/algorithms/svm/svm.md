# Máquina de Vetores de Suporte (SVM)

## 📌 Descrição

A **Máquina de Vetores de Suporte (SVM)** é um algoritmo de aprendizado supervisionado amplamente utilizado para tarefas de **classificação** e **regressão**.  
Sua principal ideia é encontrar um **hiperplano ótimo** que separe as classes de forma clara e com a maior margem possível.

![Exemplo de SVM](https://iacomcafe.com.br/wp-content/uploads/2024/09/support-vector-machine-1.png)

---

## 1. ⚙️ Hiperparâmetros

### 🔹 Definição

Hiperparâmetros são parâmetros definidos **antes** do processo de treinamento e influenciam diretamente o desempenho do modelo.  
Diferente dos parâmetros aprendidos durante o treinamento, os hiperparâmetros são ajustados manualmente ou com técnicas de validação.

### 🔸 Exemplo: Hiperparâmetro `C` (Constante de Penalização)

- O parâmetro `C` controla o equilíbrio entre a **maximização da margem** e a **minimização do erro de classificação**.
- **Valores altos de `C`**:
  - O modelo tenta classificar todos os exemplos corretamente.
  - Pode resultar em **overfitting** (ajuste excessivo).
- **Valores baixos de `C`**:
  - Permite mais erros de classificação.
  - Gera **margens maiores** e maior capacidade de generalização.
  - Pode levar a **underfitting**.

---

## 2. 🌀 Kernel Trick

O **Kernel Trick** permite que o SVM resolva problemas de **classificação não linear** ao transformar os dados para um espaço de **maior dimensão**, onde se torna possível encontrar um **hiperplano linear** que separe as classes.

![Exemplo de Kernel Trick](https://miro.medium.com/v2/resize:fit:838/1*gXvhD4IomaC9Jb37tzDUVg.png)

### 🔧 Funções de kernel comuns:

- `Linear`
- `Polinomial`
- `RBF` (Radial Basis Function ou Gaussiano)
- `Sigmoide`

### 🎯 Impacto da escolha do kernel

A escolha adequada do kernel e o ajuste dos seus hiperparâmetros (como o parâmetro `gamma` no caso do RBF) influenciam fortemente a capacidade do modelo de capturar padrões complexos nos dados.

> ⚠️ **Nota:** Um kernel mal ajustado pode resultar em **overfitting** ou **underfitting**, dependendo da complexidade do problema e da quantidade de dados disponíveis.
