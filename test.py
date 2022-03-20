i = [['a1','b1','c1'],
     ['a2','b2','c2'],
     ['a3','b3','c3']]

a = ""
b = ""
c = ""

for k in i:
    for index, value in enumerate(k):
        if index == 0:
            a += value
        elif index == 1:
            b += value
        else :
            c += value
for j in i:
    print()