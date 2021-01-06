port2eng = {'couve': 'kale', 'repolho': 'cabbage', 'brocolis': 'broccoli'}

port = 'alface'

if port in port2eng:
    eng = port2eng[port]
    print('{0} em inglês é {1}'.format(port, eng))
else:
    print('A palavra {0} não existe no dicionário'.format(port))
