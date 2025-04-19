# KNN (K-Nearest Neighbors)

## 📌 Descrição

O **KNN (K-Nearest Neighbors)** é um algoritmo de aprendizado supervisionado usado tanto para **classificação** quanto para **regressão**, sendo mais comum em tarefas de **classificação**.

![Exemplo de KNN](https://miro.medium.com/v2/resize:fit:1358/0*jqxx3-dJqFjXD6FA)

Ele é baseado na ideia de **proximidade**: para classificar um novo exemplo, o KNN analisa os `K` exemplos mais próximos no conjunto de dados de treino e atribui a classe **mais comum** entre eles.

> 🧠 Intuição: “Diga-me com quem andas, e eu te direi quem és.” – Se os vizinhos mais próximos são da classe A, é provável que o novo ponto também pertença à classe A.

---

## 1. 🧭 Como Funciona?

1. Escolha um número **K** de vizinhos (ex: 3, 5, 7...).
2. Calcule a **distância** entre o ponto a ser classificado e todos os pontos do conjunto de treinamento (geralmente usando a **distância Euclidiana**).
3. Selecione os **K vizinhos mais próximos**.
4. Para **classificação**:
   - Faça uma votação entre as classes dos vizinhos.
   - A classe mais frequente é atribuída ao novo ponto.
5. Para **regressão**:
   - A média dos valores dos vizinhos é usada como predição.

---

## 2. 📏 Distâncias Comuns

- **Euclidiana**: `sqrt((x1 - x2)^2 + (y1 - y2)^2)`
- **Manhattan**: `|x1 - x2| + |y1 - y2|`
- **Minkowski**: generaliza as anteriores
- **Cosseno**: útil para vetores em espaços de alta dimensão (ex: texto)

> ⚠️ A escolha da **métrica de distância** pode afetar bastante a performance do algoritmo.

---

## 3. 🔧 Hiperparâmetros Importantes

| Parâmetro      | Descrição |
|----------------|-----------|
| `n_neighbors`  | Número de vizinhos a considerar. Valores baixos tornam o modelo mais **sensível ao ruído**. |
| `weights`      | Pode ser `"uniform"` (padrão) ou `"distance"` (mais peso para vizinhos mais próximos). |
| `metric`       | Tipo de distância usada (padrão: `"minkowski"`). |
| `p`            | Parâmetro da métrica Minkowski (p=2 → Euclidiana, p=1 → Manhattan). |

---

## 4. 📊 Avaliação e Performance

O KNN é um **modelo preguiçoso**: ele **não aprende** um modelo explícito, apenas armazena os dados de treinamento e calcula tudo na fase de inferência.

📉 Pode ser **ineficiente com grandes volumes de dados**, pois precisa calcular distâncias para todos os pontos durante a predição.

✅ Métricas comuns para avaliação de classificação:

- Acurácia
- Precisão / Recall
- F1-score
- Matriz de Confusão

---

## 🧠 Dicas Finais

- Escolha **K ímpar** para evitar empates em classificação binária.
- O **escalonamento dos dados** é essencial para o KNN.
- Para grandes bases de dados, considere o uso de estruturas como **KD-Trees** ou **Ball Trees** para melhorar a performance.
- KNN funciona melhor quando os dados possuem **baixa dimensionalidade** e **pouco ruído**.

---