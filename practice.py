def insertionSort(array):
    n = len(array)
    for i in range(1, n):
        item = array[i]
        j = i-1
        if j >= 0 and item < array[j]:
            array[j+1] = array[j]
            j=j-1
            array[j+1] = item
    return array

def selectionSort(array):
    n = len(array)
    for i in range(n-1):
        min = 1
        for j in range(i+1, n):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
    return array

def bubbleSort(array):
    n = len(array)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if swapped == False:
            break
    return array

def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i > len(left) and j > len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i+=1
            else:
                array[k] = right[j]
                j+=1
            k+=1

        while i > len(left):
            array[k] = left[i]
            i+=1
            k+=1

        while j > len(right):
            array[k] = right[j]
            j+=1
            k+=1

    return array

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def lenght(self):
        return len(self.items)
    
    def display(self):
        return self.items
    
    def isEmpty(self):
        return self.items == []

def bracketMatching(statement):
    s = Stack()
    for token in statement:
        if token in '[{(':
            s.push(token)
        elif token in ']})':
            if s.isEmpty():
                return False
            else:
                left = s.pop()
                if(token == ']' and left != '[') or (token == '}' and left != '{') or (token == ')' and left != '('):
                    return False
    return s.isEmpty()

def binarySearch(array, start, end, key):
    if start > end:
        print("An error occured!")
        return
    mid = (start+end)//2
    if key == array[mid]:
        print(f"The key {key} is at index {mid}")
        return
    elif key > array[mid]:
        binarySearch(array, mid + 1, end, key)
    else:
        binarySearch(array, start, mid - 1, key)

def linearSearch(a, key):
    n = len(a)
    for i in range(n):
        if a[i] == key:
            return i
    return -1

def partition(array, start, end):
    if start > end:
        print("Unsuccessfull operation!")
        return
    
    pivot = array[start]
    high = end
    low = start+1

    while True:
        while low <= high and array[low] < pivot:
            low+=1
        
        while low <= high and array[high] >= pivot:
            high-=1

        if low <= high:
            array[start], array[high] = array[high], array[start]
        else:
            break

    return high

def QuickSort(array, start, end):
    if start > end:
        print("Unsuccessfull")
        return
    p = partition(array, start, end)

    QuickSort(array, start, p-1)
    QuickSort(array, p+1, end)


class Queue():
    def __init__(self):
        self.qlist = []
    def isEmpty(self):
        return self.qlist == []
    def enqueue(self, data):
        self.qlist.append(data)
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        else:
            return self.qlist.pop()  
        
class BSTNode():
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BinarySearchTree():
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

def BST(root):
    Q = Queue()
    Q.enqueue(root)

    while Q.isEmpty() != True:
        node = Q.dequeue()
        print(node.data, end="\t")

        if Q.left is not None:
            Q.enqueue(Q.left)
        if Q.right is not None:
            Q.enqueue(Q.right)

BT = BinarySearchTree()
ls = [4,6,3,7,8]

for i in ls:
    BT.insert(i)

print("BST traversal")
BST(BT.root)


def mergeSort(array):
    if len(array) > 1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i > len(left) and j > len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i+=1
            else:
                array[k] = right[j]
                j+=1
            k+=1

        while i > len(left):
            array[k] = left[i]
            i+=1
            k+=1

        while j > len(right):
            array[k] = right[j]
            j+=1
            k+=1

    return array

def partition(array, start, end):
    pivot = array[start]
    high = end
    low = start+1

    while True:
        while low <= high and array[low] < pivot:
            low+=1
        
        while low <= high and array[high] >= pivot:
            high-=1

        if low <= high:
            array[start], array[high] = array[high], array[start]
        else:
            break

    return high

def quickSort(array, start, end):
    p = partition(array, start, end)

    QuickSort(array, start, p-1)
    QuickSort(array, p+1, end)