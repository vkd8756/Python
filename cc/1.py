#r=list(map(int,input().split()))
#a=list(map(int,input().split()))
#3 3
#2 2 3
n=3
r=[2,2,3]
#r=[845,7785,2143,8452,1798,3573,5043,3188]
t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    r=list(map(int,input().split()))
    res=r
    i,j=0,1
    while j<n:
        a,b=r[i],r[j]
        p=a
        res[i]=a^p
        res[j]=b^p
        i+=1
        j+=1
    for i in res:
        print(i,end=" ")
