import os
import pandas as pd
import sys

file_path = 'your_file.xlsx'
csv_file_path = 'your_file.csv'

# Check if the file exists
if os.path.isfile(file_path):
    try:
        # If the file exists, read the Excel file and convert to .csv
        df = pd.read_excel(file_path)
        df.to_csv(csv_file_path, index=False)
        
        # Check if the .csv file has data or not
        if os.path.getsize(csv_file_path) > 0:
            print("Conversion to CSV completed successfully.")
        else:
            print("The CSV file is empty.")
            sys.exit(2)
            
    except Exception as e:
        print("Error occurred while converting the file: ", str(e))
        sys.exit(1)
else:
    print("File does not exist.")
    sys.exit(1)
