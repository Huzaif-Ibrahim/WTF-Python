class Queue:
    def __init__(self):
        self.qlist = []

    def IsEmpty(self):
        return len(self.qlist) == 0

    def Enqueue(self, item):
        self.qlist.append(item)

    def Dequeue(self):
        if self.IsEmpty():
            print("Queue is Empty")
        else:
            return self.qlist.pop(0)


class BSTNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = BSTNode(value)

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


def BFS(root):
    Q = Queue()
    Q.Enqueue(root)

    while Q.IsEmpty() != True:
        node = Q.Dequeue()
        print(node.data, end="\t")

        if node.left is not None:
            Q.Enqueue(node.left)

        if node.right is not None:
            Q.Enqueue(node.right)


BT = BinarySearchTree()

ls = [25, 10, 35, 20, 5, 30, 40]

for i in ls:
    BT.insert(i)

print("BFS Traversal")
BFS(BT.root)