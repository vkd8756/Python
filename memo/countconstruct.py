print("\nbrute force")
def countconstruct(target,lst):
    if target=="":
        return 1
    count=0
    for i in lst:
        if i in target:
            if target.index(i)==0:
                k=target.replace(i,"")
                count_rest=countconstruct(k,lst)
                count+=count_rest
    return count
print(countconstruct("abcdef",['ab','abc','cd','def','abcd']))
print(countconstruct("purple",["purp","p","ur","le","purpl"]))
print("\nmemoization")
def mem_countconstruct(target,lst,memo):
    print(memo)
    if target in memo:
        return memo[target]
    if target=="":
        return 1
    count=0
    for i in lst:
        if i in target:
            if target.index(i)==0:
                k=target.replace(i,"")
                count_rest=mem_countconstruct(k,lst,memo)
                count+=count_rest
                memo[target]=count
    return count
print(mem_countconstruct("abcdef",['ab','abc','cd','def','abcd','ef'],{}))
print(mem_countconstruct("purple",["purp","p","ur","le","purpl"],{}))
print(mem_countconstruct("eeeeeeeeeeeeeeeeeeeeeeef",["e","eee","eeee","eeee","eeeef"],{}))
