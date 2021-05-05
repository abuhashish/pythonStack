def func(list):
    lens=len(list)+1
    for i in range(0,lens):
        list.insert(0,list[i+i-1])
    for i in range(6):
        list.pop()
    return list
print(func([1,2,3,4,5]))