def classifica_rima(a, b, c, d):
    if a == b == c == d:
        return 'outra'
    if a == c and b == d:
        return 'alternada'
    if a == d and b == c:
        return 'interpolada'
    if a == b and c == d:
        return 'emparelhada'
    return 'outra'