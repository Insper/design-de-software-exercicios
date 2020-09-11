# Exercícios de Design de Software

Estes são os exercícios do servidor de Design de Software.

## Setup

Para utilizar o código deste repositório, siga as instruções a seguir:

Crie um ambiente virtual do Python:

    $ python3 -m venv env

Ative o ambiente virtual (**você deve fazer isso sempre que for executar algum script deste repositório**). No Windows:

    $ env\Scripts\activate

No Linux/MacOS:

    $ . env/bin/activate

Instale as dependências com:

    $ pip install -r requirements.txt

# Script de administração

O script `admin.py` contém comandos para gerenciamento dos exercícios.

## Criação de novos exercícios

Um exercício é definido por uma pasta em `exercicios` contendo os seguintes arquivos:

- `detalhes.json`: arquivo com as informações do exercício (veja mais detalhes [abaixo](#arquivo-de-detalhes));
- `enunciado.md`: arquivo Markdown com o enunciado do exercício - note que o título do exercício será extraído do arquivo `detalhes.json` então não deve ser repetido neste arquivo;
- `errado*.py`: arquivos com soluções incorretas - deve existir pelo menos um;
- `solucao*.py`: arquivos com soluções corretas - deve existir pelo menos um;
- `testes.py`: arquivo com os testes do exercício - deve utilizar o módulo [`strtest`](https://github.com/Insper/python-string-test-runner);
- `img.*`: arquivo opcional contendo uma imagem para ser mostrada após o enunciado (pode ser qualquer formato que abra no browser).

### Arquivo de detalhes

O arquivo `detalhes.json` é um arquivo JSON que contém um dicionário com os seguintes valores:

- `"titulo"`: string com o título do exercício;
- `"publicado"`: `true` ou `false` indicando se o exercício está disponível para os alunos ou não;
- `"terminal"`: `true` ou `false` indicando se a saída do terminal (`print` e `input`) devem ser mostradas ao usuário;
- `"nome_funcao"`: string com o nome da função a ser testada - usar `null` ou omitir se for testar o programa;
- `"tags"`: string com as tags separadas por vírgula (as tags válidas estão no arquivo `tags.txt`).

### Gerando a pasta de exercício

Você pode utilizar o comando a seguir para criar a pasta de um novo exercício com os esqueletos dos arquivos necessários:

    $ python admin.py novo SLUG

Onde `SLUG` é um identificador único para o nome do exercício. As palavras devem ser separadas por traços. Esse nome será utilizado para gerar a URL do exercício no servidor (o fato de ser uma pasta já garante a unicidade).

## Validação dos exercícios

O validador de exercícios verifica a consistência dos dados de um exercício:

- Existência dos arquivos necessários
- Execução dos testes com os exemplos de solução correta e incorreta

Para validar todos os exercícios utilize o comando:

    $ python admin.py teste

Para validar um exercício específico utilize o comando:

    $ python admin.py teste NOME-DO-EXERCICIO

Onde `NOME-DO-EXERCICIO` é o nome da pasta do exercício a ser testado.
