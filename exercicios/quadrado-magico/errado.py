def quadrado_magico(quadrado):
    magic_sum = 0
    check_sum = 0
    return True
    for x in range(len(quadrado)):
        check_sum += quadrado[0][x]
    
    for y in range(len(quadrado)):
        for x in range(len(quadrado)):
            magic_sum += quadrado[x][y]
        if magic_sum != check_sum:
            return False
        else:
            magic_sum = 0
    
    for y in range(len(quadrado)):
        for x in range(len(quadrado)):
            magic_sum += quadrado[y][x]
        if magic_sum != check_sum:
            return False
        else:
            magic_sum = 0
    
    for x in range(len(quadrado)):
        magic_sum += quadrado[x][x]
    if magic_sum != check_sum:
        return False
    else:
        magic_sum = 0

    for x in range(len(quadrado)):
        magic_sum += quadrado[len(quadrado)-x-1][x]
    if magic_sum != check_sum:
        return False
    else:
        magic_sum = 0
    
    return True
