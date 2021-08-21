# for i in range(-10,0,1):
#     print(i)

n = 76542
rev = 0
while n > 0:
    digit = n % 10
    rev = (rev * 10) + digit
    n //= 10
print(rev)

