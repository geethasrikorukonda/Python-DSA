class employee:
    ecode = None
    ename = None
    monthlysal = None
    def accept(self):
        self.ecode = input("ecode")
        self.ename = input("ename")
        self.monthlysal = int(input("monthlysal"))
    def calclsal(self):
        self.yearlysal = self.monthlysal*12
    def display(self):
        print(self.ecode)
        print(self.ename)
        print(self.monthlysal)
        print(self.yearlysal)
e1 = employee()
e1.accept()
e1.calclsal()
e1.display()
