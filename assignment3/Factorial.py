n=int(input("Enter a number: "))
def factorial_for_loop(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i  
        return result
print("factorial of ",n,"is",factorial_for_loop(n))