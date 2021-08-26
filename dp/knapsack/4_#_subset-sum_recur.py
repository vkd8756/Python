arr=[1,3,5,7]
#arr=[2,3,5,6,8,10]
sum=8
n=len(arr)
def count_sum(arr,n,sum):
    if sum==0:
        return 1
    if n==0 and sum!=0:
        return 0
    elif arr[n-1]<=sum:
        return (count_sum(arr,n-1,sum-arr[n-1]) + count_sum(arr,n-1,sum))
    else:
        return count_sum(arr,n-1,sum)
print(count_sum(arr,n,sum))
