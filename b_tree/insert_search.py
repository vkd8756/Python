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
bst=Bst()
bst.insert(1)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(5)
print(bst.find(4))
