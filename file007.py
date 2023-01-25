#some code
# list1=['a','b','c','d']
list1=[41,2,6,7,66,56,0]
n=len(list1)
print(n)
for i in range(n):
     print(i)
     for j in range(i+1,n):
          print(j)
          if list1[i]>list1[j]:
               list1[i],list1[j]=list1[j],list1[i]
               print(list1)

