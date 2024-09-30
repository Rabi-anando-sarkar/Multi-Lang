def factorial(n):
    result = 1
    
    if n == 0 or n == 1:
        return result
    
    for i in range(2,n+1):
        result *= i
        
    return result

print(factorial(0))
print(factorial(1))
print(factorial(4))
print(factorial(5))