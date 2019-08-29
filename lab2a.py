def search(num,list):
  if num in list:
     print("found")
  else:
     print("not found")
list1=[]
a=input("enter number of elemnts")
for i in range(a):
  item=int(input())
  list1.append(item)
ele=input("enter element to be searched")
search(ele,list1)
