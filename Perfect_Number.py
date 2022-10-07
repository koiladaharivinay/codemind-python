n=int(input())
a=0
temp=n
for i in range(1,n):
 if(temp%i==0):
  a=a+i
if(temp==a):
   print("True")
else:
   print("False")


