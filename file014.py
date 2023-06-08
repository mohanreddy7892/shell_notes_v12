import os
import re
import pandas as pd

sh_dir = "/path/to/directory"
data = []

for root, dirs, files in os.walk(sh_dir):
    for file in files:
        if file.endswith(".sh"):
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                content = f.readlines()
                count_chmod = 0
                octal_numbers = []
                for line in content:
                    matches = re.findall(r'chmod (\d{3})', line)
                    if matches:
                        count_chmod += len(matches)
                        octal_numbers.extend(matches)
                if octal_numbers:
                    data.append([file_path, count_chmod, ','.join(octal_numbers)])

df = pd.DataFrame(data, columns=['File Name', 'Count of Chmod', 'Octal Numbers'])
df.to_excel('chmod_info.xlsx', index=False)