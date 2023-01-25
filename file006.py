#some code

s="i.like.this.program.very.much"
print("1-->",'.'.join(s.split('.')[::-1])) #without bulitin methods
print("2-->",'.'.join(reversed(s.split('.')))) #with build in methods

#function
def reverse_string(s):
    return '.'.join(reversed(s.split('.')))
print("3-->",reverse_string(s))