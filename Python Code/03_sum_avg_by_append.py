len=int(input("How many numbers do you want to find out the average of and you can find their sum"))
nums=[]  #initial list which has no data in it

for i in range(0,len): #looping from 0 to length of the list
    elements=int(input("Enter elements : "))
    nums.append(elements)       #appending the elements to the list nums[] in the second line
total=sum(nums)
avg=total/len
print("sum of the elements",total)
print("average of the numbers are: ", avg)
