#tough one


with open('currency.txt') as f:
    lines=f.readlines()

#print(a)
currencydict={}
for line in lines:
    parsed = line.split("\t")
    currencydict[parsed[0]]=parsed[1]
    

amount=int(input("enter the amount \n"))
print("enter the name of th currency you wqant ot convery this amount to")
[print(item) for item in currencydict.keys()]
currency=input("enter the values ")
print(f"{amount}Income is equal to{amount*float(currencydict[currency])}{currency}")