class Stack:
    def __init__(self):
        self.top=-1
        self.array=[]
        self.max=5

    def isEmpty(self):
        if self.top==-1:
            return True
        return False

    def isFull(self):
        if self.top==self.max-1:
            return True
        return False

    def push(self, data):
        if self.isFull():
            print("full ")
            return 
        self.top=self.top+1
        return self.array.append(data)

    def pop(self):
        if self.isEmpty():
            print("empty")
            return
        self.top-=1
        return self.array.pop()
    
    def printStack(self):
        for i in self.array:
            print(i)


s=Stack()
for g in range(4):
    s.push(g)
c=s.pop()
d= s.pop()
print(c,d)
s.printStack()
