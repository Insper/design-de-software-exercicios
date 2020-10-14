Um sistema de correios foi encarregado de enviar uma remessa de pacotes o mais rápido possível 
Para economizar tempo com a comunicação, foi criado um sistema de organização destes pacotes, em que cada um deles corresponde a uma lista no seguinte formato:
- Posição 0: número total de pacotes
- Posição 1: número daquele pacote (um inteiro, sequencial, crescente, que começa em um)
- Posição 2: tamanho do pacote (todos os pacotes devem ter um tamanho igual ao do primeiro)
Um exemplo de uma remessa com quatro elementos seria:
	remessa = [[4,1,20],[4,2,20],[4,3,20],[4,4,20]]
Estes pacotes precisam passar individualmente por uma verificação para testar se contêm algum erro. Se este for o caso, a função deve devolver uma mensagem assim que o erro for encontrado. 
Ao final, é realizada uma última checagem que confere o número dos pacotes qye chegaram e indica se algum foi perdido ou se tudo estava certo.
Faça uma função que recebe uma lista com esses pacotes (como a do exemplo) e percorre essa lista, indicando se:
- A ordem dos pacotes foi diferente do esperado - função deve devolver a string: "ordem errada"
- O tamanho de algum pacote foi indicado de modo errado - função deve devolver a string: "tamanho errado"
- Algum pacote não chegou na verificação feita ao final (número do pacote não corresponde ao total) - função deve devolver a string: "pacote perdido"
Caso contrário, a função deve devolver a string: "tudo certo".
Você pode assumir que apenas um erro ocorre por entrada.