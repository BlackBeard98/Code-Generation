class A:

    def B(self,n):
        if n <=1:
            return n
        return self.fibo(n-1) + self.fibo(n-2)