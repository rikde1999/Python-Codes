def get_sum_of_digit(num):
    sum=0
    while num>0:
        last_digit = num % 10
        sum = sum + last_digit
        num = num//10
    return sum
num = int(input("enter a number: "))
total=get_sum_of_digit(num)
print("the total sum of digit is: ",total)