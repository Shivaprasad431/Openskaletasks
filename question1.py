def calculate_total_size(file_system, path):
    # Split the dot notation path into keys
    keys = path.split('.')
    
    # Start at the root of the file system
    current_directory = file_system
    
    # Traverse the nested dictionary
    for key in keys:
        if key in current_directory:
            current_directory = current_directory[key]  # Go deeper into the subdirectory
        else:
            return f"Directory '{path}' not found."  # Directory does not exist

    # At this point, we are at the specified directory
    total_size = 0
    
    # Check for files in the current directory
    if isinstance(current_directory, dict):
        for item in current_directory.values():
            if isinstance(item, dict) and 'size' in item:
                total_size += item['size']
    
    return f"Total size: {total_size}"

# Example file system structure
file_system = {
    "root": {
        "dir1": {
            "subdir1": {
                "file1": {"size": 500},
                "file2": {"size": 500},
            },
            "subdir2": {},
        },
        "dir2": {
            "subdir4": {
                "subsubdir5": {
                    "file3": {"size": 1200},
                    "file4": {"size": 2200},
                },
            },
        },
    }
}

# Main function to run the program
def main():
    # Get user input for the directory path
    path = input("Enter the directory path (in dot notation): ")
    
    # Calculate and display the total size
    result = calculate_total_size(file_system, path)
    print(result)

# Run the program
if __name__ == "__main__":
    main()
