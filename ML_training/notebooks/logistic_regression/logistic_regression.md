# Regressão Logística

## 📌 Descrição

A **Regressão Logística** é um algoritmo de aprendizado supervisionado amplamente utilizado para tarefas de **classificação**, especialmente em problemas binários (ex: doença vs. saudável, spam vs. não-spam).

Diferente da regressão linear, seu objetivo não é prever valores contínuos, mas sim **estimar a probabilidade** de uma amostra pertencer a uma determinada classe. Essa probabilidade é obtida aplicando a função **sigmoide (logística)** sobre uma combinação linear das variáveis de entrada.

> 📈 Por exemplo: se o modelo retorna uma probabilidade de 0.82 para a classe "positivo", isso pode ser interpretado como uma **alta confiança** de que a instância pertence àquela classe.

![Exemplo de Regressão Logística](https://brains.dev/wp-content/uploads/2023/01/log_reg8.png)

---

## 1. ⚙️ Limiar de Decisão

### 🔹 Definição

A saída da regressão logística é uma probabilidade entre 0 e 1. Para transformar essa probabilidade em uma **decisão de classe**, utiliza-se um **limiar de decisão (threshold)**.  
O valor padrão mais comum é **0.5**, ou seja:
- Se `p >= 0.5`, a amostra é classificada como **classe positiva**;
- Caso contrário, como **classe negativa**.

Esse limiar pode ser ajustado dependendo da aplicação. Por exemplo, em diagnósticos médicos, pode ser interessante **reduzir o limiar** para detectar mais casos positivos, mesmo ao custo de mais falsos positivos.

![Exemplo de Limiar de Decisão](https://d1.awsstatic.com/S-curve.36de3c694cafe97ef4e391ed26a5cb0b357f6316.png)

---

## 2. 🔧 Hiperparâmetros Importantes

A regressão logística possui diversos **hiperparâmetros** que impactam diretamente sua performance e convergência:

### 🔹 `penalty`

Controla o tipo de **regularização** usada para evitar overfitting:
- `"l2"` (Ridge): penaliza grandes pesos, preferida na maioria dos casos.
- `"l1"` (Lasso): força alguns coeficientes a zero (sparse), útil para seleção de atributos.
- `"elasticnet"`: combinação entre L1 e L2.
- `"none"`: sem regularização (raro, e pode causar overfitting).

### 🔹 `C`

É o **inverso da força de regularização**.  
Valores menores de `C` significam **maior regularização**.  
Por exemplo:
- `C = 1.0` (valor padrão) é um bom ponto de partida.
- `C < 1` aumenta a penalização, o que reduz o risco de overfitting.
- `C > 1` reduz a penalização, permitindo ajustes mais livres dos pesos.

### 🔹 `solver`

Define o algoritmo usado para otimizar a função de custo:

| Solver      | Suporta L1? | Suporta L2? | Recomendado para: |
|-------------|-------------|-------------|--------------------|
| `liblinear` | ✅           | ✅           | Datasets pequenos, L1 ou L2 |
| `saga`      | ✅           | ✅           | Datasets grandes, elasticnet |
| `lbfgs`     | ❌           | ✅           | Multiclasse, datasets grandes |
| `newton-cg` | ❌           | ✅           | Multiclasse |
| `sag`       | ❌           | ✅           | Datasets grandes e esparsos |

> ⚠️ Importante: nem todos os solvers suportam todas as penalizações.

### 🔹 `max_iter`

Número máximo de iterações para convergência.  
Útil aumentar esse valor se o modelo estiver emitindo avisos de que **não convergiu**.

---

## 3. 📊 Avaliação do Modelo

Como a saída é uma probabilidade, a Regressão Logística permite avaliar bem a performance do modelo em tarefas de classificação, utilizando métricas como:

- **Acurácia**
- **Precisão / Recall**
- **F1-score**
- **Curva ROC e AUC**
- **Matriz de Confusão**

Além disso, o modelo é interpretável: os **coeficientes** indicam a importância (positiva ou negativa) de cada variável para a predição.
