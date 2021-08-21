def swapposition(list,posi1,posi2):
    list[posi1],list[posi2] = list[posi2],list[posi1]
    return list
list=[1,2,3,4]
posi1 , posi2 = 1,3
print(swapposition(list,posi1,posi2))

#print(swapposition(list,posi1-1,posi2-1))