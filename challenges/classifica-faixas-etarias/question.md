Faça uma função que recebe um dicionário no qual as chaves são nomes de pessoas (representados por strings) e os valores são as idades de cada pessoa e retorna um novo dicionário no qual as chaves são faixas etárias e os valores são listas com os nomes das pessoas daquela faixa. Utilize a seguinte classificação:

| Faixa etária |        Idade       |
|:------------|------------------:|
| criança      | 11 anos ou menos   |
| adolescente  | Entre 12 e 17 anos |
| adulto       | Entre 18 e 59 anos |
| idoso        | 60 anos ou mais    |

### Exemplo:

Para o dicionário `{'João': 10, 'Maria': 8, 'Miguel': 20, 'Helena': 67, 'Alice': 50}` sua função deve retornar `{'criança': ['João', 'Maria'], 'adolescente': [], 'adulto': ['Miguel', 'Alice'], 'idoso': ['Helena']}`.