def prison(n,m,s):
    return (((s-1+m-1)%n)+1)
if __name__=="__main__":
    a=int(input())
    for i in range(a):
        b=list(map(int,input().split()))
        n=b[0]
        m=b[1]
        s=b[2]
        print(prison(n,m,s))