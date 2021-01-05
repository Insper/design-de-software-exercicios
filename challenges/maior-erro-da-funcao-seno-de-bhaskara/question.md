Bhāskara foi um matemático indiano do século VII que desenvolveu uma fórmula simples para calcular o valor do seno aproximado de um número em graus. A fórmula é a seguinte:

$$\sin x = \frac{4x(180-x)}{40500 - x(180-x)}$$

Onde $x$ é um valor em graus e $0^o\leq x\leq 90^o$.

Desenvolva um programa que imprima o ponto de maior erro da função de Bhāskara. Para isso, para os valores de 0 a 90 graus, de um e um grau, analise a diferença da função de Bhāskara em relação a função `math.sin` do Python e diga qual é o valor em graus que o valor de seno apresenta a maior diferença entre ambas as técnicas. Você provavelmente vai querer usar a função `abs()`.

**Importante:** seu programa deve utilizar apenas um `print`.