n = [3,2,8,9,0]
for i in range(len(n)-1):
    for j in range(len(n)-1):
        if n[j] > n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]
print(n)
