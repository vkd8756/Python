n=int(input())
#b=list(map(int,input().split()))
b=[]
for i in range(n):
    b.append(int(input()))
print(b)
#n=4
#b=[10,20,30,40,50]
#b=[1,5,8,7]
#print(n,b)
c=[]
for i in range(len(b)):
    c.append(sum(b[i+1:]))
print(c)
for i in c:
    print(i,end=" ")
