class Crypto:
    def __init__(self,str1,encrypt=[]):
        self.str1=str1
        self.encrypt=[0]*26
        j=4
        for i in range(26):
            if j+97>122:
                j=0
            self.encrypt[i]=chr(j+97)
            j+=1
        #print(self.encrypt)
    def encryption(self):
        a=list(self.str1)
        #print(a)
        b=[]
        for i in a:
            if not i!=" ":
                b.append(" ")
                continue
            c=abs(ord(i)-97)
            b.append(self.encrypt[c])
        return "".join(b)
    def __str__(self):
        return "{}".format(self.encryption())
str2="my name is vivek"
c1=Crypto(str2)
#c1.encryption("my name is vivek")
print(str2)
print(c1)
