#some code
import glob
import sys
import os
import time
path=r"C:\Users\mohan\OneDrive\Desktop\Test\\"
file_name="test[4][0-9].txt"
def create_newfiles(path,file_name,number1,number2):
    files_list=glob.glob(path+file_name,recursive=False)
    #print(files_list)

    if len(files_list)==0:
        # print(files_list)
        for i in range(number1,number2):
            open(path+'test'+str(i)+'.txt','w').close()
        print("create new files in path")
        files_list2=glob.glob(path+file_name,recursive=False)
        print(files_list2)
        for i in files_list2:
        # print(i)
            file_name=os.path.basename(i)
            print(file_name)
    else:
        print("already files are crated")
        sys.exit(0)
create_newfiles(path,file_name,40,50)
