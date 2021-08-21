row = int(input("enter the row number : "))
coloumn = int(input("enter the row number : "))

print("enter the elements for matrix 1")

matrix1 = [[int(input()) for i in range(coloumn)] for j in range(row)]
print("matrix 1 ")

for i in range(row):
    for j in range(coloumn):
        print(format(matrix1[i][j]), end=' ')
    print()


print("enter the elements for matrix 2")
matrix2 = [[int(input()) for i in range(coloumn)] for j in range(row)]
print("matrix 2 ")

for i in range(row):
    for j in range(coloumn):
        print(format(matrix2[i][j]), end=' ')
    print()

resutlt = [[0 for i in range(coloumn)] for j in range(row)]
for i in range(row):
    for j in range(coloumn):
        resutlt[i][j] = matrix1[i][j]+matrix2[i][j]

print("result is:")
for i in range(row):
    for j in range(coloumn):
        print(format(resutlt[i][j]),end=' ')

    print()