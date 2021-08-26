r=[13,14,20,11,22,17,19,22]
a=[]
y=[]
while len(a)<3:
    t=max(r)
    if t<22:
        a.append(t)
    r.remove(t)
    if t>=22:
        y.append(t)
print(a)
if len(y)<=2:
    print(y)
