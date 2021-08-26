n=7
b=[0, 0, 1, 0, 0, 1, 0]
#n=int(input())
#c=list(map(int,input().split()))
def count(target,lst,memo):
    if target in memo:
        return memo[target]
    if target==0:
        return [[0]]
    elif lst[target]==1 or target<0:
        return False
    res=[]
    sways=count(target-1,lst,memo)
    #print(sways)
    if sways:
        tways=[[target]+j for j in sways]
        res+=tways
        memo[target]=res
    sways2=count(target-2,lst,memo)
    if sways2:
        tways2=[[target]+j for j in sways2]
        res+=tways2
        memo[target]=res
    return res
a=count(6,b,memo={})
print(a)
print(len(min(a))-1)
