Em um formulário, o campo da data é salvo como uma string no seguinte formato: data = “dd/mm/yyyy”, sendo os dias, meses e anos números inteiros positivos.

Faça uma função que recebe uma string como a indicada e devolve True se a data for válida ou False, caso contrário. Na validação, você deve considerar a quantidade de meses e de dias no mês. Lembre-se de que alguns meses têm 30 enquanto outros possuem 31 dias. Também é importante levar em conta os casos de fevereiro e anos bissextos!

Um exemplo de data válida seria: “01/01/2021”

Enquanto exemplos de datas inválidas seriam: “30/02/2020”, "31/04/2020" ou "32/13/2020".