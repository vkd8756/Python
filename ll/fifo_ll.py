class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#lifo stack
#head==top
#pop=head
#push=end
class LL:
    def __init__(self):
        self.head=None
    #stack push
    def push(self,x):
        temp=self.head
        if temp is None:
            temp=Node(x)
            return
        while temp:
            if temp.next==None:
                new=Node(x)
                temp.next=new
                return
            temp=temp.next
    #stack pop
    def pop(self):
        temp=self.head.next
        #print("data",self.head.data)
        if temp is None:
            self.head=None
            return
        self.head.next=None
        self.head=temp
    def pl(self):
        temp=self.head
        if temp is None:
            print("empty")
        while temp:
            print(temp.data)
            temp=temp.next
if __name__=="__main__":
    l1=LL()
    l1.head=Node(1)
    l2=Node(2)
    l3=Node(3)
    l1.head.next=l2
    l2.next=l3
    l1.pl()
    print("\nafter stack push\n")
    l1.push(4)
    l1.pl()
    print("\nafter stack pop\n")
    for i in range(4):
        l1.pop()
        l1.pl()
        print()
