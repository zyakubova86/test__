# testing some git features

def add(a, b):
    return a + b


def fib(n):
    f1, f2 = 1, 1

    for i in range(n):
        yield f1
        f1, f2 = f2, f1 + f2


def fib_recurs(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)


# Another change test
print("test2")        
