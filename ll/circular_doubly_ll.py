class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Cdll:
    def __init__(self):
        self.head=None
    def epush(self,x):
        temp=self.head
        new_node=Node(x)
        if not temp:
            self.head=new_node
            self.head.next=new_node
            self.head.prev=new_node
            return
        while temp.next!=self.head:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
        new_node.next=self.head
    def fpush(self,x):
        temp=self.head
        new_node=Node(x)
        if not temp:
            self.head=new_node
            self.head.next=new_node
            self.head.prev=new_node
            return
        while temp.next!=self.head:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
        new_node.next=self.head
        self.head=new_node
    def pop(self):
        temp=self.head
        if not temp.next:
            self.head=None
            self.next=None
            self.prev=None
            return
        while temp.next!=self.head:
            temp=temp.next
        temp.next=self.head.next
        self.head=self.head.next
        self.head.prev=temp
    def pop_item(self,x):
        temp=self.head
        if temp.data==x:
            self.pop()
            return
        while temp.data!=x and temp.next!=self.head:
            temp=temp.next
        if not temp:
            return
        prv=temp.prev
        nxt=temp.next
        prv.next=nxt
    def pl(self):
        temp=self.head
        while temp:
            print(temp.data,"-->",end="")
            temp=temp.next
            if temp==self.head:
                print(temp.data)
                break
if __name__=="__main__":
    cdll=Cdll()
    cdll.epush(1)
    cdll.pl()
    cdll.epush(2)
    cdll.pl()
    cdll.epush(3)
    cdll.epush(4)
    cdll.pl()
    cdll.pop()
    cdll.pl()
    cdll.pop_item(4)
    cdll.pl()
    cdll.fpush(5)
    cdll.pl()
