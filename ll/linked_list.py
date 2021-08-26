class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Ll:
    def __init__(self):
        self.head=None

    def append(self,x):
        new_node=Node(x)
        temp=self.head
        if not self.head:
            self.head=new_node
            return
        while temp.next:
            temp=temp.next
        temp.next=new_node
    def prepend(self,x):
        new_node=Node(x)
        if not self.head:
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node
    def pop(self):
        temp=self.head
        if not temp.next:
            self.head=None
            return
        self.head=self.head.next
    def pop_item(self,x):
        temp=self.head
        if x==temp.data:
            return self.pop()
        while temp.next and temp.data!=x:
            prev=temp
            temp=temp.next
        if temp is None:
            return
        prev.next=temp.next

    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data,"-->",end="")
            temp=temp.next
        print()

if __name__=="__main__":
    ll=Ll()
    ll.append(2)
    ll.print_list()
    ll.prepend(1)
    ll.print_list()
    ll.append(3)
    ll.append(4)
    ll.print_list()
    ll.pop()
    ll.print_list()
    ll.pop_item(4)
    ll.print_list()
