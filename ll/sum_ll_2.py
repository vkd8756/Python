class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Ll:
    def __init__(self):
        self.head=None
    def append(self,x):
        temp=self.head
        new=Node(x)
        if not temp:
            self.head=new
            return
        while temp.next:
            temp=temp.next
        temp.next=new
    def pl(self):
        temp=self.head
        while temp:
            print(temp.data,end="")
            temp=temp.next
        print()
class Solution:
    def sum_list(self,lst1,lst2):
        p=lst1.head
        q=lst2.head
        sum_list=Ll()
        carry=0
        while p or q:
            if not p:
                i=0
            else:
                i=p.data
            if not q:
                j=0
            else:
                j=q.data
            s=i+j+carry
            if s>=10:
                remainder=s%10
                sum_list.append(remainder)
                carry=1
            else:
                sum_list.append(s)
                carry=0
            if p:
                p=p.next
            if q:
                q=q.next
        if carry:
            sum_list.append(carry)
        sum_list.pl()
l1=Ll()
l1.append(9)
l1.append(9)
l1.append(9)
l1.append(9)
l1.append(9)
l1.append(9)
l1.append(9)
l1.pl()
l2=Ll()
l2.append(9)
l2.append(9)
l2.append(9)
l2.append(9)
l2.pl()
c=Solution().sum_list(l1,l2)
