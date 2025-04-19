# Árvore de Decisão

## 📌 Descrição

A **Árvore de Decisão** é um algoritmo de aprendizado supervisionado usado tanto para **classificação** quanto para **regressão**. Sua principal característica é sua estrutura ramificada que, mapeando as possiblidades, na parte de classificação, consegue decidir a resposta para determinada condição.

![Exemplo de Árvore de Decisão](https://colaborae.com.br/wp-content/uploads/2023/07/arvore.png)

Sua estrutura é formada por **nós**: Ele possui o nó de origem, seus ramos, nós intermediários e seus filhos. Sendo o nó final, **ou folha**, o responsável pela decisão tomada.

> 🧠 Intuição: Pensa que você é uma pessoa tentando decidir se deve levar um guarda-chuva antes de sair de casa.

Você vai tomar decisões com base em perguntas simples, tipo:

    Está nublado?

        Se sim, vá para a próxima pergunta.

        Se não, provavelmente não vai chover, então não leva o guarda-chuva.

    A previsão diz que vai chover?

        Se sim, então leve o guarda-chuva.

        Se não, não precisa levar.


![Intuição](https://www.hashtagtreinamentos.com/wp-content/uploads/2022/11/Arvore-de-Decisao-1.png)

---

## 1. 🧭 Coeficinetes

1. **Gini (impureza de Gini)**

    Mede a probabilidade de um item ser classificado errado se for escolhido aleatoriamente.

    Varia de 0 (puro, só uma classe) até um valor máximo (quanto mais bagunça, mais alto).

    $$
    Gini = 1 - \sum p_i^2
    $$

    Onde pipi​ é a proporção de cada classe no grupo.

🧠 Interpretação intuitiva: quão "misturado" está o grupo. Quanto mais misturado (ex: metade sim, metade não), maior a impureza.

2. **Entropia (ou ganho de informação)**

    Vem da teoria da informação.

    Mede o grau de incerteza ou impureza.

    $$
    Entropia = - \sum p_i \log_2(p_i)
    $$

    O ganho de informação é quanto a entropia diminui ao fazer uma divisão.

🧠 Intuição: quanto mais “bagunçado” o grupo, maior a entropia. A gente quer divisões que deixem os grupos mais “puros”.

3. **Redução de variância (usado em árvores de regressão)**

    Em problemas de regressão (prever números, não classes), usa-se a variância como medida de qualidade da divisão.

    A árvore tenta fazer cortes que reduzam a variância dos valores nos grupos.

🧠 Intuição: se você separar os dados e o valor das saídas ficar mais parecido dentro de cada grupo, é uma boa divisão.

---

2. ✂️ Podagem (Pruning)

Durante o treinamento, uma árvore de decisão pode crescer demais, criando divisões muito específicas para os dados de treino. Isso pode causar overfitting, ou seja, o modelo aprende os "ruídos" dos dados ao invés dos padrões reais.

A podagem serve para controlar o tamanho da árvore, removendo partes desnecessárias e tornando o modelo mais simples e eficiente.
🔸 Tipos de podagem:
🔹 Poda Prévia (Pré-podamento)

Acontece durante a construção da árvore. Aqui, colocamos limites para impedir que ela cresça demais:

    max_depth: profundidade máxima da árvore

    min_samples_split: número mínimo de amostras para dividir um nó

    min_samples_leaf: número mínimo de amostras em uma folha

Aqui a árvore é construída completamente, e depois são removidos os ramos que não contribuem muito para a performance, com base em uma métrica de custo/complexidade.

    Em scikit-learn, usamos o parâmetro ccp_alpha (pruning de custo-complexidade).

modelos_podados = [DecisionTreeClassifier(ccp_alpha=alpha).fit(X_train, y_train) for alpha in ccp_alphas]

🧠 Intuição:

Pensa numa árvore real cheia de galhos. Se você deixar todos eles crescerem, alguns vão ficar fracos, secos ou inúteis. Podando esses galhos, a árvore fica mais forte, mais saudável e mais eficiente. O mesmo vale para a árvore de decisão.