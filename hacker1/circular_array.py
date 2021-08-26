def circularArrayRotation(a, k, queries):
    c=[]
    r=k%len(a)
    for i in queries:
        b=i-r
        c.append(a[b])
    return c

if __name__=="__main__":
    nkq=list(map(int,input().split()))
    n = nkq[0]
    k = nkq[1]
    q = nkq[2]
    1
    a=list(map(int,input().split()))
    for j in range(q):
        queries.append(int(input()))
    result=(circularArrayRotation(a,k,queries))
    for i in result:
        print(i)