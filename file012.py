# some code

list1 = ['ammo', 'sam', 'kiran', 'narayan', 'Narayan', 'zeo', 'Ammo']
print("reverse:", sorted(sorted(list1, reverse=True), key=str.lower))

print("upper first:", sorted(list1))

# Convert a list with strings all to lowercase or uppercase

list_lower = map(str.upper, list1)
print(list(set(list(list_lower))))
