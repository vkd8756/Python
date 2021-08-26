v=[60,100,120]
w=[10,20,30]
wt=50
n=3
def knapsack(v,w,wt,n):
    if (wt==0 or n==0):
        return 0
    elif w[n-1]<=wt:
        #print(n)
        #print(type(knapsack(v,w,wt,n)))
        return (max(v[n-1]+knapsack(v,w,wt-w[n-1],n-1),knapsack(v,w,wt,n-1)))
    elif w[n-1]>wt:
        #print("n",n)
        return (knapsack(v,w,wt,n-1))
print(knapsack(v,w,wt,n))
