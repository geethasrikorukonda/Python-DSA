class stack:
    def __init__(self):
        self.st=[]
    def isempty(self):
        if self.st==[]:
            return True
        else:
            return False
    def push(self,X):
        self.st.append(X)
    def pop(self):
        if self.isempty():
            return-1
        else:
            popped=self.st.pop()
            return popped
    def peek(self):
        if self.isempty():
            return-1
        else:
            return self.st[-1]
    def display(self):
        if self.isempty():
            print("stack is empty")
        else:
            for i in range(len(self.st)-1,-1,-1):
                print(self.st[i])
                print('------')
                print()
    def search(self,target):
        if self.isempty():
            print("empty")
        else:
            for i in range(len(self.st)-1,-1,-1):
                if self.st[i]==target:
                    print("found")
                    break
s1=stack()
while True:
    print('---operations---')
    print('1.push')
    print('2.pop')
    print('3.peek')
    print('4.display')
    print('5.search')
    print('6.exit')
    option=int(input("enter operation"))
    if option==1:
        ele=int(input("enter ele:"))
        s1.push(ele)
    elif option==2:
        res=s1.pop()
        if res!=-1:
            print(f'popped:{res}')
        else:
            print("underflow")
    elif option==3:
        res=s1.peek()
        if res==-1:
            print("underflow")
        else:
            print(f'top ele is={res}')
    elif option==4:
        s1.display()
    elif option==5:
        s1.search()
    elif option==6:
        break
    else:
        print("enter valid option")
   
    
        
        
             
    
