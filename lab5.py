class calldetail:
    #callfrom
    #callto
    #duration
    #calltype
    def __init__(self,cfrom,cto,time,ctype):
        self.callfrom=cfrom
        self.callto=cto
        self.duration=time
        self.calltype=ctype
    def print(self):
        print("call from:",self.callfrom,"\ncall to:",self.callto,"\nduration:",self.duration,"\ntype",self.calltype)
class util:
    #list_of_call_objects
    def __init__(self):
        self.list_of_call_objects=[]
    def parse_customer(self,list_of_call_string):
        for i in list_of_call_string:
            
            list1=i.split(",")
            #x=calldetail(list1[0],list1[1],list1[2],list1[3])
            self.list_of_call_objects.append(calldetail(list1[0],list1[1],list1[2],list1[3]))
        for i in self.list_of_call_objects:
            i.print()
list_of_call_string=[]
n=int(input("enter number of call details"))
for i in range(n):
    call=input("enter details in string format details seperated by comma")
    list_of_call_string.append(call)
util().parse_customer(list_of_call_string)
