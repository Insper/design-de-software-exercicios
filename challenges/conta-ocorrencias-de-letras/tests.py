'''
Faça uma função que recebe uma string e retorna um dicionário onde cada chave é uma letra da string, e cada valor é o número de ocorrências desta letra. Por exemplo, se passamos a string `"banana nanica"`, a função devolve o dicionário:

```python
{'b': 1, 'a': 5, 'n': 4, ' ': 1, 'i': 1, 'c': 1}
```

**Nota importante:** em geral as chaves do dicionário não estão ordenadas!

Sua função deve se chamar conta_letras
'''

from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    def test_1(self):
        entradas = ['banana nanica', 'abacaxi e abacate com banana', '', 'a']
        esperados = [
            {
                ' ': 1,
                'a': 5,
                'b': 1,
                'c': 1,
                'i': 1,
                'n': 4
            },
            {
                ' ': 4,
                'a': 9,
                'b': 3,
                'c': 3,
                'e': 2,
                'i': 1,
                'm': 1,
                'n': 2,
                'o': 1,
                't': 1,
                'x': 1,
            },
            {},
            {
                'a': 1
            },
        ]
        for entrada, esperado in zip(entradas, esperados):
            obtido = self.function(entrada)
            self.assertEqual(
                esperado, obtido,
                'Não funcionou para a entrada {0}. Esperado: {1}. Obtido: {2}.'
                .format(entrada, esperado, obtido))
