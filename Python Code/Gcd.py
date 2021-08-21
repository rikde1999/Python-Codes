def computeGCD(a,b):
    if b == 0:
        return a
    else:
        return computeGCD(b,a%b)
    
n1 = int(input("enter"))
n2 = int(input("enter"))
print(computeGCD(n1,n2))
