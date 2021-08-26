def mem_cansum(target,lst,memo):
    if target in memo:
        return memo[target]
    if target==0:
        return True
    elif target<0:
        return False
    for i in lst:
        k=target-i
        if mem_cansum(k,lst,memo):
            memo[target]=True
            return True
    memo[target]=False
    return False
def cansum(target,lst):
    return mem_cansum(target,lst,{})
#print(mem_cansum(7,[5,3,4,7],{}))
print(cansum(7,[1,2,3]))
print(cansum(300,[7,14]))
