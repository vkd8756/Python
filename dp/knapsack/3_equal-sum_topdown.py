arr=[1,5,5,11]
#arr=[1,5,3]
#arr=[1,5]
n=len(arr)
sums=sum(arr)

if sums%2!=0:
    print(False)
else:
    sums=sums//2
    t=[[0 for i in range(sums+1)] for j in range(n+1)]
    for i in range(n+1):
        #print(t)
        for j in range(sums+1):
            if j==0 :
                t[i][j]=True
            elif i==0:
                t[i][j]=False
            elif j>=arr[i-1]:
                t[i][j]=t[i-1][j-arr[i-1]]
            else:
                t[i][j]=t[i-1][j]
    print(t[n][sums])
