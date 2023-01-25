#some code
list1=[7,8,10]
c=0
for i in range(list1[0],list1[-1]+1):
    if(list1[c]==i):
        c+=1
    else:
        print(i,end=" ")