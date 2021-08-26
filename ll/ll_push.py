class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,x):
        temp=self.head
        if temp is None:
            temp=Node(x)
            return
        new_node=Node(x)
        while temp.next:
            temp=temp.next
        temp.next=new_node
    def fpush(self,x):
        temp=self.head
        if temp is None:
            temp=Node(x)
            return
        self.head=Node(x)
        self.head.next=temp
    def bpush(self,prev_node,x):
        new_node=Node(x)

        new_node.next=prev_node.next
        prev_node.next=new_node


    def pl(self):
        temp=self.head

        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()
if __name__=='__main__':
    llist=LinkedList()
    llist.head=Node(1)
    second=Node(2)
    third=Node(3)
    #llist.pl()
    llist.head.next=second
    #llist.pl()
    second.next=third
    llist.pl()
    llist.push(4)
    llist.pl()
    llist.fpush(5)
    llist.pl()
    llist.bpush(third,6)
    llist.pl()