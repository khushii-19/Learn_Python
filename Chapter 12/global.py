a = 89

def fun(): 
    # global a but function k andar its local funnc k bahar flobal wala he print hoga
    a = 3
    print(a)


fun()
print(a)