def fib(num):
 count=0
 a=0
 b=1
 if num==1:
   print(0)
 else:
   print(a)
   print(b)
   while(count<num):
      c=a+b
      print(c)
      a=b
      b=c
      count=count+1
print("enter the value of n")
ele=int(input())
fib(ele)
 
