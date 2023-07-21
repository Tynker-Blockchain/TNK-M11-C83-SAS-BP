import random
import math

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n/2 +1)):
        if n % i == 0:
            return False
    return True

''' 
   Modify the generate prime to take range of numbers to find a prime number in between.
   If no prime is found then return "Prime dose not exits in given range"
'''

# Take two numbers as parameters  x,y
def generatePrime(x,y):
    # Create a flag variable found and set it to False
    found = False
    prime = random.randint(x, y)
    while not isPrime(prime):
        prime += 1
        # Break the loop if  prime becomes greater then y
        if prime > y:
            break

    if isPrime(prime):
        return prime
    else:
        return "Prime dose not exits in given range"    

    return prime

# Pass two numbers between which you want to find prime number
num = generatePrime(10, 20)
print("Prime number in given range:", num)