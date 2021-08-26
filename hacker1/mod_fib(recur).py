t1=0
t2=1
n=6
#t3=0+1*1=1
#t4=1+1*1=2
#t5=1+2*2=5
#tn=t(n-2)+t(n-1)**2
#[0,1,1,2,5,27]
table=[-1 for i in range(n+1)]
table[0]=0
print(table)
def mod_fib(n):
    if n==2 :
        table[2]=t2
        return t2
    elif n==1:
        table[1]=t1
        return t1
    elif table[n]!=-1:
        return table[n]
    table[n]=(mod_fib(n-2)+mod_fib(n-1)**2)
    return table[n]
print(mod_fib(6))
