x=10
n=2
dp=[1] + [0]*x
print(dp)
c=0
#print(int(pow(x,1/n))+1)
for i in range(1,int(pow(x,1/n))+1):
    c+=1
    u=i**n
    print("c",c,u)
    for j in range(x,u-1,-1):
        dp[j]+=dp[j-u]
        #print(dp)
print("c",c)
print(dp)
print(dp[-1])