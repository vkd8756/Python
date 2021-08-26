def max_heap(arr):
    n=len(arr)
    for i in range(n,-1,-1):
        _max_heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        _max_heapify(arr,i,0)
def _max_heapify(arr,n,i):
    l=2*i+1
    r=2*i+2
    largest=i
    if (l<n and arr[l]>arr[i]):
        largest=l
    if (r<n and arr[largest]<arr[r]):
        largest=r
    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]
        _max_heapify(arr,n,largest)
a=[33,35,42,10,7,8,14,19,48]
max_heap(a)
print(a)
