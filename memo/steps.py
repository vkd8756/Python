def rec_steps(m,n):
    if m==1 and n==1:
        return 1
    elif m==0 or n==0:
        return 0
    return rec_steps(m-1,n)+rec_steps(m,n-1)
print(rec_steps(2,3))
print(rec_steps(1,1))
print("\n")
# After memoization

def steps(m,n,memo={}):
    key=str(m)+","+str(n)
    if key in memo:
        return memo[key]
    elif n==1 and m==1:
        return 1
    elif n==0 or m==0:
        return 0
    memo[key]= steps(m-1,n,memo)+steps(m,n-1,memo)
    return memo[key]
print(steps(2,3))
print(steps(1,1))
print(steps(18,18))
