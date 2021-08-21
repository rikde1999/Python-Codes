p = int(input("enter the row number for matrix1   :"))

q = int(input("enter the coloum number for matirx2 : "))

n = int(input("enter the coloum number for matirx2 : "))

print("Enter the elements for matrix1  :")
matrix1 = [[int(input()) for i in range(n)]for j in range(p)]
print("matrix 1 : ")
for i in range(p):
    for j in range(n):
        print(format(matrix1[i][j], "<3"), end='')
    print()


print("Enter the elements for matrix2  :")
matrix2 = [[int(input()) for i in range(q)]for j in range(n)]
print("matrix 2 : ")
for i in range(n):
    for j in range(q):
        print(format(matrix2[i][j], "<3"), end='')
    print()

result = [[0 for i in range(q)] for j in range(p)]
for i in range(p):
    for j in range(q):
        for k in range(n):
            result[i][j] = result[i][j] + matrix1[i][k] * matrix2[k][j]

print("result is :")
for i in range(p):
    for j in range(q):
        print(format(result[i][j], "<3"), end='')
    print()
