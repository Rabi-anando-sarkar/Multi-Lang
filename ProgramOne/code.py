def fibonacci(n):
    fib = [0,1]
    for i in range(2,n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib

print(fibonacci(3))
print(fibonacci(5))
print(fibonacci(7))
print(fibonacci(9))