def check(string,substr):
    if(string.find(substr)==True):
        print ('no')
    else:
        print('yes')
string=input("enter the string from where you want to search : ")
substr=input("enter the word you want to search : ")
check(string,substr)