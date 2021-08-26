a=[1,4,2,3,7,12,2]
def maxx(arr,n):
    if n==0:
        return 0
    elif n==1:
        return a[0]
    else :
        b=maxx(arr,n-1)
        if b>=a[n-1]:
            return b
        else:
            return a[n-1]
        #return max(maxx(arr,n-1),a[n-1])
print(maxx(a,len(a)))
