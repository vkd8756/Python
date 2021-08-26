def cansum(target,lst):
    if target==0:
        return True
    elif target<0:
        return False
    for i in lst:
        k=target-i
        if cansum(k,lst):
            return True
    return False
print("\nbrute force")
print(cansum(7,[5,3,4,7]))
print(cansum(7,[1,2,3]))
print(cansum(7,[2,4]))

print("\n memoization")

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

print(mem_cansum(7,[5,3,4,7],{}))
print(mem_cansum(7,[1,2,3],{}))
print(mem_cansum(300,[7,14],{}))
