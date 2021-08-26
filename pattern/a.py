a="*"
c,d=2,3
for i in range(6):

    for j in range(5):
        if (i>2 and (j==0 or j==4)):
            print(a,end="")
        elif (i<=2 and j==c):
            print(a,end="")
            c-=1
        elif (0<i<=2 and j==d):
            print(a,end="")
            d+=1
            break
        elif i==2:
            print(a,end="")
        else:
            print(' ',end="")
    print()
