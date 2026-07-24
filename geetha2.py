class deptstr:
    n=None
    def accept(self):
        self.n=int(input("enter the prices:"))
        total=0
        for i in range(self.n):
            prices=int(input("enter product prices:"))
            total=total+prices
        return total
    def calc(self):
        self.amt=self.accept()
        if self.amt>1000:
            dis=self.amt*0.1
            self.amt=self.amt-dis
            print("amt after dis")
            print(self.amt)
        elif self.amt>500 and self.amt<=1000:
            dis=self.amt*0.05
            self.amt=self.amt-dis
            print("amt after dis")
            print(self.amt)
        else:
            print("no dis")
            print(self.amt)
d1 = deptstr()
d1.calc()

        
        
        
        
