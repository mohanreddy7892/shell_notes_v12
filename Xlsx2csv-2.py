import os
import pandas as pd
import sys

# Check if the file name argument was provided
if len(sys.argv) < 2:
    print("Please provide a file name.")
    sys.exit(5)

file_names_path = sys.argv[1]

# A dictionary to store the variable assignments
variables = {}

# Check if the file exists
if os.path.isfile(file_names_path):
    with open(file_names_path, 'r') as file:
        for line in file:
            # Skip lines starting with '#'
            if line.strip().startswith('#'):
                continue
            name, value = line.strip().split('=')
            variables[name] = value
else:
    print("File does not exist.")
    sys.exit(1)

# Check if the necessary variables exist
required_variables = ['Input_path', 'Output', 'xlsx_filename', 'Csv_filename']
if not all(var in variables for var in required_variables):
    print("The text file does not contain all the necessary variables.")
    sys.exit(6)

file_path = os.path.join(variables['Input_path'], variables['xlsx_filename'])
csv_file_path = os.path.join(variables['Output'], variables['Csv_filename'])

# Check if the xlsx file exists
if os.path.isfile(file_path):
    try:
        # If the file exists, read the Excel file
        df = pd.read_excel(file_path)
        
        # Check if the .xlsx file has data or not
        if df.empty:
            print("The Excel file is empty.")
            sys.exit(4)
            
        # Convert to .csv file with comma as separator
        df.to_csv(csv_file_path, index=False, sep=',')
        
        # Check if the .csv file has data or not
        if os.path.getsize(csv_file_path) > 0:
            print("Conversion to CSV completed successfully.")
        else:
            print("The CSV file is empty.")
            sys.exit(2)
            
    except PermissionError:
        print("Permission denied. Please ensure you have the necessary access rights.")
        sys.exit(3)
    except Exception as e:
        print("Error occurred while converting the file: ", str(e))
        sys.exit(1)
else:
    print("The Excel file does not exist.")
    sys.exit(1)
