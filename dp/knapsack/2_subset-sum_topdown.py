arr=[2,3,7,8,10]
sum=11
n=len(arr)
t=[[0 for i in range(sum+1)] for j in range(n+1)]
for i in range(n+1):
    for j in range(sum+1):
        if i>=0 and j<=0:
            t[i][j]= True
        elif i==0 and j>0:
            t[i][j]=  False
        elif arr[i-1]<=j:
            t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
        else:
            t[i][j]=t[i-1][j]
#print(11 in t[i][j])
print(t[n][sum])
print(t)
