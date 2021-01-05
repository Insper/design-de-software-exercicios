Crie uma classe `Retangulo`, com um construtor (`__init__`) que recebe dois pontos e os armazena como atributos:

- Ponto do canto inferior esquerdo
- Ponto do canto superior direito

Cada ponto é um objeto do tipo `Ponto`, como definido à seguir:

```
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

Assuma que a classe `Ponto` já está definida, você só precisa implementar a classe `Retangulo`.

Sua classe `Retangulo` deve possuir dois métodos sem argumentos adicionais (lembre-se que métodos sempre recebem `self`):

1. `calcula_perimetro(self)`: calcula o perímetro do retângulo;
2. `calcula_area(self)`: calcula a área do retângulo.