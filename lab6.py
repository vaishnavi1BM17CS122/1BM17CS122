class validate:
    def __init__(self,string):
        self.check=string
    def func(self):
        for i in range(0,len(self.check)-1):
            if(self.check[i]=='('):
                if(self.check[i+1]==')'):
                    pass
                else:
                    print("not valid")
                    break
            elif(self.check[i]=='['):
                if(self.check[i+1]==']'):
                    pass
                else:
                    print("not valid")
                    break
            elif(self.check[i]=='{'):
                if(self.check[i+1]=='}'):
                    pass
                else:
                    print("not valid")
                    break
            if(self.check[len(self.check)-1]=='('or self.check[len(self.check)-1]=='{'or self.check[len(self.check)-1]=='['):

               print("not valid")
               return
            if(i==len(self.check)-2):
               print("valid")
while(1):
 str=input("enter the string")
 xyz=validate(str)
 xyz.func()
