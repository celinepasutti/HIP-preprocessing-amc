import os

def remove_first_line_in_folder(folder_path):
    # Iterate through all files in the specified folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                lines = file.readlines()
            
            # Remove the first line
            lines = lines[1:]
            
            with open(file_path, 'w') as file:
                file.writelines(lines)

# Specify the folder path
folder_path = "C://coding//HIP-preprocessing-amc//mocapPlayer"

remove_first_line_in_folder(folder_path)
