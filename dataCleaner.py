import os
import pandas as pd
from datetime import datetime
import re

# Function to convert date format
def convert_date_format(date_str):
    try:
        # Ensure the input is a string
        if isinstance(date_str, str):
            # Parse the date in the original format (mm/dd/yyyy)
            date_obj = datetime.strptime(date_str, '%m/%d/%Y')
            # Convert to the new format (dd/mm/yyyy)
            return date_obj.strftime('%d/%m/%Y')
        else:
            # Return the original value if it's not a string (e.g., float, NaN)
            return date_str
    except ValueError:
        # Return the original string if it's not a valid date
        return date_str

# Function to clean a column (remove strange symbols, newlines, and extra spaces)
def clean_column(column_value):
    if isinstance(column_value, str):
        # Replace all non-ASCII or strange symbols with a single space
        column_value = re.sub(r'[^\x00-\x7F]+', ' ', column_value)  # Replace non-ASCII characters with a space
        column_value = column_value.replace('\n', ' ').replace('\t', ' ')  # Replace newlines and tabs with spaces
        column_value = ' '.join(column_value.split())  # Remove extra spaces
        return column_value
    else:
        # Return the original value if it's not a string
        return column_value

# Function to process a single CSV file
def process_csv_file(file_path):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path, encoding='utf-8')  # Try UTF-8 first
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='latin-1')  # Fallback to Latin-1 if UTF-8 fails

    # Apply the date format conversion to all columns that might contain dates
    for col in df.columns:
        df[col] = df[col].apply(convert_date_format)

    # Clean all columns in the DataFrame
    for col in df.columns:
        df[col] = df[col].apply(clean_column)

    # Save the updated DataFrame to a new CSV file with "_Formatted" postfix
    dir_name, file_name = os.path.split(file_path)
    file_base, file_ext = os.path.splitext(file_name)
    new_file_name = f"{file_base}_Formatted{file_ext}"
    new_file_path = os.path.join(dir_name, new_file_name)
    df.to_csv(new_file_path, index=False, encoding='utf-8')

    print(f"Processed and saved: {new_file_path}")

# Function to process all CSV files in a directory and its subdirectories
def process_all_csv_files(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            # Skip files that already contain "_Formatted" in their names
            if filename.endswith('.csv') and '_Formatted' not in filename:
                file_path = os.path.join(dirpath, filename)
                process_csv_file(file_path)

# Main script
if __name__ == "__main__":
    # Set the root directory (current directory in this case)
    root_directory = os.getcwd()

    # Process all CSV files in the root directory and its subdirectories
    process_all_csv_files(root_directory)

    print("All CSV files processed successfully!")