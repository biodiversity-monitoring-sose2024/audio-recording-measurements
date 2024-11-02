import argparse
import re

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Process log file and extract sending times.")
parser.add_argument('-f', '--file', required=True, help="Path to the log file")
args = parser.parse_args()

# Read log data from the specified file
with open(args.file, 'r') as file:
    log_data = file.read()

# List of filenames
filenames = [
    "17273626.wav", "17273627.wav", "17273628.wav", "17273629.wav", "17273630.wav",
    "17273631.wav", "17273632.wav", "17273633.wav", "17273634.wav", "17273635.wav",
    "17273636.wav", "17273637.wav", "17273638.wav", "17273639.wav", "17273640.wav",
    "17273641.wav", "17273642.wav", "17273643.wav", "17273644.wav", "17273645.wav",
    "17273646.wav", "17273647.wav", "17273648.wav", "17273649.wav", "17273650.wav",
    "17273651.wav", "17273652.wav", "17273653.wav", "17273654.wav", "17273655.wav",
    "17273656.wav", "17273657.wav", "17273658.wav", "17273659.wav", "17273660.wav",
    "17273661.wav", "17273662.wav", "17273663.wav", "17273664.wav", "17273665.wav",
    "17273666.wav", "17273667.wav", "17273668.wav", "17273669.wav"
]

# Extract every second "Sending took" time value
time_values = [float(time) for time in re.findall(r"Sending took: ([0-9.]+) seconds", log_data)]
second_times_milliseconds = [time_values[i] * 1000 for i in range(1, len(time_values), 2)]
filtered_times_milliseconds = [time * 1000 for time in time_values if time * 1000 > 20]
# Map the extracted times to filenames
filename_time_pairs = list(zip(filenames, filtered_times_milliseconds))

# Print the result as a markdown table
print("| Filename     | Time (ms)      |")
print("|--------------|----------------|")

for filename, time in filename_time_pairs:
    print(f"| {filename} | {time:.2f}  |")
