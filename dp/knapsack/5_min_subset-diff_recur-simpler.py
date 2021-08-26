arr=[1,6,11,5]
n=len(arr)
sums=sum(arr)
def subset_diff(arr,n,sumCal):
    if n==0:
        return abs(sums-2*sumCal)
    return min(subset_diff(arr,n-1,sumCal+arr[n-1])
        ,subset_diff(arr,n-1,sumCal))
print(subset_diff(arr,n,0))
