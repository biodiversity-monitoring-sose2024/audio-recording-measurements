import argparse
import re

def parse_file(file_path, unit):
    data = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            image_name = lines[i].strip()[1:-1]   # Get the image name
            value = lines[i + 1].strip()    # Get the respective value
            if unit in value:
                # Remove the unit from the value and convert to float
                data[image_name] = float(value.replace(unit, ''))
    return data

def generate_markdown_table(voltages, currents):
    header = "| Image | Voltage [V] | Current [A] | Wattage [W] |\n"
    separator = "|-------|-------------|-------------|-------------|\n"
    rows = []
    for image in voltages:
        voltage = voltages[image]
        current = currents.get(image, 0)
        wattage = voltage * current
        row = f"| {image} | {voltage:.3f} | {current:.4f} | {wattage:.4f} |\n"
        rows.append(row)
    return header + separator + "".join(rows)

def main(voltage_file, amperage_file):
    # Parse the files
    voltages = parse_file(voltage_file, 'V')
    currents = parse_file(amperage_file, 'A')

    # Create the markdown table
    markdown_table = generate_markdown_table(voltages, currents)

    # Print the markdown table
    print(markdown_table)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse voltage and amperage files to compute wattage.")
    parser.add_argument("-v", "--voltage", required=True, help="Path to the voltage file")
    parser.add_argument("-a", "--amperage", required=True, help="Path to the amperage file")
    args = parser.parse_args()

    main(args.voltage, args.amperage)