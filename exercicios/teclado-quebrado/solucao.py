def conserta_teclado (string):
    string=string.lower()
    s=""
    for ch in string:
            if len(s)==0:
                s+=ch
            elif s[-1] != ch:
                s+=ch

    return s  