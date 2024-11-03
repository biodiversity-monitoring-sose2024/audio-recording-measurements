import argparse
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
import re
import numpy as np

def parse_markdown_tables(filepath):
    with open(filepath, 'r') as file:
        content = file.read()

    # Regex pattern to match markdown tables
    table_pattern = re.compile(
        r'((?:\|.+?\|\n)+\|.+?\|)\n(?!\s*([-|]+)\s*\n)')

    matches = table_pattern.findall(content)
    dataframes = []

    for match in matches:
        table = match[0]
        try:
            df = pd.read_csv(StringIO(table), sep='|', engine='python', skipinitialspace=True)
            df = df.dropna(axis=1, how='all')
            df.columns = [col.strip() for col in df.columns]
            df = df.apply(lambda col: col.str.strip() if col.dtype == 'object' else col)
            dataframes.append(df)
        except Exception as e:
            print(f"Could not parse table: {e}")

    return dataframes

def plot_data(y_column, df_list, output_file, title, x_label):
    plt.figure(figsize=(12, 6))
    
    temporal_values = []

    max_length = max(len(df[y_column]) for df in df_list)  # Find max length for alignment

    for i, df in enumerate(df_list):
        df[y_column] = pd.to_numeric(df[y_column], errors='coerce')
        temporal_values.append(df[y_column].reindex(range(max_length), fill_value=np.nan).values)
        plt.plot(df.index, df[y_column], alpha=0.3, label=f'Set {i + 1}')

    # Calculating temporal average (average per index)
    temporal_values = np.array(temporal_values)
    temporal_average = np.nanmean(temporal_values, axis=0)
    plt.plot(range(max_length), temporal_average, color='b', linestyle='-', linewidth=2, label='Temporal Average')

    # Calculating overall average across all values
    overall_average = np.nanmean(temporal_average)
    plt.axhline(y=overall_average, color='r', linestyle='--', linewidth=2, label=f'Overall Average = {overall_average:.2f}')

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_column)
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    # Save the plot to a file
    plt.savefig(output_file, transparent=True)
    plt.close()  # Close the plot to free up memory

def main():
    parser = argparse.ArgumentParser(description='Plot columns from markdown table data')
    parser.add_argument('filepaths', type=str, nargs='+', help='Paths to the markdown files containing tables')
    parser.add_argument('--y-column', type=str, required=True, help='Name of the column to plot as Y axis')
    parser.add_argument('--table-index', type=int, default=0, help='Index of the table to plot (0-based)')
    parser.add_argument('--output-file', type=str, required=True, help='Output file to save the plot')
    parser.add_argument('--title', type=str, required=True, help='The title for the plot')
    parser.add_argument('--x-label', type=str, required=True, help='The label for the X axis')

    args = parser.parse_args()

    dataframes = []

    # Process each filepath
    for filepath in args.filepaths:
        dfs = parse_markdown_tables(filepath)
        if not dfs:
            print(f"No tables found in the file: {filepath}")
            continue
        if args.table_index < 0 or args.table_index >= len(dfs):
            print(f"Error: Table index {args.table_index} out of range for file: {filepath}.")
            continue
        
        df = dfs[args.table_index]
        if args.y_column not in df.columns:
            print(f"Error: Column {args.y_column} not found in the file: {filepath}.")
            continue
        
        dataframes.append(df)

    if dataframes:
        plot_data(args.y_column, dataframes, args.output_file, args.title, args.x_label)
        print(f"Plot saved to {args.output_file}")
    else:
        print("No valid data found for plotting.")

if __name__ == '__main__':
    main()