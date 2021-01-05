Uma loja de livros usa uma tabela de cores para identificar o preço em Reais de cada livro. O seu catálogo de livros está armazenado em um dicionário em Python que indica a cor da tabela de preços de cada livro. Faça um função em Python que retorne o preço de um livro em Reais a partir de seu nome. Essa função deve receber uma string com o título de livro, um dicionário com os nome dos livros indicando a cor da tabela de preços e finalmente um dicionário das cores para os preços.

Por exemplo (atenção, os dicionários são apenas exemplos, sua função deve aceitar qualquer dicionário dentro das especificações):

Se a sua função receber os argumentos:

- título do livro: `"Dom Quixote"`
- dicionário de livros: `{"Pinóquio": "azul", "Dom Quixote": "amarelo", "O Pequeno Príncipe": "vermelho"}`
- tabela de cores: `{"vermelho": 10.0, "azul": 20.0, "amarelo": 40.0, "verde": 100.0 }`

Ela deve retornar `40.0`.

Para os mesmos dicionários e o livro `"Pinóquio"`, sua função deve retornar `20.0`.