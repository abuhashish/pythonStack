def func(list):
    newlist=[]
    for i in range (0,list[0],1):
        newlist.append(list[1])
    return newlist
print(func([6,2]))