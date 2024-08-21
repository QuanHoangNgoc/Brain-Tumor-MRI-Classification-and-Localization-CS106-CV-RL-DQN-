"""
git init
git status
git add . 
git commit -m "[-force]" 
git branch -M main 
git remote add origin https://github.com/QuanHoangNgoc/AI_Brain_Tumor.git 
git push --force origin main
"""

import subprocess 
import os


def list_files_under_50MB(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path) / (1024 * 1024)  # Convert size to MB
            if file_size < 50:
                print(f"{file_path} - {file_size:.2f} MB")
                path = file_path.replace(current_directory + "\\", "")
                file_list.append(path) 
    return file_list 


# List all files under 50MB in the root directory ("/")
current_directory = os.getcwd()
print(current_directory)

files = list_files_under_50MB(current_directory)
print(["git", "add"] + files) 


##############################################################################################
subprocess.run(["git", "add"] + files)

# Example: Commit changes with a message
commit_message = "auto add file"
subprocess.run(["git", "commit", "-m", commit_message])

# Example: Push changes to the remote repository
subprocess.run(["git", "push", "--force", "origin", "main"])

