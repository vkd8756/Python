print("\nreveersing--O(n/2)")
a=[1,2,3,4]
def rev(arr,start,stop):
    if start<stop:
        arr[start],arr[stop-1]=arr[stop-1],arr[start]
        rev(arr,start+1,stop-1)
    return arr

print(rev(a,0,len(a)))

print("\n======\nExponential--O(n)")
def expo(n,p):
    if p==0:
        return 1
    else:
        return n*expo(n,p-1)
print(expo(4,3))
print("\n======\nGood Exponential--O(logn)")
def good_expo(x,p):
    if p==0:
        return 1
    else:
        part=good_expo(x,p//2)
        result=part*part
        if p%2==1:
            result= result*x
        print(result)
        return result
print(good_expo(2,13))
print("\n======\nSum---O(n)")
a=[1,2,3,4]
def summ(arr,n):
    if n==0:return 0
    else:return summ(arr,n-1)+a[n-1]

print(summ(a,len(a)))
