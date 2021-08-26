sum=0
while True:
    print("MENU")
    print("A: drinks" '\n' "B: sweets" "\n" "C: food" "\n""Q: quit")


    a = input(":")
    if a == "A":
        print("A: pepsi""\n""B: cold drink""\n""C: Fanta")
        b=input(":")
        if b=="A":
            sum+=10
        elif b=="B":
            sum+=20
        elif b=="C":
            sum+=30
    elif a == "B":
        print("A: ladoo""\n""B: kitkat""\n""C: barfi")
        b = input(":")
        if b=="A":
            sum+=10
        elif b=="B":
            sum+=20
        elif b=="C":
            sum+=30
    elif a == "C":
        print("A: roti""\n""B: chawal""\n""C: sabji")
        b = input(":")
        if b == "A":
            sum+=10
        elif b == "B":
            sum+=20
        elif b == "C":
            sum+=30
    else:
        break
    print("amount: ",sum)
print("total amount is :", sum)


