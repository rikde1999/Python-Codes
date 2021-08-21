def reverse(string):
    reversed_string = ''
    for i in string:
        reversed_string = i+reversed_string
    print(reversed_string)

string = input("enter : ")
reverse(string)