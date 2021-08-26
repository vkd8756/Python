def howsum(target,lst):
    if target==0:
        return []
    if target<0:
        return None
    for i in lst:
        k=target-i
        res=howsum(k,lst)
        #print(res)
        if res!=None :
            res.append(i)
            return res
    return None
print('\nbrute force')
print(howsum(7,[5,3,4,7]))
#print(howsum(300,[7,14]))
print("\nMemoization")
def mem_howsum(target,lst,memo):
    print(memo)
    if target in memo:
        return memo[target]
    if target==0:
        return []
    if target<0:
        return None
    for i in lst:
        k=target-i
        res=mem_howsum(k,lst,memo)
        #print(res)
        if res!=None :
            res.append(i)
            memo[target]=res
            return memo[target]
    memo[target]=None
    return memo[target]

print(mem_howsum(7,[5,3,4,7],{}))
#print(mem_howsum(300,[7,14],{}))
