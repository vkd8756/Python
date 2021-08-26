arr=[2,3,7,12,10]
sum=11
n=len(arr)
def subset(arr,sum,n):
    if (sum==0):
        return True
    if n==0 and sum!=0:
        return False
    #if n>=0 and sum==0:
    #    return True
    #elif n==0 and sum>0:
    #    return False
    elif arr[n-1]<=sum:
        return subset(arr,sum-arr[n-1],n-1) or subset(arr,sum,n-1)
    else:
        return subset(arr,sum,n-1)
print(subset(arr,sum,n))
