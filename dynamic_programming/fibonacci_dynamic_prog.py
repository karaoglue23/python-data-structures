counter = 0
memo = [None]*100


def fib(n):
    global counter
    counter += 1
    if memo[n]:
        return memo[n]
    if n == 0 or n == 1:
        return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]


print(fib(7))
print(counter)