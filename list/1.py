a=[1,2,3,4]
b=[5,7]
def union(arr1,arr2,c=[]):
    for i in arr1:
        c.append(i)
    for i in arr2:
        if i not in c:
            c.append(i)
    return c
print(union(a,b))
