class Queue: 
    def __init__(self): 
        self.qlist=[] 
    def IsEmpty(self): 
        return len(self.qlist)==0 
    def Enqueue(self,item): 
        print("The data item inserted is",item) 
        self.qlist.append(item) 
    def Dequeue(self): 
        if self.IsEmpty(): 
            print("Queue is Empty") 
        else: 
            del_item=self.qlist.pop(0) 
            print("The deleted item is:",del_item) 
 
    def display(self): 
        if self.IsEmpty(): 
            print("Queue is empty") 
        else: 
            print(self.qlist) 
 
queue=Queue() 
while True: 
    choice=int(input("Enter your choice: 1.Insert  2. Delele 3. Display 4. Exit : ")) 
    if choice==1: 
        item=input("Enter the item to be inserted:") 
        queue.Enqueue(item) 
    elif choice==2: 
        queue.Dequeue() 
    elif choice==3: 
        queue.display() 
    else: 
        break