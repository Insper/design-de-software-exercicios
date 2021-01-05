'''
Faça uma função que recebe uma lista de palavras e retorna a palavra mais frequente. Por exemplo, para a lista

```python
['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu’]
```

sua função deve retornar 'abobora'.

**Dica**: se você não resolveu o exercício [146. Conta ocorrências de palavras](/exercicio/146), resolva-o primeiro e utilize-o como função auxiliar para este exercício (cole o código nesta solução).

Sua função deve se chamar mais_frequente
'''

from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    def test_1(self):
        entradas = [['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu'],
                    ['banana', 'abacate', 'abacate'], ['pimenta'],
                    ['pimenta', 'pimenta', 'pimenta', 'pimenta'],
                    ['abobora', 'chuchu', 'abobora', 'chuchu', 'chuchu'],
                    [
                        'abobora', 'chuchu', 'abobora', 'chuchu', 'chuchu',
                        'pimenta', 'pimenta', 'pimenta', 'pimenta'
                    ]]
        esperados = [
            'abobora',
            'abacate',
            'pimenta',
            'pimenta',
            'chuchu',
            'pimenta',
        ]
        for entrada, esperado in zip(entradas, esperados):
            obtido = self.function(entrada)
            self.assertEqual(
                esperado, obtido,
                'Não funcionou para a entrada {0}. Esperado: {1}. Obtido: {2}.'
                .format(entrada, esperado, obtido))
