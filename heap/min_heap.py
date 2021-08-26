def min_heap(arr):
    n=len(arr)//2
    for i in range(n,-1,-1):
        _min_heap(arr,i)
def _min_heap(arr,i):
    l=2*i+1
    r=2*i+2
    smallest=i
    if (l<len(arr) and arr[l]<arr[i]):
        smallest=l
    if (r<len(arr) and arr[smallest]>arr[r]):
        smallest=r
    if smallest!=i:
        arr[smallest],arr[i]=arr[i],arr[smallest]
        _min_heap(arr,smallest)
a=[11,6,5,0,8,2,7]
min_heap(a)
print(a)
