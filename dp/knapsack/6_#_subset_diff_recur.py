arr=[1,1,2,3]
sum=sum(arr)
diff=1
res=(sum+diff)//2
n=len(arr)
def subset(arr,sum,n):
    if (sum==0):
        return 1
    if n==0 and sum!=0:
        return 0
    return subset(arr,sum-arr[n-1],n-1) + subset(arr,sum,n-1)
print(subset(arr,res,n))
