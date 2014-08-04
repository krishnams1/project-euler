# Problem 2 (python)

N = 4000000

def fib(max):
    f1, f2 = 0, 1
    while f1 < max:
        yield f1
        f1, f2 = f2, f1 + f2

print sum(filter(lambda a: (a %2 ==0), fib(N)))
