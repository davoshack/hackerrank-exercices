from functools import cached_property, lru_cache

class Data:
    def __init__(self, n):
        self.n = n

    @cached_property
    def f(self):
        total = 0
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    total += i + j + k
        return total

@lru_cache
def fib(n):
    print(n)
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
