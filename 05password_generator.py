import random,string

def password(size):
    all_chars = string.ascii_letters + string.digits + string.punctuation  #a password has all the character in it
    password = ''  # initilizing the password has no data
    for char in range(size):
        # im asking the computer to take inputs from the all_chars and generators a random value
        rand_char = random.choice(all_chars)
        # now its storing the value of the random password in the pervious non data password section
        password = password + rand_char
    return password


pass_len = int(input("how many charater of password you want to have"))
new_password = password(pass_len)
print("your new password :", new_password)