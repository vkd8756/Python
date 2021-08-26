a=[48,35,42,15,7,18,24]
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
def min_key(arr):
    smallest=arr[0]
    for i in range(0,len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
    return smallest

def insert_key(arr,key):
    arr.append(key)
    i=len(arr)-1
    while i>=1 and arr[i//2]<arr[i]:
        arr[i//2],arr[i]=arr[i],arr[i//2]
        i=i//2
    print(arr)
def delete_max(arr):
    size=len(arr)-1
    if size<1:
        return "error"
    max_root=arr[0]
    arr[0]=arr[size]
    size-=1
    arr.pop()
    _max_heapify(arr,0)
    return arr
max_heap(a)
print(a)
insert_key(a,51)
print(a)
print(delete_max(a))
print(min_key(a))
