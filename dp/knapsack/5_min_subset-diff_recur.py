arr=[1,6,11,5]
n=len(arr)
sums=sum(arr)
def subset_diff(arr,n,sumCal,sumTot):
    if n==0:
        return abs(sumTot-2*sumCal)
    elif sumCal<=sumTot:
        return min(subset_diff(arr,n-1,sumCal+arr[n-1],sumTot)
        ,subset_diff(arr,n-1,sumCal,sumTot))
    else:
        return subset_diff(arr,n-1,sumCal,sumTot)
print(subset_diff(arr,n,0,sums))
print("\nSecond Way\n")
arr=[1,6,11,5]
n=len(arr)
sums=sum(arr)
def subset_diff(arr,n,sums1):
    if n==0:
        return abs(sums-2*sums1)
    return min(subset_diff(arr,n-1,sums1+arr[n-1])
        ,subset_diff(arr,n-1,sums1))
print(subset_diff(arr,n,0))
