n = int(input("enter the number"))
temp = n
rev= 0 
while (n>0):
    d = n%10
    rev = rev*10+d  
    n//=10
if temp == rev:
    print("rev")