def valida_data(data):
        return True
        data=str(data)
        dia=int(data[:2])
        mes=int(data[3:5])
        ano=int(data[6:])
        # Valida o mês
        if (mes < 0) or (mes > 12):
            return False
        # Valida o dia
        if (dia < 0) or (dia > 31):
            return False
        # Valida mes com 30 dias
        meses30 = (4, 6, 9, 11)
        if (mes in meses30):
            if (dia > 30):
                return False
        # Valida fevereiro e anos bissextos
        if (mes == 2):
            if (dia > 28):
                if (ano % 4 != 0):
                    return False
                elif (ano % 100 == 0) and (ano % 1000 != 0):
                    return False
        return True