#abcdef
#ab abc cd def abcd

def canconstruct(target,lst):
    if target=="":
        return True
    for i in lst:
        if i in target:
            if target.index(i)==0:
                k=target.replace(i,"")
                if canconstruct(k,lst):
                    return True
    return False
def mem_canconstruct(target,lst,memo):
    if target in memo:
        return memo[target]
    if target=="":
        return True
    for i in lst:
        if i in target:
            if target.index(i)==0:
                k=target.replace(i,"")
                if canconstruct(k,lst):
                    memo[target]=True
                    return True
    memo[target]=False
    return False
print("\nbrute force")
print(canconstruct("abcdef",['ab','abc','cd','def','abcd']))
print("\nmemoized")
print(mem_canconstruct("skateboard",['bo','rd','ate','t','ska','sk','boar'],{}))
