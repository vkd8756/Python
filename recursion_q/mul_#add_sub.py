a,b=2,4
def mul(x,y):
    if y==1:
        return x
    else:
        return x+mul(x,y-1)
print(mul(a,b))
