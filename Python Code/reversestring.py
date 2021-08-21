def string(str):
    rev_str=''
    index=len(str)
    while index>0:
        rev_str+=str[index-1]
        index=index-1
    return rev_str
str=input("enter the word or string you want to reverse")
print(string(str))
