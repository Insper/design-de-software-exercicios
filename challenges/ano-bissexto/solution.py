def eh_bissexto(ano):
    if ano % 4 != 0:
        return False
    if ano % 100 == 0:
        return ano % 400 == 0
    return True
