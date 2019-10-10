def overlapping(text1,text2):
    f=open(text1,'r')
    f1=open(text2,'r')
    string1=f.read()
    string2=f1.read()
    list1=[]
    list2=[]
    list1=string1.split(',')
    list2=string2.split(',')
    for i in list1:
        for j in list2:
            if i==j:
              print("overlappig")
              return
overlapping("text1","text2")           

