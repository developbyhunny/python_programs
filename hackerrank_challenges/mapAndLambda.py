cube = lambda x: x ** 3

def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)

n = int(input())
numbers = list(map(fib, range(n)))
result = list(map(cube,numbers))
print(result)