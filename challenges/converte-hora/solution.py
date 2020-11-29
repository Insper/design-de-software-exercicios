def converteHora(hora):
    hora24=int(hora[:2])
    minuto24=int(hora[3:])
    
    if (hora24 > 23) or (hora24 < 0) or (minuto24 < 0) or (minuto24 > 59):
        return None

    if (hora24 < 12):
        if (hora24 == 0):
            hora24 = 12
        return '%02d:%02d AM' % (hora24, minuto24)

    if (hora24 > 12):
        hora24 -= 12
    return '%02d:%02d PM' % (hora24, minuto24)