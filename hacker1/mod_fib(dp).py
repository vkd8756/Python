t1=0
t2=1
n=6
#t3=0+1*1=1
#t4=1+1*1=2
#t5=1+2*2=5
#tn=t(n-2)+t(n-1)**2
#[0,1,1,2,5,27]
table=[0 for i in range(n+1)]
table[0]=0
for i in range(len(table)):
    if i==0:
        table[i]=0
    elif i==1:
        table[i]=t1
    elif i==2:
        table[i]=t2
    else:
        table[i]=table[i-2]+table[i-1]**2
print(table[n])
