import pandas as pd
import os

# Load the Excel file
file_path = '/Users/markedino/Documents/RCoW_Sample/T1 - Summary - Incorrect Closures.xlsx'
output_dir = '/Users/markedino/Documents/RCoW_Sample/saved1x1'  # Specify your output directory

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

df = pd.read_excel(file_path)

# Extract the first column
first_column = df.iloc[:, 0]

# Iterate through each column (starting from the second column) and save it along with the first column
for column in df.columns[1:]:
    # Create a new DataFrame with the first column and the current column
    column_df = pd.concat([first_column, df[[column]]], axis=1)

    # Define the output file name and path
    output_file = os.path.join(output_dir, f'{column}.xlsx')

    # Save the DataFrame to a new Excel file
    column_df.to_excel(output_file, index=False)

print("Columns have been saved as separate files successfully.")