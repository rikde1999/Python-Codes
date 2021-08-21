FirstSet = {65, 42, 78, 83, 23, 57, 29}
SecondSet = {67, 73, 43, 48, 83, 57, 29}
count = 0
intersection = FirstSet.intersection(SecondSet)

print("the common elements are :.",intersection)
for i in intersection:
    FirstSet.remove(i)
print(FirstSet)



          

    