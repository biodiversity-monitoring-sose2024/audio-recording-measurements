import sys
import os
import re

def parse_data(log_data):
    # Regex patterns to match the time and filename
    time_pattern = re.compile(r'Finished sending data in (\d+) ms')
    filename_pattern = re.compile(r'Deleting /sdcard/queue/([\w\d]+\.wav)')

    # Lists to store times and filenames
    times = []
    filenames = []

    # Find all matches
    times = time_pattern.findall(log_data)
    filenames = filename_pattern.findall(log_data)

    # Generate markdown table
    markdown_table = "| File          | Time [ms]     |\n"
    markdown_table += "| ------------- | ------------- |\n"
    for filename, time in zip(filenames, times):
        markdown_table += f"| {filename}  | {time}         |\n"

    return markdown_table

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {os.path.basename(__file__)} <log_file_path>")
        sys.exit(1)

    log_file_path = sys.argv[1]

    log_data = ""
    try:
        with open(log_file_path, 'r') as file:
            log_data = file.read()
    except FileNotFoundError:
        print(f"The file {log_file_path} does not exist.")
        sys.exit(1)

    result = parse_data(log_data)

    print(result)

if __name__ == "__main__":
    main()