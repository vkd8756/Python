def sub(arr,d,m):
    count=0
    if m==1 :
        return s.count(d)
    for i in range(len(s)-m+1):
        if sum(s[i:i+m])==d:
            count+=1
    return count
if __name__=="__main__":
    arr=[1,2,1,3,2]
    d=3
    m=2
    print(sub(arr,d,m))
