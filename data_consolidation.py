import os
import pandas as pd

def merge_csv_files(folder_path, output_file='merged_data.csv'):
    """
    Merge all CSV files in the specified folder into a single CSV file.

    Parameters:
    - folder_path (str): Path to the folder containing CSV files.
    - output_file (str): Name of the output CSV file. Default is 'merged_data.csv'.
    """
    # List to store dataframes from CSV files
    dfs = []

    # Iterate through files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            # Read CSV file and append dataframe to the list
            df = pd.read_csv(os.path.join(folder_path, filename))
            dfs.append(df)

    # Concatenate dataframes
    merged_df = pd.concat(dfs, ignore_index=True)

    # Write merged dataframe to a new CSV file
    merged_df.to_csv(output_file, index=False)

# Example usage
folder_path = 'D:\Eshipz\AI_LOAD_DATA\CODE\data_aug_2023'
merge_csv_files(folder_path)

