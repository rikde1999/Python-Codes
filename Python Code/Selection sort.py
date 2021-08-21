#for non duplicate numbers in a list

'''1.'''   # list1 = [7,2,2,7,1,9,6,0]

# for i in range(len(list1)):
#     min_val = max(list1[i:])
#     min_val = min(list1[i:])
#     min_index = list1.index(min_val)
#     list1[i] , list1[min_index] = list1[min_index] , list1[i]

# print(list1)

#for duplicate number in a list

''' 2. '''  # list1 = [7,2,2,-7,-1,9,6,0]

# for i in range(len(list1)):
#     min_val = max(list1[i:])
#     min_val = min(list1[i:])
#     min_index = list1.index(min_val,i)
#     list1[i] , list1[min_index] = list1[min_index] , list1[i]

# print(list1)

''' 3. '''   # list1 = [7,2,2,-7,-1,9,6,0]

# for i in range(len(list1)):
#     # min_val = max(list1[i:])
#     min_val = min(list1[i:])
#     min_index = list1.index(min_val,i)
#     if list1[i] != list1[min_index]:
#         list1[i] , list1[min_index] = list1[min_index] , list1[i]

# print(list1)

''' 4. ''' #user input and without using built in function

# list1 = [7,2,2,-7,-1,9,6,0]

# for i in range(len(list1) - 1):
#     min_value = list1[i]
#     for j in range(i+1, len(list1)):
#         if list1[j] > min_value:
#             min_value = list1[j]
#     min_index = list1.index(min_value,i)
#     if list1[i] != list1[min_index]:
#         list1[i] , list1[min_index] = list1[min_index] , list1[i]
        
# print(list1)

''' 5. '''

num = int(input("how many number you want to input"))
list1 = [int(input("how many number you want to input")) for x in range(num)]

for i in range(len(list1) - 1):
    min_value = list1[i]
    for j in range(i+1, len(list1)):
        if list1[j] > min_value:
            min_value = list1[j]
    min_index = list1.index(min_value,i)
    if list1[i] != list1[min_index]:
        list1[i] , list1[min_index] = list1[min_index] , list1[i]
        
print(list1)

