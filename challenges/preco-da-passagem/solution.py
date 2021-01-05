dist = int(input())
if dist <= 200:
    print('{0:.2f}'.format(dist*0.5))
else:
    print('{0:.2f}'.format(100 + (dist-200)*0.45))