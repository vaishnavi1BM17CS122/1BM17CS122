print("enter the number of elements in the list")
n=int(input())
list1=[]
list2=[]
for i in range(n):
   
   list1.append(int(input()))
for i in list1 :
   if(i%2==0):
     list2.append(i)
print("list is:",list2)
