import pandas as pd
import re
from pathlib import Path
from collections import defaultdict

# List of XML file paths
xml_files = [
    Path('path/to/file1.xml'),
    Path('path/to/file2.xml'),
    # add more file paths as needed...
]

# Dictionary to store files for each condition
files_by_condition = defaultdict(list)

# Extract conditions from each file and store files by condition
for file_path in xml_files:
    with file_path.open('r') as file:
        xml_string = file.read()

    conditions = set(re.findall(r'<INCOND NAME="(.*?)"', xml_string)) \
                 | set(re.findall(r'<OUTCOND NAME="(.*?)"', xml_string)) \
                 | set(re.findall(r'<CONTROL NAME="(.*?)"', xml_string)) \
                 | set(re.findall(r'<DOCOND CONDITION="(.*?)"', xml_string))

    for condition in conditions:
        files_by_condition[condition].append(str(file_path))

# Convert files_by_condition to a list of dictionaries for DataFrame
data = [{'Condition': condition, 'Files': ', '.join(files)} for condition, files in files_by_condition.items()]

# Create DataFrame and write to Excel
df = pd.DataFrame(data)
df.to_excel('ConditionsWithFiles.xlsx', index=False)
