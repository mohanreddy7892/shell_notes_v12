import collections
list1=[10,10.0,'python']
#slicing lists
#there are two types :
#forward slicing (index) start with 0
#backward slicing (index) start with -1
list=list1[-2]
print(list)
print(list)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b=a[:]
print(b)
print(a[::3])


List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 
# Show original list
print("\nOriginal List:\n", List)
 
print("\nSliced Lists: ")
 
# Display sliced list
print(List[3:9:2])

print(List[::2])
 
# Display sliced list
print(List[::])



# Initialize list
List = ['Geeks', 4, 'geeks !']

# Show original list
print("\nOriginal List:\n", List)

print("\nSliced Lists: ")

# Display sliced list
print(List[::-1])

# Display sliced list
print(List[::-3])

# Display sliced list
print(List[:1:-1])



# Initialize list
List = [-999, 'G4G', 1706256, '^_^', 3.1496]

# Show original list
print("\nOriginal List:\n", List)

print("\nSliced Lists: ")

# Display sliced list
print(List[10::2])

# Display sliced list
print(List[1:1:1])

# Display sliced list
print(List[-1:-1:-1])

# Display sliced list
print(List[:0:])





# Initialize list
List = [-999, 'G4G', 1706256, 3.1496, '^_^']
 
# Show original list
print("\nOriginal List:\n", List)
 
 
print("\nSliced Lists: ")
 
# Modified List
List[2:4] = ['Geeks', 'for', 'Geeks', '!']
 
# Display sliced list
print(List)

List[:6] = []
print(List)




