import time
a=[41,42,43,45,49]
print(a[::-1])
for i in a:
    a=i/7+2
    #print(a)
    a=float(a)
    if a%2==0:
        print("result is..")
        time.sleep(2)
        print(i,"--->",a,"yes")

