n=5
def harmonic(s):
    if s==1:
        return 1
    else:
        return (harmonic(s-1))+(1/(s))
print(harmonic(5))
#print((1/1)+(1/2)+(1/3)+(1/4)+(1/5))
print("\n====\nSeries--1/1!+2/2!+3/3!+..")
def fact_harm(s):
    if s==1:
        return 1
    else:
        return (fact_harm(s-1))+(s/fact(s))
def fact(n):
    if n==1 or n==1:
        return 1
    else:
        return n*fact(n-1)
#print(fact(4))
print(fact_harm(5))
