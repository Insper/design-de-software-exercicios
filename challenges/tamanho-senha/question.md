Você estava pensando em possíveis senhas bacanas e anotou todas elas, em forma de texto. Porém esqueceu de se informar do tamanho mínimo que elas deveriam ter. Ao invés de revisar as palavras uma por uma, você teve a brilhante ideia de escrever uma função em Python para fazer isso por você!
A função recebe esse texto (como uma String) e um número inteiro positivo N, correspondente a um tamanho, e retorna uma lista com todas as palavras maiores que N contidas na String recebida.
Um exemplo seria:
	-  Entrada: "frase para a função que filtra as palavaras", N=5
	-  Saída: ['função', 'filtra', 'palavaras']
Se todas as palavras forem menores que N, a função retorna uma lista vazia.