# some code
import requests
import shutil
import os
import subprocess
import stat

#url = 'https://api.github.com/repos/mohanreddy7892/mohanreddy7892'
def remove_readonly(func, path, _):
    """Remove the read-only attribute of a file or directory."""
    os.chmod(path, stat.S_IWRITE)
    func(path)


# Replace with your own access token and repository information
access_token = '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'
owner = 'mohanreddy7892'
repo = 'mohanreddy7892'
# repo = 'https://github.com/mohanreddy7892/mohanreddy7892'
branch = 'Mohan'
url = f'https://api.github.com/repos/{owner}/{repo}'
print(url)
headers = {'Authorization': f'token {access_token}'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Successfully authenticated with Git!")
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.json())

destination_dir = rf'C:\Users\mohan\OneDrive\Desktop\Test_Git'
# Remove the existing directory if it exists
if os.path.exists(destination_dir):
    shutil.rmtree(destination_dir, onerror=remove_readonly)

# Create the new directory
os.makedirs(destination_dir)

remote_url = f'https://{access_token}@github.com/{owner}/{repo}.git'
# Clone the specific branch
try:
    subprocess.run(['git', 'clone', '--branch', branch, remote_url, destination_dir], check=True)
    print(f"Successfully cloned branch '{branch}' from repository '{owner}/{repo}'.")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
