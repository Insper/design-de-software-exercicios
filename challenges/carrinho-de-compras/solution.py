'''
Faça uma classe chamada `Carrinho` que inicializa um dicionário vazio no construtor (`__init__(self)`)
e possui dois métodos: `adiciona(self, nome_produto, preco)` e `total_do_produto(self, nome_produto)`.

O método `adiciona` deve inserir o valor `preco` na chave `nome_produto` no dicionário. Se já existir
um valor nessa chave, os preços devem ser somados.

O método `total_do_produto` deve retornar o preço total daquele produto específico.

Exemplo de uso:

```python
c = Carrinho()
c.adiciona('banana', 5)
total_banana = c.total_do_produto('banana')
print(total_banana)  # Vai imprimir 5
c.adiciona('abacate', 7)
c.adiciona('banana', 4)
total_banana = c.total_do_produto('banana')
print(total_banana)  # Vai imprimir 9
```
'''

class Carrinho:
    def __init__(self):
        self.precos = {}

    def adiciona(self, produto, preco):
        if produto not in self.precos:
            self.precos[produto] = 0
        self.precos[produto] += preco

    def total_do_produto(self, produto):
        return self.precos.get(produto)
