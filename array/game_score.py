class Game:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def get_name(self):
        return self.name
    def get_score(self):
        return self.score
    def __str__(self):
        return "Name--{} score--{}".format(self.name.upper(),self.score)

class ScoreCard:
    def __init__(self,capacity=5):
        self.size=0
        self.scores=[None]*capacity
    def __getitem__(self,k):
        return self.scores[k]
    def str (self):
        return "\n".join(str(self.scores[j]) for j in range(self.size))
    def add_item(self,entry):
        scored=entry.get_score()
        good=self.size<len(self.scores)
        if good:
            self.size+=1
            j=self.size-1
            #print(j)
            if j>0:
                while j>0 and self.scores[j-1].get_score()<scored:
                    self.scores[j]=self.scores[j-1]
                    j-=1
                self.scores[j]=entry
            else:
                self.scores[j]=entry
    def pl(self):
        for i in self.scores:
            if i!=None:
                print(i)
p1=Game("vkd",90)
#print(p1)
p2=Game("vkd1",80)
#print(p2)
p3=Game("vkd2",100)
#print(p3)
p4=Game("vkd3",70)
#print(p4)
p5=Game("vkd4",110)
#print(p5)
p6=Game("vkd5",120)
#print(p6)
s1=ScoreCard()
s1.add_item(p1)
s1.pl()
s1.add_item(p2)
s1.add_item(p3)
s1.pl()
s1.add_item(p4)
s1.add_item(p5)
s1.pl()
s1.add_item(p6)
print("======")
s1.pl()
