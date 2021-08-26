arr=[11,5,1,5]
#arr=[1,5,3]
n=len(arr)
sums=sum(arr)
t=[[-1 for i in range(sums+1)] for j in range(n+1)]
def partition(arr,n,sums):
    if sums==0:
        return True
    if n==0 and sums>=0:
        return False
    elif sums>=arr[n-1]:
        t[n][sums]=partition(arr,n-1,sums-arr[n-1]) or partition(arr,n-1,sums)
        return t[n][sums]
    else:
        t[n][sums]=partition(arr,n-1,sums)
        return t[n][sums]
if sums%2!=0:
    print(False)
else:
    print(partition(arr,n,sums//2))
