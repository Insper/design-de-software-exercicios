def aniversariantes_de_setembro(dic={}):
    dic_setembro = {}
    for i in dic:
        if dic[i][3:5] == '09':
            dic_setembro[i] = dic[i]
    return dic_setembro