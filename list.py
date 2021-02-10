list=[]
nlist=[] #list to store positive elements
n=int(input("number of elements:"))
for i in range(0,n):  #input using for loop
  i=int(input())
  list.append(i)
print(f"Input:{list}")
for j in range(0,n):  #accessing elements in list using for loop
  if (list[j]>0):
    nlist.append(list[j])
print(f"Output:{nlist}")
