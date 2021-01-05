import math

def calcula_tempo(dic = {}):
    dic_aux = {}
    for i in dic:
        dic_aux[i] = math.sqrt(200/dic[i])
    return dic_aux