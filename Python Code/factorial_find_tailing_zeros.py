#calculate the factorial of a given number and
#find the number of trailing zero in that factorial

def factorial(number):
    if number==0 or number==1:
        return 1
    else:
         return number*factorial(number-1)
def trailingzero(n):
    count=0
    i=5
    while (number//i !=0):
        count+=int(number/i)
        i=i*5
    return count

if __name__=='__main__':
    number=int(input("enter the number"))
    #fact=factorial(number)
    #print(f"the factorial is {fact}")
    print(trailingzero(number))