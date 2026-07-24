Class Node:
    def__init__(self,data):
        self.data=data
        self.next=None
class stackll:
    def__init__(self):
        self.top=None
    def isempty(self):
        if self.top is None:
            return True
        else:
            return false:
    def push(self,data):
        newNode=Node(data)
        if self.isempty():
            self.top=newNode
        else:
            newNode.next=self.top
            self.top=newNode
    def pop(self):
        if self.isempty():
            retun-1
        else:
            delNode=self.top
            popped=delNode.data
            self.top=self.top.next
            delNode.next=None
            del delNode
            return popped
    def peek(self):
        if self.isempty():
            return-1
        else:
            return self.top.data
    def display(self):
        if self.isempty():
            print("st isempty")
        else:
            temp=self.top
            while temp:
                print(temp.data)
                print('------')
                temp=temp.next
                print()
    def search(self.target):
        if self.isempty():
            print("empty")
        else:
            temp=self.top
            while temp:
                if temp.data==target:
                    print("found")
                    break
               else:
                   temp=temp.next
           else:
               print('not found")
s1=stackll()
while true:
    print('---operation---')
    print('1.push')
    print('2.pop')
    print('3.peek')
    print('4.display')
    print('5.search')
    print('6.exit')
    option=int(input("enter operation"))
    if option==1:
        ele=int(input('enter ele: "))
        s1.push(ele)
    elif option==2:
        res=s1.pop()
        if res!==1:
            print(f'popped:{res}')
        else:
            print9'under flow")
    elif option==3:
        res=s1.peek()
        if res==1:
            print("under flow")
        else:
            print(f'top ele is:{res}')
    elif option==4:
        s1.display()
    elif option==5:
        target=int(input("search for:"))
            s1.search(target)
    elif option==6:
        break
    else:
        print("enter vaild option")
          
                
                
