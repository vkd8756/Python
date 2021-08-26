
def fn(x,c,n):
    if pow(n,c)<x:
        return(fn(x,c,n)+fn(x-pow(n,c),c,n+1))
    elif pow(n,c)==x:
        return 1
    else :
        return 0

if __name__=='__main__':
    x = 10
    c = 2
    n = 1
    print(fn(x,n,c))

'''for i in range(10):
    d+=1
    print(pow(d,2))'''
