def fib(n):
    """print a fibonacci series up to n."""
    a,b=0,1
    while b<n:
        print b,
        a,b=b,a+b
fib(2000)
