import os
import random
import shutil
import re

# Define the source directory
src_dir = './my_dataset/train/sad'
dst_dir = './my_dataset/val/sad'
key = 'sad'
percentage_val = 0.2

def remove_invalid_files(directory, file_path=None):
    valid_extensions = ['.jpg', '.jpeg', '.png']
    if file_path is None:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in valid_extensions:
                os.remove(file_path)
                print(f"Removed file: {file_path}")
    else:
        file_extension = os.path.splitext(file_path)[1].lower()
        if file_extension not in valid_extensions:
            os.remove(file_path)
            print(f"Removed file: {file_path}")

def rename_files(src_dir, key):
    # Loop over all the files in the source directory
    index = 1
    for filename in os.listdir(src_dir):
        # Construct the full path to the file
        file_path = os.path.join(src_dir, filename)
        # Extract the extension from the original file name
        match = re.search(r'(\.\w+)$', filename)
        if match:
            extension = match.group(1)
            # Construct the new file name
            new_filename = f"{key}_{index}{extension}"
            
            # Construct the full path to the new file
            new_file_path = os.path.join(src_dir, new_filename)
            
            # Rename the file
            os.rename(file_path, new_file_path)
            index = index + 1
            print(f"Renamed file: {file_path} -> {new_file_path}")

remove_invalid_files(src_dir)

rename_files(src_dir, key)


# Get a list of all the files in the source directory
files = os.listdir(src_dir)

# Get a random sample of files
random_files = random.sample(files, int(len(files) * percentage_val))

# Move the files
for file_name in random_files:
    # Construct the full path to the file
    src_file = os.path.join(src_dir, file_name)
    
    # Construct the full path to the destination file
    dst_file = os.path.join(dst_dir, file_name)
    
    # Move the file
    shutil.move(src_file, dst_file)