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
filesystem = {
    "root": {
        "dir1": {
            "subdir1": {
                "file1.txt": 100,
                "file2.txt": 200,
                "subsubdir1": {
                    "file3.txt": 50,
                    "file4.txt": 150,
                    "subsubsubdir1": {
                        "file5.txt": 500,
                        "emptydir1": {}
                    }
                }
            },
            "subdir2": {
                "file6.txt": 300,
                "subsubdir2": {
                    "file7.txt": 700,
                    "subsubsubdir2": {
                        "file8.txt": 800,
                        "file9.txt": 900
                    }
                },
                "emptydir2": {}
            },
            "file10.txt": 1000
        },
        "dir2": {
            "subdir3": {
                "subsubdir3": {
                    "file11.txt": 400,
                    "file12.txt": 500
                },
                "subsubdir4": {
                    "emptydir3": {}
                }
            },
            "subdir4": {
                "file13.txt": 600,
                "subsubdir5": {
                    "file14.txt": 700,
                    "file15.txt": 800,
                    "subsubsubdir3": {
                        "emptydir4": {},
                        "file16.txt": 900,
                        "file17.txt": 1000
                    }
                }
            },
            "emptydir5": {}
        },
        "dir3": {
            "file18.txt": 1100,
            "subdir5": {
                "subsubdir6": {
                    "file19.txt": 1200,
                    "subsubsubdir4": {
                        "file20.txt": 1300,
                        "emptydir6": {}
                    }
                }
            }
        },
        "emptydir7": {},
        "file21.txt": 1400
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
