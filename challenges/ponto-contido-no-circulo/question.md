Crie uma classe chamada `Circulo` que tem na construção (no __init__ ) um ponto como centro e um float como raio. Adicione um método `contem(self, ponto)` que avalia se um ponto está dentro da área do círculo ou não. 

Pontos são representados por objetos da classe `Ponto`, especificada a seguir. Você **não precisa** implementar a classe `Ponto`.

```
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```