Você foi contratado para uma fábrica de boias de piscina.

As boias fabricadas têm sempre o formato de um toróide (torus), que é definido pelo raio interno da boia ($R$) e o raio da seção transversal dela ($r$). As boias possuem um peso ($P$) medido por uma balança.

Sua função é descobrir se a boia vai "boiar" ou não. Considere que a densidade da água para a temperatura ambiente de 997 kg/m³ ou 0,997 g/cm³ e qualquer coisa com densidade menor ou igual a esse valor irá boiar. Lembre-se que a densidade é calculada como o peso dividido pelo volume.

Para calcular o volume de um toróide (torus) use a seguinte equação: 

$$2{\pi^2}R{r^2}$$

![](/media/exercicios/torus.png)

Crie uma função que receba o peso da boia ($P$), o raio interno da boia ($R$) e o raio da seção transversal ($r$). Os valores do peso ($P$) serão dados em Kg e os valores dos raios ($R$) e ($r$) em centímetros. Se a boia boiar a função deverá retornar `True`, caso contrário deverá retornar `False`.