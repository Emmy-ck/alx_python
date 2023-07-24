def is_prime(number):
    if number <= 1:
        return False
    
    for i in range(2, int(number / 2) + 1): #Check divisors from 2 upto the squareroot of the number
        if number % i == 0:
            return False
        
    return True