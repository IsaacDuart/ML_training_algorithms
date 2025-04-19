# Naive Bayes

## 📌 Descrição

O **Naive Bayes** é um algoritmo de aprendizado supervisionado baseado no **Teorema de Bayes**.  
Ele é amplamente utilizado em tarefas de **classificação**, especialmente quando há grande volume de dados textuais, como na filtragem de spam e análise de sentimentos.

A principal ideia é calcular a **probabilidade de uma amostra pertencer a uma determinada classe**, considerando as probabilidades anteriores e a verossimilhança das features — assumindo que elas são **independentes entre si**, o que simplifica os cálculos.

---

## 1. ⚙️ Hiperparâmetros

### 🔹 Definição

Hiperparâmetros são definidos **antes** do processo de treinamento e afetam diretamente a performance do modelo.  
No caso do Naive Bayes, os hiperparâmetros controlam o comportamento de suavização e o tratamento das distribuições de probabilidade.

### 🔸 Exemplo: Hiperparâmetro `var_smoothing` (no GaussianNB)

- Esse hiperparâmetro adiciona um pequeno valor à variância calculada de cada feature, evitando divisão por zero.
- **Valores muito baixos**:
  - Podem causar instabilidade numérica.
- **Valores maiores**:
  - Aumentam a suavização, podendo reduzir o risco de overfitting.

> ℹ️ O Naive Bayes é conhecido por ter **poucos hiperparâmetros**, o que o torna simples e rápido de treinar.

---

## 2. 📊 Teorema de Bayes

O algoritmo se baseia na fórmula:

\[
P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}
\]

### Componentes:

- \( P(A|B) \): **Probabilidade posterior** (classe A dado os dados B)
- \( P(B|A) \): **Verossimilhança** (como os dados são prováveis sob a classe A)
- \( P(A) \): **Probabilidade a priori** da classe
- \( P(B) \): **Probabilidade dos dados** (usado para normalizar)

O Naive Bayes classifica a instância na classe com **maior probabilidade posterior**.

---

## 3. 🧠 Variações do Naive Bayes

Cada tipo de Naive Bayes é adaptado para um tipo específico de dado:

- **Gaussian Naive Bayes**: assume que as features seguem uma distribuição normal (contínuo).
- **Multinomial Naive Bayes**: usado para contagem de ocorrências (ex: palavras).
- **Bernoulli Naive Bayes**: adequado para dados binários (ex: presença/ausência de termos).

---

## 4. ⚖️ Vantagens e Desvantagens

### ✅ Vantagens

- Muito rápido e simples de implementar.
- Funciona bem com **muitos atributos independentes**.
- Pouco sensível ao tamanho do dataset.
- Requer pouco ajuste de parâmetros.

### ❌ Desvantagens

- A suposição de **independência entre features** raramente é verdadeira.
- Pode ter desempenho inferior em dados onde há **forte correlação entre atributos**.

---

## 5. 🎯 Quando usar?

- Classificação de texto (e-mails, documentos, tweets).
- Detecção de spam.
- Análise de sentimentos.
- Problemas de classificação com grande volume de dados e atributos.

> 💡 Mesmo com uma suposição tão "ingênua", o Naive Bayes continua sendo um dos algoritmos **mais eficazes e rápidos** em diversos contextos práticos.
