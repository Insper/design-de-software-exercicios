import math


def snell_descartes(n1, n2, teta1):
    sin_t2 = n1 * math.sin(math.radians(teta1)) / n2
    teta2_r = math.asin(sin_t2)
    return math.degrees(teta2_r)
