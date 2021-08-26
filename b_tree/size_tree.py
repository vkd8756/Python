#         1
#      /    \
#     2      3
#    / \    / \
#  4   5  6   7
class Stack:
    def __init__(self):
        self.items=[]
    def push(self,x):
        self.items.append(x)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items)==0
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def __len__(self):
        return self.size()
    def size(self):
        return len(self.items)
#Queue class for level order traversal
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

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self,root):
        self.root=Node(root)
    def print_tree(self,traversal_type):
        if traversal_type=="preorder":
            return self.preorder_print(self.root,"")
        elif traversal_type=="inorder":
            return self.inorder_print(tree.root,"")
        elif traversal_type=="postorder":
            return self.postorder_print(tree.root,"")
        elif traversal_type=="levelorder":
            return self.levelorder_print(tree.root)
    def preorder_print(self,start,traversal):
        #root-left-right
        if start:
            traversal +=(str(start.value)+"-")
            traversal=self.preorder_print(start.left,traversal)
            traversal=self.preorder_print(start.right,traversal)
        return traversal
    def inorder_print(self,start,traversal):
        #left-root-right
        if start:
            traversal=self.inorder_print(start.left,traversal)
            traversal+=(str(start.value)+"-")
            traversal=self.inorder_print(start.right,traversal)
        return traversal
    def postorder_print(self,start,traversal):
    #    left-right-root
        if start:
            traversal=self.postorder_print(start.left,traversal)
            traversal=self.postorder_print(start.right,traversal)
            traversal+=(str(start.value)+"-")
        return traversal
    def levelorder_print(self,start):
    # moving on after printing each level
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
    def size(self):
        if not self.root:
            return 0
        stack=Stack()
        stack.push(self.root)
        size=1
        while stack:
            node=stack.pop()
            if node.left:
                size+=1
                stack.push(node.left)
            if node.right:
                size+=1
                stack.push(node.right)
        return size
tree=BinaryTree(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)
print("\npreorder")
print(tree.print_tree("preorder"))
print("\ninorder")
print(tree.print_tree("inorder"))
print("\npostorder")
print(tree.print_tree("postorder"))
print("\nlevel order")
print(tree.print_tree("levelorder"))
print("\nsize of tree")
print(tree.size())
