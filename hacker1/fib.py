"1 1 2 3 5 8 13"
def fib(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        fibo=fib(n-1)+fib(n-2)
    return fibo
print(fib(6))
n=int(input(":"))
i=0
ans=0
n1,n2=0,1
while i<n:
    nth=n1+n2
    ans=ans+i
    print(ans)
    i += 1
