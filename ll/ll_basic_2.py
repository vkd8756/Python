class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,x):
        new=Node(x)
        temp=self.head
        if self.head is None:
            self.head=new
            return
        while temp:
            if temp.next==None:
                temp.next=new
                return
            temp=temp.next
    def pl(self):
        temp=self.head
        if temp is None:
            print("empty")
        while temp!=None:
            print(temp.data)
            temp=temp.next
if __name__=='__main__':
    llist=LinkedList()
    llist.pl()
    print("\nafter push\n")
    llist.push(4)
    llist.pl()
    print("\nafter push\n")
    llist.push(5)
    llist.pl()
