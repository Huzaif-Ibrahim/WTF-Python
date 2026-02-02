class Stack():
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def isEmpty(self):
        return self.items == []
    def peek(self):
        return self.items[len(self.items)-1]
    def display(self):
        return self.items
    def size(self):
        return len(self.items)
    
s = Stack()
print("Elements: ", s.display())
print("Is empty: ",s.isEmpty())
print("---Push Operations---")
s.push(3)
s.push(21)
s.push(9)
print("Top element: ", s.peek())
print("size: ", s.size())
print("Elements: ", s.display())
print("Is empty: ",s.isEmpty())
print("---Pop Operations---")
s.pop()
s.pop()
print("Elements: ", s.display())