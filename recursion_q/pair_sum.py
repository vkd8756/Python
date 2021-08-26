a=[1,2,3,4]
k=8
a.sort()
def bs(arr,target,first,last):
    if last<first:
        return False
    elif first!=last-1 and arr[last-1]>=target:
        mid=(first+last)//2
        if  target==arr[mid]:
            return True
        elif target<arr[mid]:
            return bs(arr,target,first,mid-1)
        else:
            return bs(arr,target,mid+1,last)
    return False
collect=[]
for i in range(len(a)):
    target=k-a[i]
    collect.append(bs(a,target,i,len(a)))
print(True in collect)
