
def ms(a):
    if len(a)>1:
        mid=len(a)//2
        left_lst=a[:mid]
        right_lst=a[mid:]
        ms(left_lst)
        ms(right_lst)
        i,j,k=0,0,0
        while j<len(right_lst) and i<len(left_lst):
            if left_lst[i]==right_lst[j]:
                return False
            elif left_lst[i]<right_lst[j]:
                a[k]=left_lst[i]
                i+=1
                k+=1
                return True
            else:
                a[k]=right_lst[j]
                k+=1
                j+=1
                return True
        while i<len(left_lst):
            a[k]=left_lst[i]
            i+=1
            k+=1
            return True
        while j<len(right_lst):
            a[k]=right_lst[j]
            k+=1
            j+=1
            return True
arr=[2,1,4,3,1]
print(ms(arr))
print(arr)
