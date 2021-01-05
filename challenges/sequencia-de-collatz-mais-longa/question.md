Considere a seguinte sequência iterativa definida para os números inteiros positivos:

$$
\begin{align}
n &\rightarrow n/2 (n\text{ é par}) \\\\
n & \rightarrow 3n+1 (n\text{ é ímpar})
\end{align}
$$

Usando a regra acima e começando com o número 13, geramos a seguinte sequência:

$$ 13 \rightarrow 40 \rightarrow 20 \rightarrow 10 \rightarrow 5 \rightarrow 16 \rightarrow 8 \rightarrow 4 \rightarrow 2 \rightarrow 1 $$

Percebe-se que essa sequência (começando em 13 e terminando em 1) contém 10 termos. Apesar de ainda não ter sido provado (Problema de Collatz), acredita-se que a sequência sempre termina em 1, independentemente do número inicial.

Faça um programa que determina qual número positivo inicial menor que 1000 gera a sequência de Collatz mais longa. Seu programa deve imprimir esse número.

**Nota:** Uma vez que a sequência começa os números podem passar de 1000.

Adaptado de [https://projecteuler.net/problem=14](https://projecteuler.net/problem=14)