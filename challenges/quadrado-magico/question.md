Um quadrado mágico consiste em uma matriz quadrada (mesmo número de linhas e colunas), em que os elementos são organizados de modo que a soma de cada linha, coluna ou de cada umas das duas diagonais principais seja sempre a mesma. 
Um exemplo de um quadrado mágico (que pode ser representado por uma lista de listas) seria:
[
        [6, 1, 8],
        [7, 5, 3],
        [2, 9, 4]
    ]
Faça uma função que recebe como argumento uma lista de listas, como a do exemplo, e retorna True se for um quadrado mágico ou False, caso contrário. Você pode assumir que a função sempre receberá uma matriz de números inteiros positivos, de ordem maior ou igual a três.	
Uma dica para facilitar sua resolução: Você pode primeiramente calcular a soma da primeira linha para usar como referência. Depois, cheque cada linha, coluna e as diagonais restantes, comparando-as com a referência estabelecida. Lembre-se que se trata de uma matriz quadrada de tamanho variável!