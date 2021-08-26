arr=[1,5,6,11]
#arr=[1,2,7]
sum=sum(arr)
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
print(t,"\n","TABLE")
a=t[n]
print(a)
v=[i for i in range(len(a)//2) if a[i]==True]
print(v)
mn=sum
range=sum
##print(range)
#print(v)
for i in v:
    mn=min(mn,range-(2*i))
print(mn)
