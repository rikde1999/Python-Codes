#it search the whole list and returns the index of the element.
list1 = [2,1,5,6,7,1,9,0]
search_the_num = int(input("enetr the number : "))
found = False

for i in range(len(list1)):
    if list1[i] == search_the_num:
        found = True
        print("the search list is : ",i)
        # print("the number is ",search_the_num)
        break

if found == False:
    print("the number is not in the list.")

