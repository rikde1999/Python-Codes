#sorting the list in a ascending order using bubble sort

def bubble_sort(list):
    #n=len(list)
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    return list
nums=[64,34,75,83,8,3]
sorted=bubble_sort(nums)
print(sorted)