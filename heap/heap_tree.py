class Stack:
    def __init__(self):
        self.items=[]
    def push(self,x):
        self.items.append(x)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    def peek(self):
        if not self.items:
            return self.items[-1]
    def is_empty(self):
        return len(self.items)==0
    def __len__(self):
        return self.size()
    def size(self):
        return len(self.items)
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
    def size(self):
        return len(self.items)
    def __len__(self):
        return self.size()
    def peek(self):
        if not self.is_empty():
            return self.items[-1].data
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self,root):
        self.root=Node(root)
    def insert(self,x):
        if not self.root:
            self.root=Node(x)
            return
        return self._insert(self.root,x)
    def _insert(self,cur_node,x):
        if cur_node.data>x:
            if not cur_node.left :
                cur_node.left=Node(x)
            else:
                self._insert(cur_node.left,x)
        elif cur_node.data<x:
            if not cur_node.right:
                cur_node.right=Node(x)
            else:
                self._insert(cur_node.right,x)
        else:
            print("data already exists")
    def print_tree(self,traversal_type):
        if traversal_type=="inorder":
            return self.inorder_print(self.root,"")
        elif traversal_type=="preorder":
            return self.preorder_print(self.root,"")
        elif traversal_type=="postorder":
            return self.postorder_print(self.root,"")
        elif traversal_type=="levelorder":
            return self.levelorder_print(self.root)
        elif traversal_type=="reverse levelorder":
            return self.rev_levelorder_print(self.root)
    def postorder_print(self,start,traversal):
        if start:
            traversal=self.postorder_print(start.left,traversal)
            traversal=self.postorder_print(start.right,traversal)
            traversal+=str(start.data)+"--"
        return traversal
    def inorder_print(self,start,traversal):
        if start:
            traversal=self.inorder_print(start.left,traversal)
            traversal+=str(start.data)+"--"
            traversal=self.inorder_print(start.right,traversal)
        return traversal
    def preorder_print(self,start,traversal):
        if start:
            traversal+=str(start.data)+"--"
            traversal=self.preorder_print(start.left,traversal)
            traversal=self.preorder_print(start.right,traversal)
        return traversal
    def levelorder_print(self,start):
        traversal=""
        if not start:
            return
        queue=Queue()
        queue.enqueue(start)
        while queue.__len__()>0:
            node=queue.dequeue()
            traversal+=str(node.data)+"--"
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal
    def rev_levelorder_print(self,start):
        if start is None:
            return
        queue=Queue()
        stack=Stack()
        queue.enqueue(start)
        traversal=""
        while queue.__len__()>0:
            node=queue.dequeue()
            stack.push(node.data)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        while stack.__len__()>0:
            node=stack.pop()
            traversal+=str(node)+"--"
        return traversal
    def height(self,node):
        if node is None:
            return -1
        left_height=self.height(node.left)
        right_height=self.height(node.right)
        return (1+max(left_height,right_height))
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
    def ancestor(self,start,target):
        if start is None:
            return False
        if start.data==target:
            return True
        if self.ancestor(start.left,target):
            print(start.data,end=" ")
            return True
        if self.ancestor(start.right,target):
            print(start.data,end=" ")
            return True
        return False
    def max_heap(self,start):
        if start is None:
            return
        queue=Queue()
        arr=[]
        queue.enqueue(start)
        traversal=""
        while queue.__len__()>0:
            node=queue.dequeue()
            arr.append(node.data)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        n=len(arr)//2
        for i in range(n,-1,-1):
            self._max_heapify(arr,i)
        print(arr)
    def _max_heapify(self,arr,i):
        l=2*i+1
        r=2*i+2
        largest=i
        if (l<len(arr) and arr[l]>arr[i]):
            largest=l
        if (r<len(arr) and arr[largest]<arr[r]):
            largest=r
        if largest!=i:
            arr[largest],arr[i]=arr[i],arr[largest]
            self._max_heapify(arr,largest)


if __name__=="__main__":
    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(4)
    tree.root.left.right=Node(5)
    #tree=BinaryTree()
    #tree.insert(4)
    #tree.insert(2)
    #tree.insert(5)
    #tree.insert(3)
    #tree.insert(1)
    print("preorder  ==> ",tree.print_tree("preorder"))
    print("postorder ==> ",tree.print_tree("postorder"))
    print("inorder   ==> ",tree.print_tree("inorder"))
    print("levelorder==> ",tree.print_tree("levelorder"))
    print("revlevorder==>",tree.print_tree("reverse levelorder"))
    print("Height of tree is ",tree.height(tree.root))
    print("Size of tree is ",tree.size())
    print("ancestors of 3 is/are ",end=" ")
    tree.ancestor(tree.root,3)
    tree.max_heap(tree.root)
