def calcula_escola(escola):
    
    nota_escola = 0 # Nota final da escola de samba
    
    i = 0
    while i < len(escola):

        if escola[i][0]<=escola[i][1] and escola[i][0]<=escola[i][2] and escola[i][0]<=escola[i][3]:
            nota_escola += escola[i][1] + escola[i][2] + escola[i][3]
        elif escola[i][1]<=escola[i][0] and escola[i][1]<=escola[i][2] and escola[i][1]<=escola[i][3]:
            nota_escola += escola[i][0] + escola[i][2] + escola[i][3]
        elif escola[i][2]<=escola[i][0] and escola[i][2]<=escola[i][1] and escola[i][2]<=escola[i][3]:
            nota_escola += escola[i][0] + escola[i][1] + escola[i][3]
        else:
            nota_escola += escola[i][0] + escola[i][1] + escola[i][2]
        
        i += 1

    return nota_escola


#tom_maior = [[9.9, 9.9, 10, 9.9], [10, 9.9, 9.8, 10], [10, 10, 10, 10], [10, 10, 10, 10], [10, 9.9, 9.9, 10], [9.9, 10, 10, 10], [10, 10, 9.9, 9.9], [0.0, 9.9, 10, 9.9], [10, 9.8, 10, 10]]
#print(calcula_escola(tom_maior))
#Nota da escola Tom Maior == 269.3

#aguia_de_ouro = [[10, 10, 9.9, 10], [9.9, 10, 10, 9.9], [10, 10, 10, 10], [10, 10, 10, 10], [10, 10, 10, 10], [9.9, 10, 10, 10], [10, 10, 10, 10], [0, 10, 10, 10], [10, 10, 10, 10]]
#print(calcula_escola(aguia_de_ouro))
#Nota aguia_de_ouro == 269.9

#perola_negra = [[9.7, 9.9, 9.7, 9.8], [9.7, 9.9, 9.7, 10], [10, 10, 10, 10], [10, 10, 10, 10], [9.4, 9.6, 9.8, 10], [9.9, 9.9, 9.9, 10], [10, 10, 10, 10], [0, 9.8, 9.8, 9.8], [10, 10, 9.8, 10]]
#print(calcula_escola(perola_negra))
#Nota perola_negra == 267.6
