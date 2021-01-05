Se pode usar uma série para calcular o valor do e (número de Euler ou Neperiano). Basicamente a ideia é somar uma sequência de número, e conforme se avança na sequência, se chega mais perto do valor desejado. A série de Taylor para calcular $e^x$ é:

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \frac{x^5}{5!} + ...$$

Faça uma função em Python que calcula o resultado do $e^x$ para uma série de tamanho $n$. Você pode supor que as entradas para $x$ e $n$ serão enviadas nesta ordem e sempre serão números positivos.