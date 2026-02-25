class Stack1:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    
class BTSNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        newNode = BTSNode(value)
        if self.root is None:
            self.root = newNode
        else:
            curNode = self.root
            while curNode is not None:
                if value < curNode.data:
                    if curNode.left is None:
                        curNode.left = newNode
                        break
                    else:
                        curNode = curNode.left
                else:
                    if curNode.right is None:
                        curNode.right = newNode
                        break
                    else:
                        curNode = curNode.right
                        
def DFS(root):
    s = Stack1()
    s.push(root)
    while s.isEmpty() != True:
        node = s.isEmpty()
        print(node.data, end='\t')
        if node.right is not None:
            s.push(node.right)
        if node.left is not None:
            s.push(node.left)
            
BT = BinarySearchTree()

ls = [25, 10, 35, 20, 5, 30, 40]
for i in ls: BT.insert(i)
print("DFS Traversal")
DFS(BT.root)
    