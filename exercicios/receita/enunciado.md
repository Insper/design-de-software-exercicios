Em um belo dia, você decidiu fazer um bolo. Já estava no meio da receita, quando descobriu que suas xícaras e colheres tinham tamanhos diferentes do esperado. Para não estragar a sobremesa, você teve a brilhante ideia de fazer uma função para calcular as conversões para poder usar o copo de medidas, em mililitros. 
Faça uma função que recebe uma receita em forma de dicionário, em que as chaves são os ingredientes (no singular ou plural) e os valores correspondem às quantidades (em xícaras ou colheres). A função deve retornar um dicionário, ainda com os ingredientes como chaves, mas com as quantidades em ml.  O formato das strings correspondentes aos valores do dicionário a serem devolvidas deve ser: “X ml”, sendo X o número correspondente à quantidade convertida.
Você pode basear os valores de conversão de acordo com a figura.
Um exemplo seria:
Entrada da função: receita = { "ovos":"4", "açúcar":"2 xícaras", "leite":"1 xícara", "farinha":"2 xícaras", "fermento": "1 colher de sopa","baunilha":"1 colher de chá" }
Saída da função: {'ovos': '4', 'açúcar': '500 ml', 'leite': '250 ml', 'farinha': '500 ml', 'fermento': '15 ml', 'baunilha': '5 ml'}


Fonte da figura: https://br.pinterest.com/pin/14144186317979140/