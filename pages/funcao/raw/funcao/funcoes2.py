"""
Programa que converte de milhas para quilômetros. Versão melhor documentada.

@author: Profs. de Design de Software
"""

# Função que converte um valor de distância
# dado em milhas para quilômetros.
def converte_milhas_para_km(distancia_mi):
    distancia_km = 1.60934 * distancia_mi
    return distancia_km

# Quanto é 10 mi em km?
milhas = 10
km = converte_milhas_para_km(milhas)
print(km)
