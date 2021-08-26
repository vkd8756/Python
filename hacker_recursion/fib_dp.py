
print("This is DP")
def fib_n(n,memo):
    if n in memo:
        return memo[n]
    if n==1 or n==2:
        result= 1
    else:
        result=fib_n(n-1,memo)+fib_n(n-2,memo)
    memo[n]=result
    #print(memo, len(memo))
    return result


def fib_memo(n):
    memo={}
    return fib_n(n,memo)
print(fib_memo(6))
'''1 1 2 3 5 8'''
print("This is bottom up approach")
def bottom_up(n):
    if n==1 or n==2 :
        return 1
    bottom_up=[None]*(n+1)
    bottom_up[1]=1
    bottom_up[2]=1
    for i in range(3,n+1):
        bottom_up[i]=bottom_up[i-1]+bottom_up[i-2]
    print(bottom_up)
    return bottom_up[n]
print(bottom_up(1))
