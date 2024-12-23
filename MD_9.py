import os
import time

# Function to recursively list all files in a directory and write to a file
def traverse_directory(path, level=0, file=None):
    if not os.path.exists(path):
        print(f"Directory not found: {path}")
        if file:
            file.write(f"Directory not found: {path}\n")
        return
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        line = "  " * level + item
        print(line)
        if file:
            file.write(line + "\n")
        if os.path.isdir(item_path):
            traverse_directory(item_path, level + 1, file)

# Function to get file stats and write to a file
def file_stats(file_path, file=None):
    try:
        stats = os.stat(file_path)
        file_info = {
            'size': stats.st_size,
            'Creation time': time.ctime(stats.st_ctime),
            'Last Modification time': time.ctime(stats.st_mtime),
            'File type': 'Directory' if os.path.isdir(file_path) else 'File'
        }
        for key, value in file_info.items():
            line = f"{key}: {value}"
            print(line)
            if file:
                file.write(line + "\n")
    except FileNotFoundError:
        error_message = f"File not found: {file_path}"
        print(error_message)
        if file:
            file.write(error_message + "\n")

# Example usage
if __name__ == "__main__":
    root_directory = r'C:\Users\janis\Documents\Jānis\ViA\2024_I_sem\Kiberdrošības politika_K.Felzenbergs'
    new_output_directory = r'C:\Users\janis\Documents\Jānis\Via\2024_I_sem\Pitons drošības testētājiem_K.Felzenbergs\pysec24'
    output_file_path = os.path.join(new_output_directory, "Cybersecurity_policy_info.txt")

    # Open the output file in write mode with utf-8 encoding
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        print("Directory Listing:")
        output_file.write("Directory Listing:\n")
        traverse_directory(root_directory, file=output_file)

    # Get stats for a given file after closing the file used for writing
    file_path = output_file_path
    print("\nFile Stats:")
    with open(file_path, 'a', encoding='utf-8') as output_file:
        output_file.write("\nFile Stats:\n")
        file_stats(file_path, file=output_file)


