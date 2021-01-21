# 05. Laços de Repetição (while)

O objetivo de aprendizado deste handout é que, ao final da atividade, você seja capaz de utilizar laços de repetição (não se preocupe, vamos explicar o que é isso) em seus programas em conjunto com as estruturas que vimos nas aulas anteriores (`#!python if`, `#!python input`, etc.) Para isso, vamos trabalhar com o exemplo de um jogo simples: o programa escolhe um número aleatório e o jogador precisa descobrir qual foi o número escolhido.

:::admonition{type=danger title="Importante"}
Sempre valide a resposta com o professor ou algum colega que já tenha validado a própria resposta **antes de seguir para o próximo exercício**.
:::

## Aquecimento

Para começar, vamos implementar uma versão do jogo na qual o jogador só tem uma chance para acertar (sim, completamente na sorte).

:::admonition{type=exercise title="EXERCÍCIO 1"}

Faça um programa que:

1. Sorteia um número aleatório entre `#!python 1` e `#!python 20` e guarda numa variável;
    - Use a função `#!python randint` da biblioteca `#!python random` (**dica**: procure a documentação na internet)
1. Pede ao jogador um número entre `#!python 1` e `#!python 20`
1. Dê o feedback da resposta do jogador:
    - Se o número digitado for menor que o número sorteado, escreva `#!python "Muito baixo"`;
    - Caso contrário, se o número digitado for maior que o número sorteado, escreva `#!python "Muito alto"`;
    - Caso contrário, escreva `#!python "Acertou"`.

:::

## Repetindo o `#!python if`

Vamos fazer uma breve reflexão. O que seria necessário alterar no código do exercício 1 para que o jogador tivesse 2 chances? Uma solução rápida seria copiar o bloco do `#!python if`, `#!python elif`, `#!python else` e colar no final do programa. Mas e se o jogador tivesse 5 chances? E 100? E se pudesse continuar tentando **enquanto não tivesse adivinhado o número**?

::::admonition{type=exercise title="EXERCÍCIO 2"}

O nosso jogo possui muitas condições, então, para introduzir o próximo conceito, vamos considerar um exemplo menor.

Faça um programa que pergunta ao aluno se ele tem dúvidas na disciplina. Se o aluno responder qualquer coisa diferente de `#!python 'não'`, escreva `#!python 'Pratique mais'`.

Uma possível solução para esse exercício pode ser encontrada em: [https://youtu.be/80jQUj6JmYY](https://youtu.be/80jQUj6JmYY). **Atenção**: consulte o vídeo somente depois de tentar resolver o exercício. **Compreender o vídeo não é garantia de que você sabe resolver o problema.** Caso você não tenha conseguido resolver o exercício, assista ao vídeo e depois tente novamente **sem consultar o vídeo novamente**.

:::admonition{type=info title="Resposta" collapse}
Seu código deveria ser similar a este:

::snip{file="raw/while/gabarito2.py"}
:::

::::

::::admonition{type=exercise title="EXERCÍCIO 3"}

Vamos preparar nosso código para que seja possível perguntar novamente se o aluno tem dúvidas caso ele já tenha respondido antes que sim. Adicione uma variável `#!python tem_duvidas` **logo no começo do programa**. *Inicialize* essa variável com (ou seja, faça ela receber inicialmente) o valor `#!python True`. Coloque todo o seu código original dentro de um `#!python if tem_duvidas:`.

Além disso, se o aluno responder `#!python 'não'`, mude o valor da variável `#!python tem_duvidas` para `#!python False`, pois o aluno não tem mais dúvidas.

:::admonition{type=danger}
Essa modificação **não deve alterar** o comportamento do seu programa. Teste-o para garantir que ainda está funcionando. Note que, como inicialmente `#!python tem_duvidas = True`, o programa **sempre vai entrar no `#!python if`**.
:::

Antes de prosseguir, compare o seu código com a resposta abaixo. Para os próximos passos fazerem sentido **é importante que o seu código siga a mesma estrutura.**

:::admonition{type=info title="Resposta" collapse}
Com a modificação acima seu código deve ficar semelhante a:

::snip{file="raw/while/gabarito3.py"}

:::

::::

Considere a seguinte versão modificada do seu programa:

::snip{file="raw/while/tem_duvidas2.py"}

Existem duas possibilidades:

- Se o usuário responder `#!python 'não'` na primeira vez, a variável `#!python tem_duvidas` será atualizada com `#!python False`. Assim, o bloco do segundo `#!python if tem_duvidas` **não será executado**.
- Se o usuário responder qualquer coisa diferente de `#!python 'não'`, a variável `#!python tem_duvidas` continuará valendo `#!python True`. Assim, o bloco do segundo `#!python if tem_duvidas` **será executado** e o programa perguntará novamente se o aluno tem dúvidas.

::::admonition{type=exercise title="EXERCÍCIO 4"}

Modifique o programa acima para que o aluno tenha 5 chances para responder que não tem mais dúvidas. Depois disso, **mesmo que ele ainda tenha dúvidas**, escreva `#!python 'Até a próxima'`. **Dica**: a ideia deste exercício é copiar e colar código e adicionar um `#!python print` no fim. Se você fez algo além disso, provavelmente não é o que estávamos esperando neste ponto.

:::admonition{type=info title="Resposta" collapse}
Com a modificação acima seu código deve ficar semelhante a:

::snip{file="raw/while/gabarito4.py"}
:::

::::

## O operador `#!python while`

Se quiséssemos repetir a pergunta mais 100 vezes, poderíamos continuar copiando e colando o código. Um problema é que o código ficaria cada vez mais difícil de manter. Imagine que você decidiu aceitar a resposta `#!python 'não tenho'` ao invés de somente `#!python 'não'`. Agora você teria pelo menos 100 linhas diferentes para alterar no seu código.

Ok, é chato e pode dar bastante trabalho, mas ainda dá para fazer. Agora, o que precisaríamos fazer para que o programa **continuasse perguntando enquanto o usuário não respondesse "não"**. Se copiássemos o mesmo bloco de código 1000 vezes ele poderia responder `#!python 'sim'` nas 1001 primeiras vezes. Se fizéssemos o mesmo 100000 de vezes, o usuário ainda poderia (por mais que improvável) responder `#!python 'sim'` nas 100001 primeiras vezes. Assim, vemos que é necessário utilizar alguma outra estrutura, no caso, o operador `#!python while`. Vamos começar relembrando o que o `#!python if` faz:

<img src="raw/while/if.png" alt="O `if` executa o bloco se a condição for verdadeira" width="50%">

O `#!python while` funciona de maneira similar, mas ao final da execução do bloco, **a condição é reavaliada** e, caso seja verdadeira, o bloco é executado novamente **enquanto a condição for verdadeira**:

<img src="raw/while/while.png" alt="O `while` executa o bloco enquanto a condição for verdadeira" width="50%">

:::admonition{type=exercise title="EXERCÍCIO 5"}
Modifique o programa do [exercício 3](#exercicio-3) para que ele continue perguntando se o usuário tem dúvidas enquanto ele responder qualquer coisa diferente de `#!python 'não'`. **Dica**: basta trocar um dos `#!python if`s por um `#!python while`.
:::

:::admonition{type=exercise title="EXERCÍCIO 6"}
Faça o exercício :challenge{type=trace slug=aluno-com-duvidas}.

O vídeo a seguir apresenta uma possível solução para o exercício anterior e explica o conceito de `#!python while`: [https://youtu.be/vNspAsXabxY](https://youtu.be/vNspAsXabxY).
:::

:::admonition{type=exercise title="EXERCÍCIO 7"}

Agora podemos voltar para o nosso jogo. Modifique o seu programa do [exercício 1](#exercicio-1) para que o jogador possa continuar chutando um valor enquanto o usuário não acertar. Em outras palavras, modifique o programa para que o jogador tenha tentativas infinitas.

O vídeo a seguir apresenta algumas possíveis soluções: [https://youtu.be/Z-N5kzXHHO0](https://youtu.be/Z-N5kzXHHO0). Novamente, **consulte o vídeo somente depois de tentar resolver o exercício por conta própria**.

:::

## Alguns padrões de uso do `#!python while`

Vamos trabalhar agora com alguns padrões comuns de uso do `#!python while`. Procure entender a lógica dos programas a seguir. De modo geral sempre será necessário adaptar o padrão para a sua aplicação específica.

:::admonition{type=exercise title="EXERCÍCIO 8"}
Faça o exercício :challenge{type=trace slug=padroes-de-uso-do-while-contagem}.
:::

### Padrões de uso do `#!python while`: contagem

Podemos utilizar o `#!python while` para fazer contagens. No exemplo do exercício anterior, nós contamos quantas vezes o bloco do `#!python while` é executado (lembrando que em programação começamos a contar do 0). Essa informação é armazenada na variável `#!python contador`.

Você pode usar qualquer nome de variável para o contador. No nosso exemplo nós utilizamos `#!python contador` para deixar o seu objetivo explícito. Entretanto, o uso de contadores é tão comum, que é normal encontrar variáveis que servem como contadores com nomes curtos, como `#!python i` ou `#!python j`. Independentemente do nome da variável, um contador é uma variável utilizada para guardar o resultado da contagem.

:::admonition{type=exercise title="EXERCÍCIO 9"}

Modifique o código do [exercício 7](#exercicio-7) para mostrar ao final do jogo a quantidade de tentativas do jogador até ele descobrir o número correto.

O vídeo a seguir explica o padrão de uso do `#!python while` com contadores e apresenta uma possível solução para este exercício: [https://youtu.be/wBjnd2RaJKE](https://youtu.be/wBjnd2RaJKE). Como sempre, **consulte somente depois de tentar resolver o exercício**.

:::

:::admonition{type=exercise title="EXERCÍCIO 10"}
Faça o exercício :challenge{type=trace slug=padroes-de-uso-do-while-validacao}.
:::

### Padrões de uso do `#!python while`: validação

No exercício 8 temos um exemplo de como usar o `#!python while` para validar uma entrada. Nesse caso, o programa vai ficar "preso" no `#!python while` até que o usuário digite um número válido (no exemplo, um número par).

:::admonition{type=exercise title="EXERCÍCIO 11"}

Modifique o jogo de adivinha ([exercício 9](#exercicio-9)) para validar que a entrada do usuário é um número inteiro entre 1 e 20 (inclusive). Ou seja, antes de verificar se o jogador acertou o número é necessário validar a entrada. **Entradas inválidas não devem ser contabilizadas**.

Para uma possível solução, consulte o vídeo a seguir: [https://youtu.be/5IQDVYPi9As](https://youtu.be/5IQDVYPi9As).

:::

:::admonition{type=exercise title="EXERCÍCIO 12"}

Modifique o jogo de adivinha para que ele tenha no máximo cinco tentativas. Caso o jogo termine por exceder o limite de tentativas, uma mensagem adequada deve ser impressa (e.g. `#!python 'Que pena, você perdeu!'`).

Uma solução é apresentada em: [https://youtu.be/GfsmrVnLdws](https://youtu.be/GfsmrVnLdws)

:::

:::admonition{type=exercise title="QUALIDADE DE CÓDIGO"}
Assista o vídeo a seguir com uma discussão sobre a qualidade do código: [https://youtu.be/XCb8jSUcfsc](https://youtu.be/XCb8jSUcfsc).
:::

:::admonition{type=exercise title="EXERCÍCIOS ADICIONAIS"}
Como sempre, se acabar os exercícios deste handout, continue praticando com [os exercícios disponíveis](/while/challenges).
:::
