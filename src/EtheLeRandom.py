from random import randint as r

def randint(a, b):
    list = []
    list2 = []
    for i in range(1000):
        list.append(r(a, b))

    for i in range(1000):
        list2.append(r(a, b))

    if r(1, 2) == 1:
        thing = list[r(0, len(list)-1)]
    else:
        thing = list2[r(0, len(list)-1)]


    return thing