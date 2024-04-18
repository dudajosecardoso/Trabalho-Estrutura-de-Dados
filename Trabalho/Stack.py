class List:
    def __init__(self,data=None):
        self.data = data
        self.next= None

class Stack:
    def __init__(self):
        self.top= None

    def push(self,data):
        node= List(data)
        if self.top is not None:
            node.next= self.top
        self.top=node

    def pop(self):
        if self.top is not None:
            data= self.top.data
            self.top= self.top.next
            return data
        
    def peek(self):
        if self.top is not None:
            return self.top.data
        
    def empty(self):
        return self.top is None
    
    def size(self):
        count= 0
        current= self.top

        while current is not None:
            count+= 1
            current= current.next
        return count
