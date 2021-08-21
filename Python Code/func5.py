def sum_num(num):
    if num:
        return num + sum_num(num-1)
    else:
        return 0 

res = sum_num(10)
print(res)
