class node:
    def __init__(self,data):
        data=none
        next=none
class singlylinkedlist:
    def __init__(self):
       self.head=none
    def display(self):
        temp=self.head
        while temp:
           print(temp.data,end='')
           temp=temp.next
    def insertbegin(self,data):
        newnode=node(data)
        if self.head is none:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def inserted(self,data):
        newnode=node(data)
        if self.head is none:
            self.head=newnode
        else:
            temp=slf.head
            while temp.next:
                temp=temp.next
            temp.next=newnode
    def search(self,target):
        if self.head is none:
            print("sll is empty")
        else:
            temp=self.head
            while temp:
                if temp.data==target:
                    print("found")
                else:
                    temp=temp.next
            else:
                  print("not found")
    def delbegin(self):
         if self.head is none:
             print("sll is empty")
         else:
             temp=self.head
             self.head=self.head.next
             temp.next=none
             del temp
    def delend(self):
        if self.head is none:
           print("sll is empty")
        else:
           temp=self.head
           while temp.next.next:
                temp=temp.next
                delnode=temp.next
                temp.next=none
                del delnode
    def length(self):
         c=0
         temp=self.head
         while temp:
             c+=1
             temp=temp.next
         print(c)
sll=singlytlinkedlist()         
sll.insertbegin(10)
sll.insertbegin(20)
sll.insertbegin(30)
sll.insertbegin(40)
sll.display()
print()
sll.insertend(15)
sll.insertend(25)
sll.insertend(35)
sll.display()
print()
sll.search(20)
sll.search(30)
sll.search(200)
sll.display()
print()
sll.delbegin()
sll.display()
print()
sll.delend()
sll.display()
print()



            
                        
