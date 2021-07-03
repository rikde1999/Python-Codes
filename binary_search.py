def binary_search(list1,item):
    first = 0
    last = len(list1) - 1
    found = False
    
    while first <= last and not found:
        mid = (first+last) // 2
        if list1[mid] == item:
            found = True
        else:
            if item < list1[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

numlist = [4,27,19,0,28,7,2,9]
search_num = int(input("enetr the number : "))
found = binary_search(numlist,search_num)

if found == True:
    print("its present in the list",search_num)
else:
    print("its not presnt in the list",search_num)
