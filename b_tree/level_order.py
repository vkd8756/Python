class Queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,x):
        self.items.insert(0,x)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items)==0
    def peek(self):
        return self.items[-1].value
    def __len__(self):
        return self.size()
    def size(self):
        return len(self.items)
#q=Queue()
#q.enqueue(1)
#q.enqueue(2)
#q.enqueue(3)
#q.dequeue()

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class Bst:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            self._insert(data,self.root)
    def _insert(self,data,cur_node):
        if data>cur_node.value:
            if cur_node.right is None:
                cur_node.right=Node(data)
            else:
                self._insert(data,cur_node.right)
        elif data<cur_node.value:
            if cur_node.left is None:
                cur_node.left=Node(data)
            else:
                self._insert(data,cur_node.left)
        else:
            print("data already exists")
    def find(self,data):
        if self.root:
            is_found=self._find(data,self.root)
            if is_found:
                return True
            return False
        else:
            return None
    def _find(self,data,cur_node):
        if data>cur_node.value and cur_node.right:
            return self._find(data,cur_node.right)
        elif data<cur_node.value and cur_node.left:
            return self._find(data,cur_node.left)
        if data==cur_node.value:
            return True
    def levelorder_print(self,start):
        traversal=""
        if start is None:
            return
        queue=Queue()
        queue.enqueue(start)
        while queue.__len__()>0:
            traversal += str(queue.peek())+"-"
            node=queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal
bst=Bst()
bst.insert(2)
bst.insert(1)
bst.insert(5)
bst.insert(4)
bst.insert(6)
print(bst.find(4))
print(bst.levelorder_print(bst.root))
