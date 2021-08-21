def remove(string,i):#remove charcter at index i
    a=string[ :i]#character before the ith index
    b=string[i+1: ]#character after the nth index
    return a+b #returning string After removing
#calling the remove string
if __name__=='__main__':
    string="helloworld"
    i=3#rremoving the 3rd index fro the word
    print(remove(string,i)) 
    