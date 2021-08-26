def allconsrtuct(target,lst):
    if target=="":
        return [[]]
    res=[]
    for i in lst:
        if i in target:
            if target.index(i)==0:
                k=target.replace(i,"",1)
                sways=allconsrtuct(k,lst)
                tways=[[i]+j for j in sways]
                res+=tways
                #print(res)
    return res
print(allconsrtuct("purple",["purp","p","ur","le","purpl"]))
