# prime number in function
def prime_number(num):
    if num == 0 or num == 1:
        return False

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False

print(prime_number(1))