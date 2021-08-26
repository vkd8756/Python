a=[1,2]
def unique(arr,start,stop):
    if stop-start<1:return False
    elif unique(arr,start,stop-1):return True
    elif unique(arr,start+1,stop):return True
    else: return arr[start]!=arr[stop]
print(unique(a,0,len(a)))
