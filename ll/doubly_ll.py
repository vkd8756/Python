class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Dll:
    def __init__(self):
        self.head=None

    def fpush(self,x):
        new_node=Node(x)
        self.head.prev=new_node
        new_node.next=self.head
        self.head=new_node


    def epush(self,x):
        new_node=Node(x)
        temp=self.head
        if not temp:
            self.head=new_node
            return
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp

    def pop(self):
        temp=self.head
        if not temp:
            self.head=None
            self.prev=None
            self.next=None
            return
        self.head=self.head.next
        self.head.prev=None
    def pop_item(self,x):
        temp=self.head
        if self.head.data==x:
            return self.pop()
        while temp.next and temp.data!=x:
            temp=temp.next
        if temp.data!=x:
            return
        prv=temp.prev
        nxt=temp.next
        prv.next=nxt
        nxt.prev=prv


    def pl(self):
        temp=self.head
        while temp:
            print(temp.data,"-->",end="")
            temp=temp.next
            if temp==self.head:
                print(temp.data)
                break
        print()
if __name__=="__main__":
    dll=Dll()
    dll.epush(2)
    dll.pl()
    dll.epush(3)
    dll.pl()
    dll.epush(4)
    dll.pl()
    dll.fpush(1)
    dll.pl()
    dll.pop()
    dll.pl()
    print("\nafter poping")
    dll.pop_item(2)
    dll.pl()
