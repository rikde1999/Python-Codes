for i in range(1001):
    num = i
    sum = 0
    n = len(str(i)) 
    while(i != 0):
        digit = i % 10
        sum = sum + digit ** n
        i = i // 10 

    if num == sum:
        print(num)