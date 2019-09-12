class student:
    def __init__(self):
        self.id=0
        self.age=0
        self.marks=0
    def set(self):
        print("enter id,age,marks")
        self.id=int(input())
        self.age=int(input())
        self.marks=int(input())
    def get(self):
        print("details:id",self.id,"age:",self.age,"marks:",self.marks)
    def validating_marks(self):
        if(self.marks<0 and self.marks>100):
            print("invalid marks")
            return "false"
        else:
            return "true"
    def validating_age(self):
        if(self.age>20):
            return "true"
        else:
            print("enter correct age")
            return "false"
    def check_qualification(self):
        if(self.validating_marks()=="true" and self.validating_age()=="true"):
            if(self.marks>=65):
                
                return "true"
            else:
                return "false"
        else:
            self.validating_marks()
            self.validating_age()
            return "false"
list=[]
n=int(input("enter number of students"))
for i in range(n):
    list.append(student())
for i in range(n):
    list[i].set()
    if(list[i].check_qualification()=="true"):
        list[i].get()
    else:
        print("not elligible")
    
     
    
