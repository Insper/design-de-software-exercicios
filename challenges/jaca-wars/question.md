Jaca Wars! Você mora no sítio, e está em guerra com seu vizinho. Você dispõe de uma catapulta de lançamento de jacas, onde você consegue escolher a velocidade v e o ângulo $\theta$, **em graus**, de lançamento da jaca. Uma jaca quando cai se espalha por um raio de 2 metros. Seu alvo é a catapulta do vizinho, que está à 100 metros da sua. 

Faça um programa que pede a velocidade e o ângulo de lançamento da sua jaca, e diz se ela cairá muito perto, muito longe, ou acertará o alvo. Considere que a jaca acerta o alvo se cai à uma distância do alvo menor que o seu raio de espalhamento. A fórmula da distância alcançada por um projétil (na ausência de efeitos de arrasto da atmosfera) é:

$$ d = \frac{v^2\sin(2\theta)}{g} $$

onde $g=9.8 m/s^2$. Os possíveis valores impressos são `'Muito perto'`, `'Muito longe'` e `'Acertou!'`. Considere "Muito perto" se não chegou no alvo, e "Muito longe" se passou do alvo. **O seu programa deve imprimir exatamente essas strings, caso contrário ele será considerado errado (mesmo que a fórmula esteja correta).**

(Nota do professor: jacas balísticas podem ser letais. Não jogue jacas nos outros.)