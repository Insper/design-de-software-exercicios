# 02. Código reutilizável com funções

<span id="f-mat"></span>

Já vimos como criar valores numéricos e de texto puro em Python (chamados em Python de "literais") e variáveis. Tudo isso parece muito com a boa e velha matemática. E já que estamos vendo todas essas relações, um outro conceito importante em matemática são funções. Por exemplo:

$$f(x) = 1.60934\cdot x$$

Essa função converte valores em milhas ($x$) para quilômetros. Por exemplo: $f(10) = 1.60934\cdot 10 = 16.0934$, ou seja, 10 milhas é o mesmo que 16.0934 km.

O Python também nos permite criar funções! Escrevendo a mesma função acima em Python:

::snip{file="raw/funcao/funcoes_def.py" showLineNumbers id="f-python"}

Novamente temos muitas observações importantes. Vamos começar pelos nomes:

- O `#!python x` na linha 1 é chamado de **argumento** da função.
- O `#!python y` na linha 3 é chamado de **retorno** ou **resultado** da função.
- As linhas 2 e 3 são chamadas de **corpo** ou **bloco** da função.
- O corpo da função é identificado com os 4 espaços no começo da linha. Esses 4 espaços são chamados de **indentação**.

:::admonition{type="info" title="Indentação"}
A indentação é crucial e Python e tem um significado especial. Ela é utilizada para indicar blocos de código. Portanto não se deve utilizar indentações a mais ou a menos, pois isso causará um erro na execução do programa.

O uso de 4 espaços é outra padronização da comunidade Python. Se você usar 2, 3 ou qualquer outra quantidade de espaços (ou até mesmo o caractere `tab`) o código funcionará da mesma forma. Desde que seja consistente, ou seja, escolha um formato e utilize-o em todo o seu programa. Recomendamos que você utilize 4 espaços para seguir o padrão da comunidade.
:::

Se você executar o código acima não vai acontecer nada. Nesse código nós estamos apenas **definindo** a função `#!python f` (por isso a palavra `#!python def`). Podemos entender a linha 1 como: "Python, **quando** eu pedir para você executar a função `#!python f`, passando um valor para `#!python x`, o que você deve fazer é: multiplicar o valor armazenado na variável `#!python x` por 1.60934 e guardar o resultado na variável `#!python y` e depois devolver o valor armazenado na variável `#!python y` como o resultado". Em outras palavras, é como se estivéssemos **criando um novo comando do Python** (assim como já temos o `#!python print`, por exemplo).

## Chamando funções em Python

Considere novamente a função matemática $f(x)$ [vista acima](#f-mat). Note que não existe um valor, ou resultado, para $f(x)$ a não ser que você defina quanto vale o $x$. Da mesma forma, não existe um resultado, ou valor de retorno, para a função [`#!python f(x)` no Python](#f-python) a não ser que definamos um valor para `#!python x`.

Essa ideia é a mesma que [apresentamos sobre a função `#!python print`](#print-arg), ou seja, precisamos de uma informação adicional. Uma vez que definimos uma função é como se ela se tornasse parte da linguagem Python. Assim, para esse contexto introdutório, não existe nenhuma diferença entre a função `#!python print` e a função `#!python f(x)` em termos de importância. Ambas são comandos disponíveis no Python para o programador utilizar em seu código.

Vamos então ver um exemplo de uso da nossa função `#!python f(x)`. Considere o código a seguir:

::snip{file="raw/funcao/funcoes.py" id="f-programa" showLineNumbers}

Nas linhas 1 a 3 a função `#!python f(x)` é definida, ou seja, após a execução dessas linhas o Python sabe o que fazer sempre que precisarmos dessa função. Na linha 5, armazenamos o número 10 na variável `#!python a`. Na linha 6 ocorre a chamada da função. Vamos detalhar o que ocorre nessa linha:

- O valor da variável `#!python a` é utilizado, o Python consulta esse valor na memória e substitui na chamada da função. Agora a linha é equivalente a `#!python b = f(10)`.
- A função `#!python f()` é executada com o argumento `#!python 10`.
- A próxima linha executada é a linha 1.
- O Python cria uma nova região temporária na memória. Essa memória só existirá enquanto a função estiver sendo executada.
- Na linha 1 é criada uma variável chamada `#!python x` nessa memória temporária, armazenando o valor recebido como argumento, no caso `#!python 10`.
- Na linha 2 o valor `#!python x` é substituído por `#!python 10` e o valor `#!python 16.0934` (resultado da multiplicação) é armazenado na variável `#!python y`, também na memória temporária.
- Na linha 3 o valor guardado na variável `#!python y` é devolvido como resultado.
- A memória temporária criada para a função `#!python f()` é desativada. A partir deste momento as variáveis que estavam contidas nela (`#!python x` e `#!python y`) não existem mais.
- Voltamos para a linha 6.
- Agora que temos o resultado da função a linha é equivalente a `#!python b = 16.0934`.
- O valor `#!python 16.0934` é armazenado na variável `#!python b`

Por fim, na linha 7, o valor armazenado na variável `#!python b` é utilizado como argumento da função `#!python print()` e o valor `#!python 16.0934` é mostrado no terminal.

:::admonition{type=exercise title="EXERCÍCIO 1"}
Faça o exercício :challenge{type="trace" slug="converte-milhas-para-km"} para consolidar a sua compreensão sobre funções em Python.
:::

:::admonition{type="info" title="Dica Pro: use bons nomes!"}
No dia seguinte você abre [esse programa](#f-programa). O que faz mesmo esse código? Acredite, é mais comum do que você imagina. Enquanto estamos desenvolvendo o programa temos muito claro para quê cada variável serve, mas não precisamos de muito tempo para olhar o mesmo código e não ter ideia do que está acontecendo.

Por isso, use nomes que façam sentido para as suas variáveis e funções. Quando não estiver claro o suficiente, adicione comentários, mas as vezes boas escolhas de nomes dispensam comentários no código. Considere a versão a seguir (ela faz exatamente o mesmo que o nosso código anterior):

::snip{file="raw/funcao/funcoes2.py" showLineNumbers}

Neste exemplo os comentários poderiam até ser removidos, pois o nome da função já deixa claro o que ela faz.

:::

:::admonition{type=exercise title="EXERCÍCIO 2"}
Faça o exercício :challenge{type="code" slug="celsius-para-fahrenheit"}.

Primeiro resolva em seu próprio computador, fazendo testes com alguns valores específicos (ex: 0 e 100). Depois disso, envie apenas a definição da função, sem o código que chama a função. Por exemplo, no [programa que desenvolvemos acima](#f-programa), você enviaria apenas as linhas 1 a 3.

**Sempre que o exercício do servidor pedir uma função você deve enviar apenas a definição da função, sem o código de teste que chama a função.**
:::

:::admonition{type=exercise title="EXERCÍCIO 3"}
Faça o exercício :challenge{type="code" slug="area-do-triangulo"}.

Dica: uma função em Python, assim como uma função matemática multivariada, pode receber vários argumentos separados por vírgula.

Não esqueça de escrever código de teste também. Pense em valores de teste que sejam interessantes. Por exemplo: e se a base for zero? E se a altura for zero? E se forem iguais?
:::
