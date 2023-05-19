# read all the files in the directory and format them

import os

def read_files_in_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith('.py') and file_name[-5]=='L':
                original_file_path = os.path.join(root, file_name)            
                # Modify the file name as desired
                base_name, ext = os.path.splitext(file_name)
                new_file_path = base_name[-2:]+'_'+base_name[:-3]+ext
                modified_file_path = os.path.join(root, new_file_path)
                print(original_file_path, modified_file_path)
                os.rename(original_file_path, modified_file_path)

# Example usage
directory_path = '/Users/zzy/Code/CompetitiveProgramming/Leetcode'
read_files_in_directory(directory_path)