import pandas as pd
import os
import glob

# Specify the input and output directories
input_dir = '/Users/markedino/Documents/RCoW_Sample/saved1x1'  # Directory containing the .xlsx files
output_dir = '/Users/markedino/Documents/RCoW_Sample/converted_to_txt'  # Directory to save the .txt files

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Get all .xlsx files in the input directory
xlsx_files = glob.glob(os.path.join(input_dir, '*.xlsx'))

# Iterate through each .xlsx file
for file_path in xlsx_files:
    # Load the Excel file
    df = pd.read_excel(file_path)

    # Extract the first column
    first_column = df.iloc[:, 0]

    # Get the base name of the file (without extension) for naming output files
    base_name = os.path.splitext(os.path.basename(file_path))[0]

    # Iterate through each column (starting from the second column) and save it along with the first column
    for column in df.columns[1:]:
        # Create a new DataFrame with the first column and the current column
        column_df = pd.concat([first_column, df[[column]]], axis=1)

        # Define the output file name and path
        output_file = os.path.join(output_dir, f'{base_name}_{column}.txt')

        # Save the DataFrame to a new text file
        column_df.to_csv(output_file, sep='\t', index=False)

print("Columns have been saved as separate text files successfully.")
