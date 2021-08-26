v=[60,100,120]
w=[10,20,30]
wt=50
n=3
t=[[-1 for i in range(wt+1)] for j in range(n+1)]
#print(t)
def knapsack(v,w,wt,n):
    #print(n,wt)
    #print(t[n][wt])
    if n==0 or wt==0:
        return 0
    if t[n][wt]!=-1:
        return t[n][wt]
    elif w[n-1]<=wt:
        #print(n)
        #print(type(knapsack(v,w,wt,n)))
        t[n][wt]=(max(v[n-1]+knapsack(v,w,wt-w[n-1],n-1),knapsack(v,w,wt,n-1)))
        return t[n][wt]
    elif w[n-1]>wt:
        #print("n",n)
        t[n][wt]=(knapsack(v,w,wt,n-1))
        return t[n][wt]

print(knapsack(v,w,wt,n))
print(t)
