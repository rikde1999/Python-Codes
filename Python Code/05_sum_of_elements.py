#1st method to solve the sum of the elements

# def sum_of_the_elements(nums):
#     sum=0
#     for num in nums:
#         sum+=num
#     return sum
# nums=[1,2,3,4,5]
# total= sum_of_the_elements(nums)
# print("the sum of the elements is : " ,total)



#2nd method to solve the sum of the elements

# a=[]
# sum=0
# size = int(input("enter the size of the list : "))
# for num in range(size):
#     elements = int(input("enter the elements in the list : "))
#     a.append(elements)
# for num in range(size+1):
#     sum+=num
# print(sum)


#3rd method to solve the sum of the elements 

def sum_of_the_elements(Numlist):
    sum=0
    for num in range(number):
        sum+=Numlist[num]
    return sum
Numlist=[]
number=int(input("enter the total number of elemenets for the list: "))
for num in range(1,number+1):
    elements=int(input("enter the elements for the list : "))
    Numlist.append(elements) 
total = sum_of_the_elements(Numlist)
print("the total sum of the elements is :", total)   



