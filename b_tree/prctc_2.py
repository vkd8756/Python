class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Btree:
    def __init__(self):
        self.root=None
    def insert(self,x):
        new=Node(x)
        if not self.root :
            self.root=new
            return
        return self._insert(self.root,x)
    def _insert(self,cur,data):
        new=Node(data)
        if cur.data>data:
            if not cur.left:
                cur.left=new
            else:
                return self._insert(cur.left,data)
        elif cur.data<data:
            if not cur.right:
                cur.right=new
            else:
                return self._insert(cur.right,data)
        else:
            print("data already exists")
    def find(self,data):
        if self.root:
            is_found=self._find(data,self.root)
            if is_found:
                return True
            return False
        return None
    def _find(self,data,cur):
        if data==cur.data:
            return True
        elif data>cur.data and cur.right:
            return self._find(data,cur.right)
        elif data<cur.data and cur.left:
            return self._find(data,cur.left)

bst=Btree()
bst.insert(1)
bst.insert(2)
bst.insert(3)
print(bst.find(3))
