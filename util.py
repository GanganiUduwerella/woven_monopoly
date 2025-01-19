import os
import glob

def selectFile(pattern):
    
    data_dir = "data"

    search_pattern = os.path.join(data_dir, pattern)
    matching_files = glob.glob(search_pattern)


    if not matching_files:
        raise FileNotFoundError(f"No files matching pattern '{pattern}' found in '{data_dir}'.")

    if len(matching_files) == 1:
        return matching_files[0]

    print("Multiple files found:")
    for idx, file in enumerate(matching_files):
        print(f"{idx + 1}: {os.path.basename(file)}")

    while True:
        try:
            choice = int(input("Select a file by entering its number: ")) - 1
            if 0 <= choice < len(matching_files):
                return matching_files[choice]
            else:
                print("Invalid selection. Please choose a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
