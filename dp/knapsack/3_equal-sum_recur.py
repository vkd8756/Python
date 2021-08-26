arr=[11,5,1,5]
#arr=[1,5,3]
n=len(arr)
sums=sum(arr)
def partition(arr,n,sums):
    #if sums.is_integer()!=True:
        #return False
    if sums==0:
        return True
    elif n==0 and sums!=0:
        return False
    elif sums>=arr[n-1]:
        return partition(arr,n-1,sums-arr[n-1]) or partition(arr,n-1,sums)
    else:
        return partition(arr,n-1,sums)
#print(partition(arr,n,sums/2))
if sums%2!=0:
    print(False)
else:
    print(partition(arr,n,sums//2))
