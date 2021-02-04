# 04. Desvios Condicionais (if)

Nas aulas anteriores desenvolvemos programas que funcionam mais ou menos como uma linha de produção: uma série de comandos são executados um após o outro, sem opção de seguir por um caminho diferente. Você pode argumentar que o `#!python input()`, visto na aula passada, permite que o programa se comporte de formas diferentes dependendo do que o usuário digitar no teclado. Mas se olharmos o programa em si, **a sequência de operações executadas** é sempre a mesma. Na aula de hoje veremos como desenvolver programas que, dada uma condição, executam, ou não, um determinado bloco de código.

Suponha que queremos desenvolver uma função que recebe dois números, `#!python x` e `#!python y` como argumento e devolve 1 se `#!python x` for maior do que `#!python y` e 0, caso contrário. A não ser que exista uma fórmula fechada (existe, para alguns casos), precisamos de alguma forma de executar um trecho de código **somente se** `#!python x` for maior que `#!python y` e outro trecho de código **somente se** essa condição não for verdadeira. Nossa função deve fazer algo parecido com o seguinte:

<img src="raw/if/if.png" alt="Esquema da função que compara `x` e `y`" width="60%" />

Para isso vamos precisar do operador `#!python if`. Vamos começar com um exemplo curto para entender como ele funciona.

:::admonition{type=exercise title="EXERCÍCIO 1"}

Teste o seguinte programa:

::snip{file="raw/if/if_true.py"}

O que foi mostrado no terminal? A saída do terminal está de acordo com o que você esperava que acontecesse?

:::

## O operador `#!python if`

O operador `#!python if` funciona da seguinte maneira:

- No caso de `#!python if True:` o bloco do `#!python if` é executado;
- No caso de `#!python if False:` o bloco do `#!python if` não é executado.

**Importante:** o operador `#!python if` **sempre** deve ser procedido por um valor `#!python True` ou `#!python False`. Mas então, para que serve o `#!python if`? Ele parece bastante limitado... Para isso precisamos abrir mais um parênteses.

## Operadores relacionais

:::admonition{type=exercise title="EXERCÍCIO 2"}

Teste o programa a seguir:

::snip{file="raw/if/op_relacionais.py"}

:::

:::admonition{type=exercise title="EXERCÍCIO 3"}

Faça o exercício :challenge{type="trace" slug="operadores-relacionais"}.

Todas as expressões no código acima resultam em um valor booleano (`#!python True` ou `#!python False`). Vimos que o `#!python if` só pode ser seguido de um valor booleano. Como as expressões acima resultam em um valor booleano, elas também podem ser utilizadas com o `#!python if`!

:::

:::admonition{type=exercise title="EXERCÍCIO 4"}

Considere o programa a seguir. Antes de testar, discuta com um colega qual você espera que seja a saída no terminal. Depois disso, teste o programa e valide a sua hipótese.

::snip{file="raw/if/if_op_relacionais.py"}

:::

As expressões acima utilizam _operadores relacionais_ para comparar valores e o resultado dessas operações **sempre** é um valor booleano. A tabela a seguir resume os principais operadores relacionais:

| **Operador**  | **Operação**   |
| ------------- | -------------- |
| `#!python ==` | Igual          |
| `#!python !=` | Diferente      |
| `#!python >`  | Maior          |
| `#!python <`  | Menor          |
| `#!python >=` | Maior ou Igual |
| `#!python <=` | Menor ou Igual |

## Voltando para o problema inicial

Agora podemos voltar para o problema inicial: faça uma função que recebe dois números `#!python x` e `#!python y` e devolve 1, caso `#!python x` seja maior que `#!python y`, ou zero, caso contrário.

:::admonition{type=exercise title="EXERCÍCIO 5"}

Teste o programa a seguir:

::snip{file="raw/if/testa_x_y.py"}

Caso o programa acima não tenha funcionado, tente resolver o problema com a ajuda dos seus colegas. Se não conseguirem resolver, conversem com o professor.
:::

::::admonition{type=exercise title="EXERCÍCIO 6"}
Acrescente a seguinte linha ao final do programa acima: `#!python print(testa_x_y(5, 10))`. Teste o programa novamente.

:::admonition{type=danger title="Erro de variável não definida"}
Um erro semelhante a este deve ter ocorrido: `#!python UnboundLocalError: local variable 'resultado' referenced before assignment`. Ele indica que a variável `#!python resultado` foi referenciada antes de receber um valor. Antes de ler o próximo parágrafo, tente identificar por conta própria por que esse erro aconteceu.

Os valores `#!python 5` e `#!python 10` são recebidos pela função nas variáveis `#!python x` e `#!python y` respectivamente. Na linha seguinte, `#!python x > y` é avaliado como `#!python 5 > 10`, ou seja, `#!python False`. Nesse caso, o bloco do `#!python if` não é executado e a próxima linha é `#!python return resultado`, mas qual valor está guardado em `#!python resultado`? Como a variável `#!python resultado` não foi inicializada **nesta execução da função**, o erro `#!python UnboundLocalError` ocorre.
:::
::::

## E o "caso contrário"?

Para corrigir o erro na nossa função, vamos voltar à descrição do problema inicial: uma função que devolve 1 caso `#!python x` seja maior que `#!python y` ou zero, caso contrário. Precisamos tratar esse _"caso contrário"_. Para isso existe o operador `#!python else`, que significa, literalmente, _"caso contrário"_.

::::admonition{type=exercise title="EXERCÍCIO 7"}

Teste o programa a seguir:

::snip{file="raw/if/if_else.py"}

:::admonition{type=danger title="Atenção"}
Se você não sabe o que a primeira linha do código acima faz, revise o handout da aula passada antes de prosseguir.
:::

Faça alguns testes variando a entrada para verificar se o programa faz o que você espera. O operador `#!python else` captura todos os casos para os quais a condição do `#!python if` é falsa.

::::

## Agora vai!

:::admonition{type=exercise title="EXERCÍCIO 8"}
Agora sim, podemos terminar nossa função. Modifique a função do exercício 6 para que o programa volte a funcionar.
:::

## Encadeando condicionais

É possível testar uma nova condição caso a anterior falhe, utilizando o operador `#!python elif`. Ele pode ser lido como _"senão, se"_. Vamos trabalhar com um exemplo.

:::admonition{type=exercise title="EXERCÍCIO 9"}

Teste o programa a seguir:

::snip{file="raw/if/if_elif_else.py"}

O que deve acontecer se o número `#!python 0` for digitado? E o número `#!python 11`? E o número `#!python 10000`?
:::

:::admonition{type=exercise title="EXERCÍCIO 10"}
Se `#!python numero` for igual a zero, `#!python numero % 2 == 0` é `#!python True`. Discuta com algum colega e valide com o professor: por que quando o usuário digita o número zero o programa não imprime `#!python 0 é par`?
:::

:::admonition{type=exercise title="EXERCÍCIO 11"}
Discuta com um colega: por que podemos utilizar o `#!python else` para imprimir que o número é ímpar? Em outra palavras, por que não precisamos de um `#!python elif numero % 2 != 0:`?
:::

:::admonition{type=exercise title="EXERCÍCIO 12"}
Altere a função do exercício 8 para que ela devolva `#!python 1` se `#!python x` for maior do que `#!python y`, `#!python 0` se `#!python x` for igual a `#!python y` ou `#!python -1`, se `#!python x` for menor do que `#!python y`.
:::

## If's encadeados

Dentro do bloco de um `#!python if`, `#!python elif` ou `#!python else`, podemos ter qualquer código Python válido. Inclusive outros `#!python if`'s. Considere a função a seguir, que, dada a idade de uma pessoa, devolve uma string que indica em que países essa pessoa é considerada maior de idade.

::snip{file="raw/if/testa_maioridade.py"}

:::admonition{type=exercise title="EXERCÍCIO 13"}
Faça o teste de mesa no exercício :challenge{type="trace" slug="testa-maioridade"}.
:::

:::admonition{type=exercise title="EXERCÍCIO 14"}
Modifique a função acima para utilizar **exatamente** um `#!python if`, um `#!python elif` e um `#!python else`.
:::

## Operadores lógicos

## Operador `#!python and`

Nos exercícios anteriores vimos como testar uma única condição, mas em muitos casos pode ser útil testar mais do que uma condição de uma vez. Por exemplo, um arco-íris ocorre se _está chovendo_ **e** _fazendo sol_, simultaneamente. Ou seja:

::snip{file="raw/if/chuva_sol.py"}

:::admonition{type=exercise title="EXERCÍCIO 15"}
Teste o programa acima, modificando os valores de `#!python esta_chovendo` e `#!python faz_sol`. Existem 4 combinações possíveis. Teste todas e verifique se a saída no terminal corresponde ao que você esperava.
:::

## Operador `#!python or`

Em outros casos é suficiente que _pelo menos uma das condições for satisfeita_. Por exemplo: uma pessoa paga meia entrada no teatro se _for estudante_ **ou** _for idosa_. Ou seja:

::snip{file="raw/if/paga_meia.py"}

:::admonition{type=exercise title="EXERCÍCIO 16"}
Teste o programa acima, modificando os valores de `#!python estudante` e `#!python idoso`. Existem 4 combinações possíveis. Teste todas e verifique se a saída no terminal corresponde ao que você esperava.
:::

## Operador `#!python not`

Também existe a possibilidade de querermos considerar os casos em que uma condição é falsa. Por exemplo: sempre tomo sopa quando o dia não está quente.

::snip{file="raw/if/toma_sopa.py"}

:::admonition{type=exercise title="EXERCÍCIO 17"}
Teste o programa acima, modificando os valores de `#!python esta_quente`. Existem 2 possibilidades. Teste ambas e verifique se a saída no terminal corresponde ao que você esperava.
:::

### Resumindo

Vamos resumir o comportamento dos operadores `#!python and`, `#!python or` e `#!python not`:

- **`#!python and`**: devolve `#!python True` se **AMBOS** os valores forem verdadeiros;
- **`#!python or`**: devolve `#!python True` se **PELO MENOS UM** dos valores forem verdadeiros;
- **`#!python not`**: inverte de `#!python True` para `#!python False` e vice-versa.

::::admonition{type=exercise title="EXERCÍCIO 18"}

Faça uma função que recebe os lados de um triângulo e retorna se ele é equilátero, isósceles ou escaleno (se não sabe alguma dessas definições, procure na internet). Teste sua resposta no exercício :challenge{type="code" slug="classificador-de-triangulos"}.

Você pode implementar essa função de diversas maneiras diferentes. Implemente as seguintes versões e compare o código gerado para cada uma:

1. Teste se o triângulo é equilátero, depois se é isósceles e depois se é escaleno;
2. Teste se o triângulo é equilátero, depois se é escaleno e depois se é isósceles;
3. Teste se o triângulo é isósceles, depois se é equilátero e depois se é escaleno;

:::admonition{type=danger title="Erro comum"}

Assuma que as variáveis `#!python lado1`, `#!python lado2` e `#!python lado3` guardam as medidas dos lados do triângulo. Um erro comum neste exercício é tentar combinar duas comparações de maneira incompleta. Por exemplo, para verificar se um triângulo é isósceles:

`#!python if lado1 == lado2 and != lado3`

Apesar de ser razoável achar que esse código seria válido ele **não funciona**. Lembre-se que os operadores lógicos (`#!python and` e `#!python or`) combinam dois valores booleanos, portanto **cada lado do operador deve ser uma expressão completa**. Assim, o correto seria:

`#!python if lado1 == lado2 and lado1 != lado3`

:::

::::

### EXERCÍCIOS ADICIONAIS

Se acabar os exercícios propostos neste handout, resolva os [outros exercícios disponíveis](/if/challenges).
