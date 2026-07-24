class student:
    def __init__(self):
        self.lst=[]
    def accept(self):
        n=int(input("enter numbers"))
        self.lst.append(R)
        print(self.lst)
    def avg(self):
        total=0
        for R in self.lst:
            total=total+R
            avg=total//len
        return avg
    def maxx(self):
        max=self.lst[0]
        for R in self.lst:
            if R>max:
                max=R
        return max
    def minn(self):
        min=self.lst[0]
        for R in self.lst:
            if R<min:
                min=R
        return min
    def leng(self):
        count=0
        for i in range(len(self.lst)):
            count=count+1
        return count
            
obj=student()
obj.accept()
while True:
    print('1.avg')
    print('2.max')
    print('3.min')
    print('4.len')
    print('5.exit')
    chance=int(input('enter chance'))
    if chance==1:
        print("avgg: ",obj.avg())
    elif chance==2:
        print("minn: ",obj.minn())
    elif chance==3:
        print("maxx: ",obj.maxx())
    elif chance==4:
        print("leng: ",obj.leng())
    else:
        break

    

    
    
