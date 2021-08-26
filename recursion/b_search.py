a=[2,4,5,7,23,45,67,89,90]
a.sort()
def bs(arr,target,first,last):
    if last<first:
        return False
    else:
        mid=(first+last)//2
        if  target==arr[mid]:
            return True
        elif target<arr[mid]:
            return bs(arr,target,first,mid-1)
        else:
            return bs(arr,target,mid+1,last)
print(bs(a,23,0,len(a)))
