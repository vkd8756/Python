v=[60,100,120]
w=[10,20,30]
wt=50
n=3
t=[[0 for j in range(wt+1)] for i in range(n+1)]
#print(t)
for i in range(n+1):
    for j in range(wt+1):
        if i==0 or j==0:
            t[i][j]=0
        elif w[i-1]<=j:
            t[i][j]=max(v[i-1]+t[i-1][j-w[i-1]],t[i-1][j])
        else:
            t[i][j]=t[i-1][j]
print(t[n][wt])
