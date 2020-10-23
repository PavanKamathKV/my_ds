class inpix_To_Postpix():
    def __init__(self):
        self.top=-1
        self.array=[]
        self.precedence=0
        self.max=10

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
            print("Stack full!!")
            return
        self.top=self.top+1
        return self.array.append(data)

    def pop(self):
        if self.isEmpty():
            print("empty!!")
            return
        e=self.array.pop()
        self.top=self.top-1
        return e

    def printArray(self):
        for i in self.array():
            print(i)
        
    def getPrecedence(self):
        a={"+":1,"-":1,"*":2,"/":2,"^":3}
        return a

    def infix_Postfix(self,exp):
        a=self.getPrecedence()
        star=""
        for c in exp:
            if c.isalnum():
               star=star+c
            else:
                if c not in a.keys():
                    print("INvalid EXp!!")
                    return
                if self.isEmpty():
                    self.push(c)
                else:
                    if a[c] > a[self.array[self.top]]:
                        self.push(c)
                    else:
                        while not self.isEmpty() and a[c]<=a[self.array[self.top]]:
                            t=self.pop()
                            star=star+t
                        self.push(c)
        while not self.isEmpty():
            p=self.pop()
            star=star+p
        print(star)
        
exp="a+w-g*d-b"
i=inpix_To_Postpix()
i.infix_Postfix(exp)
