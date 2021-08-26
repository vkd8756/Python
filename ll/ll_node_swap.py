class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LL:
    def __init__(self):
        self.head=None
    def fpush(self,x):
        new=Node(x)
        if self.head is None:
            self.head=new
            return
        new.next=self.head
        self.head=new
    def epush(self,x):
        temp=self.head
        while temp:
            if temp.next==None:
                new=Node(x)
                temp.next=new
                return
            temp=temp.next
    def bpush(self,prev_data,x):
        temp=self.head
        while temp:
            if temp.data==prev_data:
                break
            temp=temp.next
        new_node=Node(x)
        new_node.next=temp.next
        temp.next=new_node
    def swap(self,key_1,key_2):
        if key_1==key_2:
            return
        prev_1=None
        temp_1=self.head
        while temp_1 and temp_1.data != key_1:
            prev_1=temp_1
            temp_1=temp_1.next
        prev_2=None
        temp_2=self.head
        while temp_2 and temp_2.data != key_2:
            prev_2=temp_2
            temp_2=temp_2.next
        if not temp_1 or not temp_2:
            return
        #print("prev1",prev_1.data,"prev2",prev_2.data,"temp",temp_1.data,"temp_2",temp_2.data)
        if prev_1:
            prev_1.next=temp_2
        else:
            self.head=temp_2
        if prev_2:
            prev_2.next=temp_1
        else:
            self.head=temp_1
        temp_1.next,temp_2.next=temp_2.next,temp_1.next
    def pl(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
if __name__=="__main__":
    l1=LL()
    l1.fpush(1)
    l1.epush(2)
    l1.pl()
    print("\nafter front push\n")
    l1.epush(4)
    l1.pl()
    print("\nafter end push\n")
    l1.epush(5)
    l1.pl()
    #print("\nafter between push\n")
    #l1.bpush(4,6)
    #l1.pl()
    print("\nafter swapping\n")
    l1.swap(1,4)
    l1.pl()
