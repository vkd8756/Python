arr=[1,5,6,11]
sum=sum(arr)
n=len(arr)
t=[[-1 for i in range(sum+1)] for j in range(n+1)]
def subset(arr,sum,n):
    if sum==0:
        return True
    if n==0 and sum!=0:
        return False
    if t[n][sum]!=-1:
        return t[n][sum]
    elif arr[n-1]<=sum:
        t[n][sum]=subset(arr,sum-arr[n-1],n-1) or subset(arr,sum,n-1)
        return t[n][sum]
    else:
        t[n][sum]=subset(arr,sum,n-1)
        return t[n][sum]
print(subset(arr,sum,n))
print(t)
