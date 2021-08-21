# list=[]
# n=int(input("enter the list"))
# for i in range(1,n+1):
#     elements=int(input("enter the elements : "))
#     list.append(elements)
# print("the largest of the list is" , max(list))


def mymax():
    n=int(input("enter the size of the list : "))
    for i in range(1,n+1):
        elements=int(input("enter the elements : "))
        list.append(elements)
    max=list[0]
    for x in list:
        if x > max:
            max = x
    return max
list=[]
print(mymax())