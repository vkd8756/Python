n=3
sum=4
arr=[1,2,3]
def poss(curr_sum,arr,n):
    if curr_sum==0:
        return 1
    elif curr_sum<0:
        return 0
    elif n<=0:
        return 0
    else :
        return poss(curr_sum-arr[n-1],arr,n) + poss(curr_sum,arr,n-1)
print(poss(sum,arr,n))
