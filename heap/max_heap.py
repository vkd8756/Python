def max_heap(arr):
    n=len(arr)//2
    for i in range(n,-1,-1):
        _max_heapify(arr,i)
def _max_heapify(arr,i):
    l=2*i+1
    r=2*i+2
    largest=i
    if (l<len(arr) and arr[l]>arr[i]):
        largest=l
    if (r<len(arr) and arr[largest]<arr[r]):
        largest=r
    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]
        _max_heapify(arr,largest)

a=[11,6,5,0,8,2,7]
max_heap(a)
print(a)
