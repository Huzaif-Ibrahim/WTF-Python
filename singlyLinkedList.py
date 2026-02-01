class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.first = None

    def prepend(self, data):
        newNode = Node(data)
        if self.first is None:
            self.first = newNode
        else:
            newNode.next = self.first
            self.first = newNode

    def removeFirst(self):
        if self.first is None:
            print("List is empty")
        else:
            current = self.first
            self.first = self.first.next
            print("The deleted element is :", current.data)

    def display(self):
        if(self.first == None):
            print("List is empty")
            return 
        else:
            current = self.first
            print("Your List : ")
            while(current):
                print(current.data, end = " ")
                current = current.next
                
    def search(self, item):
        if(self.first == None):
            print("List is empty")
            return 
        current = self.first
        found = False
        while current != None and not found:
            if current.data == self.item:
                found = True
                return current.data
            else:
                current = current.next
        
        if found:
            print("Item found")
        else:
            print("Item not found")
            
s1 = SinglyLinkedList()
while(True):
    choice = int(input("\n1-insert \n2-delete \n3-search \n4-disply \n5-exit \nEnter your choice : "))
    if(choice == 1):
        item = input("Enter the element to insert : ")
        s1.prepend(item)
        s1.display()
    elif(choice == 2):
        item = input("Enter the element to delete : ")
        s1.removeFirst(item)
        s1.display()
    elif(choice == 3):
        item = input("Enter the element to search : ")
        s1.search(item)
        s1.display()
    elif(choice == 4):
        s1.display()
    else:
        break
