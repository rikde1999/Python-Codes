number_of_terms = 5
start = 2
sum = 0
for i in range(0,number_of_terms):
    print(start,end=' ')
    sum += start
    start = (start * 10) + 2
print("the sum of the series is : ",sum)