total=0
count=0
print("If you press 'done' then the loop will terminate and you will get the result ")
while True:
    inp=input("enter the number ")
    if inp=='done': 
        break
    value=int(inp)
    total=total+value
    count=count+1
avg=total/count
print(avg)
print(total)