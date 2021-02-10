a=0
b=1
n=int(input("number of terms:"))
flag=0      #counter
if (n==0):
 print(0)
else:
 flag=1
 print(a,end=" ")
 while flag<n:
     print(b,end=" ")
     s=a+b
     a=b
     b=s
     flag+=1
