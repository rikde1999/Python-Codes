


# 7.patterns

# *
# **
# ***
# ****
# *****

n = 5
for i in range(n):
    for j in range(i+1):
        print("*",end="")

    print()

# DECEREASING TRIANGLE PATTERN 
# i = 0 - 5   *   *   *   *   *
# i = 1 - 5   *   *   *   *
# i = 2 - 5   *   *   *   
# i = 3 - 5   *   *   
# i = 4 - 5   *   

# in each row their is a decrease in star


n = 5
for i in range(n):

    for j in range(i,n):
        print("*",end = " ")
    print()


#  RIGHT TRIANGLE.

# i =     _   _   _   _   *
# i =     _   _   _   *   *  
# i =     _   _   *   *   *
# i =     _   *   *   *   *
# i =     *   *   *   *   *

# i. Decreasing Space
# ii. Increasing Stars


# iii. First it will print the 5 spaces and then next k loop print the 1st star
#      second it will print th 4 spaces and then next k loop print the 2nd star.


n = 5
for i in range(n):
    for j in range(i,n):
        print(" ",end = " ")

    for k in range(i + 1):
        print("*",end = " ")

    print() 


#  RIGHT SIDED TRIANGLE 

# i = 0 - 5   *   *   *   *   *
# i = 1 - 5   _   *   *   *   *
# i = 2 - 5   _   _   *   *   *   
# i = 3 - 5   _   _   _   *   *   
# i = 4 - 5   _   _   _   _   * 


for i in range(5):
    for j in range(i+1):
        print(" ",end = " ")

    for j in range(i , 5):
        print("*",end = " ")


    print()


# HILL PATTERN

#              *
#          *   *   *   
#     *    *   *   *   *   
# *   *   *    *   *   *   *    


# 1. Decresing Space
# 2. increasing star
# 3. increasing star


n = 5
for i in range(n):
    for j in range(i,n):
        print(" ",end = "")

    for k in range(i):
        print("*",end = "")

    for j in range(i+1):
        print("*",end = "")

    print()



# REVERSE HILL PATTERN

      
# *   *   *    *   *   *   *    
#     *    *   *   *   *  
#          *   *   * 
#              *

# 1. increasing Space
# 2. Decresing star
# 3. Decresing star



n = 5

for i in range(n):
    for j in range(i + 1):
        print(" ",end = " ")

    for k in range(i,n-1):
        print("*",end = " ")

    for j in range(i,n):
        print("*",end = " ")
    print()