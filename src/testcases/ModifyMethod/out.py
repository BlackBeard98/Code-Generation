class Memoize:

    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]


class Seq:

    @Memoize
    def fib_modified(self, n):
        if n <= 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)
