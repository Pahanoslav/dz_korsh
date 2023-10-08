for a in range(0, 1000):
    flag = 1
    for x in range(0, 1000):
        if (((x&28!=0) or (x&45!=0)) <= ((x%48 == 0) <= (x&a!=0))) == False:
            flag = 0
    if flag == 1:
        print(a)
