import math

def isPrime(n):
    if n <= 1:
        return False
    
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print(isPrime(1))
print(isPrime(4))
print(isPrime(5))
print(isPrime(9))