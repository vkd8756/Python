a=[1,1,2,2,3,3,4,4]
#a=[0,1,1,2,2,2,3,3,3,3]
cnt_one=0
cnt_two=0
cnt_three=0
cnt_four=0
cab=0
a.sort()
for i in a:
    if i==1:cnt_one+=1
    elif i==2:cnt_two+=1
    elif i==3:cnt_three+=1
    elif i==4 : cnt_four+=1
#print(cnt_one,cnt_two,cnt_three,cnt_four)
cab+=cnt_four
while (cnt_three!=0 and cnt_one!=0):
    cab+=1
    cnt_three-=1
    cnt_one-=1
while (cnt_three!=0 and cnt_one==0):
    cab+=cnt_three
    cnt_three=0
cab+=cnt_two//2
if cnt_two%2!=0:
    if cnt_one<=2:
        cnt_two=0
        cab+=1
        cnt_one=0
    else:
        cnt_one-=2
        cnt_two=0
if cnt_one!=0:
    cab+=cnt_one//4
    if cnt_one%4!=0:
        cab+=1

print(cab)