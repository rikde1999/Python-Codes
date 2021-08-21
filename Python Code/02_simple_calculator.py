def add(n1,n2):
    return n1+n2

def subtarct(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

n1=int(input("enter the first number :\n"))
n2=int(input("enter the first number :\n"))
choice=input("enter what you want to do:\n")

result=0
if choice == '+':
    result=add(n1,n2)

elif choice == '-':
    result=subtarct(n1,n2)

elif choice == '*':
    result=multiply(n1,n2)

elif choice =='/':
    result=divide(n1,n2)
else:
    print("you chose a wrong input: ")
print(n1,choice,n2,'=',result)