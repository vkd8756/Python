import sys
#sets setrecursionlimit to 1000000
#sys.setrecursionlimit(1000000)
print("factorial")
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))
print(fact(2))
print("======\n")
print("bad fibonacci")
def bad_fib(n):
    if n==1 or n==2:
        return 1
    else:
        return bad_fib(n-1)+bad_fib(n-2)
print(bad_fib(6))
print(bad_fib(10))
print("======\n")
print("good fibonacci")
def good_fib(n):
    if n<=1:
        return(n,0)
    else:

        (a,b)=good_fib(n-1)
        print("a=",a,"b=",b,"===",a+b)
        return(a+b,a)
print(good_fib(6))
