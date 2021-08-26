arr=[2,3,7,8,10]
arr=[2,3,5,6,8,10]
sum=10
n=len(arr)
t=[[0 for i in range(sum+1)] for j in range(n+1)]
for i in range(n+1):
    for j in range(sum+1):
        if i==0:
            t[i][j]=0
        if j==0:
            t[i][j]=1
        elif j>=arr[i-1]:
            t[i][j]=t[i-1][j-arr[i-1]]+t[i-1][j]
        else:
            t[i][j]=t[i-1][j]
print(t[n][sum])
print(t)
