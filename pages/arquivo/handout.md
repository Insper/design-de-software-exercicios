# 09 - Arquivos

:::admonition{type=info}

Os testes deste handout utilizam arquivos externos. Por esse motivo, não faz muito sentido fazermos testes de mesa no servidor. A melhor maneira de entender o que o programa está fazendo é executá-lo no próprio computador para observar as mudanças nos outros arquivos. Assim, neste handout não teremos testes de mesa do servidor. Faça todos os testes no seu próprio computador.

:::

Nossos programas até o momento utilizam dados fornecidos pelo usuário ou obtidos a partir de algum cálculo, mas esses dados são perdidos assim que o programa acaba. Arquivos são estruturas de dados que normalmente são armazenados em dispositivos secundários de memória. Esses dispositivos secundários de memória permitem o armazenamento permanente dos dados, ou seja, mesmo depois que o programa acaba ou até depois que o computador é reiniciado, os dados continuam existindo. Os principais dispositivos de armazenamento atualmente são:

- Disco Rígido (HD)
- Solid-State Drive (SSD)
- Pen Drives

Os arquivos armazenados nestes dispositivos possuem sempre uma **identificação (nome)** e sua **localização** (normalmente em uma estrutura hierárquica de diretórios). Outros atributos como data e permissões de acesso também são normalmente usados no índice.

## Acessando arquivos

Arquivos são lidos como uma sequência de bytes. Um byte é um conjunto de 8 bits (<b>BI</b>nary digi<b>T</b>), que são valores do tipo 0 ou 1. Bytes por si só não possuem significado nenhum, são simplesmente uma sequência de 0s e 1s. É necessário que um programa seja capaz de entender essa sequência de bytes do arquivo para extrair alguma informação.

Existem basicamente dois tipos de arquivos:

- **Arquivos de texto**: os bytes representam caracteres. Por exemplo, os arquivos `#!python .py` que criamos com o nosso código Python são arquivos de texto. Cada caractere do nosso código Python (incluindo espaços e pula linha) é representado por um byte e armazenado no nosso HD ou SSD.
- **Arquivos binários**: cada byte pode ter um significado diferente. Por exemplo, em imagens é comum usar bytes para representar cores. No exemplo abaixo, os bytes do arquivo (à direita) são interpretados por um programa que é capaz de mostrar o resultado como uma imagem (à esquerda)

<img src="raw/arquivo/arquivo-binario.png" width="50%" />

Neste handout vamos aprender a trabalhar com arquivos em Python. Ao final do handout você deve ser capaz de abrir um arquivo para (1) ler os dados armazenados; ou (2) escrever dados.

## Arquivos em Python

Antes de utilizar qualquer arquivo é necessário abri-lo. Para isso, existe a função `#!python open()`, que recebe pelo menos dois argumentos: a localização do arquivo e o modo de abertura. Depois de utilizar o arquivo é **muito importante** lembrar de fechá-lo. [Muitos problemas podem acontecer se você esquecer de fechar o programa](https://www.myinstants.com/instant/tan-tan-tan/). Para isso devemos usar a função `#!python close()`:

```python
# Modo tradicional de ler um arquivo
arquivo = open('arquivo_texto.txt', 'r')
conteudo = arquivo.read()
arquivo.close() # O que acontece se não fechar?

# Imprime o conteúdo
print(conteudo)

```

O programa acima abre um arquivo chamado `#!python arquivo_texto.txt` para leitura (**importante**: ele deve existir na mesma pasta onde você está executando o seu programa), armazena o conteúdo na variável `#!python conteudo`, fecha o arquivo e depois imprime todo o conteúdo do arquivo.

:::admonition{type=exercise title="EXERCÍCIO 1"}

Teste o programa acima no seu computador. Para isso, crie um arquivo chamado `#!python arquivo_texto.txt` e escreva alguma coisa (pode ser no Spyder, VS Code, ou qualquer editor de texto de sua preferência - **não use o Word, pois ele gera um arquivo muito mais complicado**). Salve o programa acima **na mesma pasta**. Execute seu programa. Ele deve imprimir no terminal o conteúdo do seu arquivo.

:::

:::admonition{type=danger title="Caminho (*path*) do arquivo"}

Quando estamos trabalhando com arquivos é comum obtermos o erro `#!python FileNotFoundError`. Ele ocorre quando tentamos abrir (`#!python open()`) um arquivo que não existe. É importante que o arquivo que você está tentando abrir esteja na mesma pasta que contém o seu programa.

É possível abrir arquivos localizados em outras pastas do seu computador, mas nesse caso é necessário especificar o caminho do arquivo, ou seja, qual é a sequência de pastas que devem ser percorridas para se localizar esse arquivo.

:::

### Abrindo arquivos com o `#!python with`

Como dissemos anteriormente, é muito importante se lembrar de fechar o arquivo depois de utilizá-lo. Na verdade, isso é tão importante que existe uma maneira de escrevermos um código que fecha o arquivo automaticamente depois que terminamos de utilizá-lo:

::snip{file=raw/arquivo/with_open.py}

A sintaxe do código acima é um pouco diferente, então vamos por partes. O `#!python with` define um bloco dentro do qual o arquivo será utilizado. Assim que o bloco termina, o que é indicado pelo fim da indentação, o arquivo será automaticamente fechado. A função `#!python open()` não foi alterada, mas agora ao invés de `#!python arquivo = open('arquivo_texto.txt', 'r')` nós temos `#!python open('arquivo_texto.txt', 'r') as arquivo`. O resultado será o mesmo: o arquivo aberto será armazenado na variável `#!python arquivo`. Essa inversão da ordem é feita apenas em conjunto com o `#!python with`.

:::admonition{type=exercise title="EXERCÍCIO 2"}

Teste a versão do programa acima. O resultado deve ser o mesmo da primeira versão.

:::

### Modos de abertura de um arquivo

Comentamos que existem dois tipos de arquivo: arquivos binários e arquivos de texto. Nos exemplos acima nós trabalhamos com a leitura de um arquivo de texto. Para isso o modo de abertura do arquivo foi o `#!python 'r'`, ou seja, leitura (*read*). Para abrir um arquivo binário para leitura devemos utilizar o modo `#!python 'rb'` (*read binary*). Tanto o modo `#!python 'r'` quanto o modo `#!python 'rb'` permitem apenas a leitura de um arquivo existente. Não é possível adicionar (escrever) nenhuma informação a ele.

Para adicionar dados a um arquivo devemos abri-lo com algum dos modos de **escrita**. Os modos disponíveis são `#!python 'w'` e `#!python 'a'`. O modo `#!python 'w'` cria um novo arquivo no modo escrita (**write**). **Importante:** se já existir um arquivo com o mesmo nome ele apaga o antigo. O modo `#!python 'a'` (*append*) é um modo de escrita alternativo que adiciona o novo conteúdo ao final do arquivo se ele já existir, sem apagar o conteúdo anterior. Exemplos:

::snip{file=raw/arquivo/open_wa.py}

A seguir apresentamos um resumo dos principais modos de abertura de arquivos (para mais detalhes consulte [a documentação](https://docs.python.org/3/library/functions.html#open)):

- **`'r'`**: modo de leitura de arquivo texto;
- **`'rb'`**: modo de leitura de arquivo binário;
- **`'w'`**: modo de escrita de arquivo texto;
- **`'wb'`**: modo de escrita de arquivo binário;
- **`'a'`**: modo de escrita de arquivo texto, sem apagar o conteúdo anterior;
- **`'ab'`**: modo de escrita de arquivo binário, sem apagar o conteúdo anterior.

:::admonition{type=exercise title="EXERCÍCIO 3"}

Teste o programa acima no seu computador. Ele não vai imprimir nada no terminal, mas ao abrir o arquivo `#!python arquivo_texto.txt` o seu conteúdo deve ser:

```
algum dado
novo dado

```

Se trocássemos a ordem dos blocos `#!python with` do programa acima, qual seria o efeito esperado? Teste essa mudança e verifique se ele fez o que você esperava.

:::

:::admonition{type=exercise title="EXERCÍCIO 4"}

Salve o arquivo [`#!python cancao_do_exilio.txt` (disponível neste link)](raw/arquivo/cancao_do_exilio.txt) na mesma pasta onde você fez os outros testes deste handout. Depois disso, teste cada um dos programas abaixo:

#### Programa 1

::snip{file=raw/arquivo/cancao_exilio1.py}

#### Programa 2

::snip{file=raw/arquivo/cancao_exilio2.py}

#### Programa 3

::snip{file=raw/arquivo/cancao_exilio3.py}

Note que no último exemplo as linhas aparecerão sempre com uma linha em branco entre si. Isso acontece porque no arquivo original cada linha termina em um `#!python '\n'`, que indica que a linha terminou, mas o print também pula uma linha automaticamente, então sempre serão puladas duas linhas.

:::

### Resumo dos métodos de arquivos:

Abaixo você encontra um resumo dos principais métodos de arquivos. Para mais detalhes, consulte [a documentação](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files).

#### Para arquivos abertos no modo de leitura

- **`read`**: retorna todo o conteúdo do arquivo em uma única string;
- **`readline`**: retorna uma string contendo apenas a próxima linha;
- **`readlines`**: retorna uma lista de strings, contendo uma string para cada linha.

#### Para arquivos abertos no modo de escrita

- **`write`**: escreve no arquivo a string passada como argumento;
- **`writelines`**: recebe uma lista de strings e escreve todas no arquivo.

:::admonition{type=exercise title="EXERCÍCIO 5"}

Faça o [Exercício 158. Conta palavras no arquivo](http://softdes.insper.edu.br/exercicio/158).

:::

:::admonition{type=exercise title="EXERCÍCIO 6"}

Faça o [Exercício 85. Bananas no arquivo](http://softdes.insper.edu.br/exercicio/85).

:::

:::admonition{type=exercise title="EXERCÍCIO 7"}

Faça o [Exercício 86. CSV para TSV](http://softdes.insper.edu.br/exercicio/86).

:::

:::admonition{type=exercise title="EXERCÍCIO 8"}

Faça o [Exercício 87. Custo do churrasco](http://softdes.insper.edu.br/exercicio/87).

:::

## O formato JSON

O formato JSON é uma forma de trocar informação de modo estruturado, simples e rápido entre sistemas. Ele é muito parecido com um dicionário do Python, contudo o JSON é um texto (string) e não uma estrutura de dados. Por ser um texto, ele pode ser armazenado em um arquivo. Assim esses dados continuam existindo, mesmo depois que o programa termina. Exemplo:

```
{"Alunos":[
     { "nome": "João", "notas": [ 8, 9, 5 ]  },
     { "nome": "Maria", "notas": [ 8, 10, 7 ] },
     { "nome": "José", "notas": [ 10, 10, 9 ] }
]}
```

O JSON acima contém os nomes e notas de 3 alunos. Esse poderia ser o conteúdo de um arquivo de texto chamado, por exemplo, `#!python alunos.json`. Para utilizar os dados presentes nele será necessário processar a string JSON para obter um dicionário. Para isso utilizamos o módulo `#!python json` do Python:

::snip{file=raw/arquivo/exemplo_json.py}

:::admonition{type=exercise title="EXERCÍCIO 9"}

Baixe o arquivo [`alunos.json`](raw/arquivo/alunos.json) disponível [neste link](raw/arquivo/alunos.json). Salve-o na mesma pasta onde você está fazendo os testes deste handout. Abra o arquivo no Spyder, VS Code ou seu editor de texto favorito. Crie um novo arquivo chamado `testa_json.py` e copie o código do programa acima. Teste-o e verifique o conteúdo do arquivo `alunos.json`.

:::

:::admonition{type=exercise title="EXERCÍCIO 10"}

Faça o [Exercício 159. Valor total do estoque](http://softdes.insper.edu.br/exercicio/159).

:::
