from contextlib import nullcontext
from numpy import str_
import pandas as pd
from openpyxl.workbook import workbook
from datetime import date
import os
import sys
from pandas.core.reshape.concat import concat

# total arguments
try:
    print("\nName of Python script:", sys.argv[0])
    n = len(sys.argv[1])
    print(n)
    if(n != 8):
        print("\nArguments passed:",+n)
        print("please pass valid report date<YYYYMMDD> parameter")
        sys.exit(1)
except IndexError:
    print("please pass valid parameter\n")
    print("example: py Fileread.py  <report_date>")
    sys.exit(1)

try:
    #today = date.today()
    #print ("Today's date",today)
    print("Read data from csv file EMP.CSV") #Data frame 
    df_csv = pd.read_csv('Emp.csv') #read Data frme from INput file 
    #print(df_csv)
    print("convert csv file to comma seperated csv file")
    file_name = "EMPDATA"
    #filename=file_name +"_" + str(today).replace('-', '') + ".csv"
    filename=file_name +"_" + str(sys.argv[1]) + ".csv"
    print(filename)
    df_csv.to_csv(r'outputfile.txt', sep = '|', index=False)
    print("its sucesfully convert csv file to comma seperated csv file")

    
    #renmaing file "output.txt to empdata <report_date> .csv"
    old_name = r"outputfile.txt"
    try:
        os.rename(old_name, filename)
        
    except FileExistsError:
        print("File already Exists")
        print("Removing existing file")
        # skip the below code
        # if you don't' want to forcefully rename
        os.remove(filename)
        # rename it
        os.rename(old_name, filename)
        print('Done renaming a file')
except:
    print("An exception occurred");

