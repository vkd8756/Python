M=6
N=2
one=(M//N)

ty=[]
sy=[]

for i in range(M):
    a=input()
    if len(a) > 1:
        if a[0] == "T" :
            ty.append(a)
        elif a[0] == "S" :
            sy.append(a)
ty.sort()
sy.sort()
#print(ty,sy)
c=0
if len(ty)<M//2:
    for i in ty:
        if c + 1 != int(i[3:]):
            ty.insert(c, "absent")
        c += 1
    if len(ty)<M//2:
        ty.append("absent")
c=0
if len(sy)<M//2:
    for i in sy:
        if c + 1 != int(i[3:]):
            sy.insert(c, "absent")
        c += 1
    if len(sy)<M//2:
        sy.append("absent")
seat=[]
for i in range(len(sy)):
    seat.append(ty[i])
    seat.append(sy[i])
print(seat)
final=[]
#print(list(zip(ty,sy)))
c=0
while c<len(seat):
    final.append((seat[c:c+one]))
    c+=one
print(final)
'''TY01
TY03
SY01
SY02
SY03
TY05
TY04
SY04
TY02
SY05'''