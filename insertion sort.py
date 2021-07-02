# def insertion_sort(arr):
#     for i in range(len(arr)):
#         temp = arr[i]
#         pos = i
        
#         while pos > 0 and arr[pos-1] > temp:
#             arr[pos] = arr[pos-1]
#             pos-=1
#             arr[pos] = temp
#     return arr

# numbers = [3,5,8,9,2]
# insertion_sort(numbers)
# print(numbers)

arr = [2,5,1,9,7]
for i in range(len(arr)):
    temp = arr[i]
    pos = i

    while pos > 0 and arr[pos-1] > temp:
        arr[pos] = arr[pos-1]
        pos-=1
        arr[pos] = temp
        print(arr)

    