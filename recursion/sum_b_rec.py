#binary rec=two times same func is called
a=[1,2,3,4,5]
def b_sum(arr,start,stop):
    if start>=stop:
        return 0
    elif start==stop-1:
        return arr[start]
    else:
        mid=(start+stop)//2
        return b_sum(arr,start,mid)+b_sum(arr,mid,stop)
print(b_sum(a,0,len(a)))
