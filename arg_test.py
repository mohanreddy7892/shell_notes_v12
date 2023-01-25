from os import system
import sys
import getopt
from wsgiref.simple_server import sys_version
import platform
hostname = platform.uname()
print(hostname)
print(sys_version)
n=len(sys.argv)
print(f"Total  arugements passed",n)
print("\nName of python script",sys.argv[0])
for i in range(1,n):
    print(sys.argv[i],end=" ")
    
if n == 4:
    print("its valid parameters")
else:
    print("pleas pass valid arguments\nits not valid argument \nretun exit 8")
    sys.exit(8)
    
    
    

