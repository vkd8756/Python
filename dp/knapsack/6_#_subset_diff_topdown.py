arr=[1,1,2,3]
diff=1
sum=(diff + sum(arr))//2
#sum=4
n=len(arr)
t=[[0 for i in range(sum+1)] for j in range(n+1)]
for i in range(n+1):
    for j in range(sum+1):
        if i>=0 and j<=0:
            t[i][j]= 1
        elif i==0 and j>0:
            t[i][j]=  0
        elif arr[i-1]<=j:
            t[i][j]=t[i-1][j-arr[i-1]] + t[i-1][j]
        else:
            t[i][j]=t[i-1][j]
#print(11 in t[i][j])
print(t[n][sum])
