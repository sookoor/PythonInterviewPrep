def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

for i in range(0, 11):
    print str(i) + ": " + str(fib(i))
