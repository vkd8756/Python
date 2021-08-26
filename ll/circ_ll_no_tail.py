class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CLl:
    def __init__(self):
        self.head=None
        self.size=1
    def push(self,x):
        new=Node(x)
        temp=self.head
        if not temp:
            self.head=new
            new.next=self.head
            self.size+=1
            return
        while temp.next!=self.head:
            temp=temp.next
        temp.next=new
        new.next=self.head
    def pop(self):
        if self.head.next is None:
             self.head=None
             self.size=0
             return
        temp=self.head
        while temp.next!=self.head:
            temp=temp.next
        self.head=self.head.next
        temp.next=self.head
        self.size-=1
    def pl(self):
        temp=self.head
        while temp:
            #print("temp",temp.data)
            print(temp.data,"-->",end="")
            temp=temp.next
            if temp==self.head:
                print(temp.data)
                break
        print()
if __name__ =="__main__":
    cll1=CLl()
    #cll1.head=Node(1)
    cll1.pl()
    print("\nafter push\n")
    cll1.push(1)
    cll1.push(2)
    cll1.pl()
    cll1.push(3)
    cll1.pl()
    cll1.push(4)
    cll1.pl()
    print("\nafter pop\n")
    cll1.pop()
    cll1.pl()
    #print()
    #cll1.circ()
    print("\nFinal List\n")
    cll1.pl()
