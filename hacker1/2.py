def getWays(sums,arr,n):
    for i in range(n+1):
        for j in range(sums+1):
            if j==0:
                table[i][j]=1
            #elif j<=0:
            #    table[i][j]=0
            elif i<=0:
                table[i][j]=0
            elif arr[i-1]<=j :
                table[i][j]=table[i][j-arr[i-1]] +table[i-1][j]
            else:
                table[i][j]=table[i-1][j]
    #print(table)
    return table[n][sums]
sums=18
arr=[49, 9, 40, 17, 46, 24, 42, 26, 43, 41, 35, 1, 47, 28, 20, 38, 2, 44, 32, 22, 18, 45, 25]
#sums=4
#arr=[1,2,3]
n=len(arr)
table=[[0 for i in range(sums+1)] for j in range(n+1)]
print(getWays(sums,arr,n))
print(table)
