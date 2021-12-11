#this script convert csv file to pipe seperated csv file 
from contextlib import nullcontext
import numpy as np
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
    df_csv["Emp Name"] = df_csv["Name Prefix"] + df_csv["First Name"] + df_csv["Middle Initial"] + df_csv["Last Name"]
    print(df_csv["Emp Name"])
    df_csv.add(df_csv)
    #df_csv = df_csv.replace(r'Emp.csv',np.NaN, regex=True)
    #df_csv.to_csv('modified2.csv')
    df_csv.drop(columns="Name Prefix",inplace=True)
    df_csv.drop(columns="First Name",inplace=True)
    df_csv.drop(columns="Middle Initial",inplace=True)
    df_csv.drop(columns="Last Name",inplace=True)
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
print("script is completed sucessfully")

