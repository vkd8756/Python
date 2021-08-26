arr=[2,3,7,8,10]
arr=[1,3,5,7]
sum=8
n=len(arr)
t=[[-1 for i in range(sum+1)] for j in range(n+1)]
def count_sum(arr,n,sum):
    if sum==0:
        return 1
    if n==0 and sum!=0:
        return 0
    if t[n][sum]!=-1:
        return t[n][sum]
    elif arr[n-1]<=sum:
        t[n][sum]=(count_sum(arr,n-1,sum-arr[n-1]) + count_sum(arr,n-1,sum))
        return t[n][sum]
    else:
        t[n][sum]=count_sum(arr,n-1,sum)
        return t[n][sum]
print(count_sum(arr,n,sum))
#print(t)
