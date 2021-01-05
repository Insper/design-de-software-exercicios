**Este exercício caiu na avaliação final de Design de Software 2019-2**

Sua empresa possui filiais em diversas regiões da cidade e você precisa fazer uma análise simples dos gastos com infraestrutura em cada bairro. Os gastos com infraestrutura nos últimos 12 meses para cada bairro estão disponíveis em um dicionário como o apresentado a seguir (atenção, este é somente um exemplo):

```python
{
    'Bairro 1': [1234.45, 5123.32, 6134.35, 8567.98, 5472.28, 9715.38, 1380.15, 2569.42, 8459.24, 8351.25, 4082.19, 1750.16],
    'Bairro 2': [236.62, 845.52, 475.72, 846.22, 735.34, 846.26, 48.97, 624.37, 375.46, 4568.76, 73.32, 475.74],
    'Bairro 3': [51234.45, 5123.32, 61334.35, 8567.98, 5472.28, 9715.38, 1380.15, 2569.42, 8459.24, 82351.25, 4082.19, 1750.16],
}
```

Nesse dicionário, as chaves são os nomes dos bairros e os valores são listas com exatamente 12 números, representando o gasto com infraestrutura em cada mês para o respectivo bairro.

Faça uma função que recebe um dicionário de gastos com infraestrutura, como o descrito acima, e retorna um novo dicionário com o gasto total com infraestrutura nos últimos 6 meses para cada bairro. Nesse dicionário, as chaves são os nomes dos bairros e os valores são números, representando o gasto total dos últimos 6 meses naquele bairro.