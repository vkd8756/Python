def ruler(maj_length,inches,n):
    if n%2==0:a,n=n//2,n-1
    else:a=n//2+1
    line(maj_length,"0")
    for i in range(1,1+inches):
        interval(n,a)
        line(maj_length,str(i))

def interval(n,a):
    if n>0:
        interval(n-1,a)
        if n==a:
            line(2)
        else:
            line(1)
        #interval(length-1)
def line(length,stri=""):
    line="-"*length
    if stri:
        line+=stri
    print(line)
print(ruler(4,2,5))
