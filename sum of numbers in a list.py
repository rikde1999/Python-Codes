test_list = [12,11,13,14]
res = []
for ele in test_list:
    sum = 0
    for digit in str(ele): 
        sum += int(digit)
    res.append(sum)
    
print(res)