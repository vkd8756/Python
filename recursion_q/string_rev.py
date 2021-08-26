a='racecar'
a=list(a)
b='racecaar'
def rever(s,start,stop):
    if start>stop:
        return
    elif start==stop-1:
        return s[start]
    else:
        s[start],s[stop-1]=s[stop-1],s[start]
        rever(s,start+1,stop-1)
    s="".join(s)
    return s
print(rever(a,0,len(a))==b)
