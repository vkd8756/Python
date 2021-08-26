a=[[1,2,3],[1,2,3],[1,2,3]]
#print(sum(a[0])+sum(a[1]))
def summ(list1,n):
    #print(n)
    if n==1:
        return sum(a[0])
    else:
        return summ(list1,n-1)+sum(a[n-1])
print(summ(a,len(a)))
