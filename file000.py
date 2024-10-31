#some code
import os
import sys
print(os.getcwd())
path="C:\\Users\\mohan\\OneDrive\\Desktop"
#change the directory 
os.chdir(path)
print(os.getcwd())

#create directory in path
# os.mkdir("My_notes")
dir_exits=os.path.exists("My_notes")
print(dir_exits)

def dir_exits_check(path,dir_name):
    return os.path.isdir(dir_name)

print(f"Dir_checking by using dir function :",dir_exits_check(path,"mynotes"))
if dir_exits_check==True:
    print("Directory is exists given path",path)
else:
    print("Directory does not exits in given path ",path)
    sys.exit (7)
