pl = 0
e = 0
an = 0


def ans():
    qwe=[]
    for i in range(10000):
        tmp=str(i).zfill(4)
        if len(set(map(int, tmp)))==4:
            qwe.append(list(map(int, tmp)))
    return qwe
print(ans())

def ans1():
    pass

def num():
    pass

def ch():
    pass

def bans():
    pass

