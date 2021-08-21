my_list = [1,2,4,5,6,9,0,34,56]
n = 3
print([my_list[i:i + n] for i in range(0, len(my_list), n)])

