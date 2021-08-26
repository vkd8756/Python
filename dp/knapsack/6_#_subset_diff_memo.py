arr=[1,1,2,3]
sum=sum(arr)
diff=1
res=(sum+diff)//2
n=len(arr)
t=[[-1 for i in range(res+1)] for j in range(n+1)]

def subset(arr,sum,n):
    if (sum==0):
        return 1
    if n==0 and sum!=0:
        return 0
    if t[n][sum]!=-1:
        return t[n][sum]
    t[n][sum]=subset(arr,sum-arr[n-1],n-1) + subset(arr,sum,n-1)
    return t[n][sum]
print(subset(arr,res,n))
