# dataCleaner

This Python script is a versatile tool for cleaning and formatting data from various file types. Currently, it supports CSV files, with plans to add support for more file types (e.g., Excel, JSON, etc.) and additional data cleaning functionalities in future updates.

## Features
- **Current Features:**
  - Recursively processes all CSV files in a directory and its subdirectories.
  - Formats dates from `mm/dd/yyyy` to `dd/mm/yyyy`.
  - Cleans corrupted or messy data (e.g., removes strange symbols, extra spaces, and newlines).
  - Adds a `_Formatted` postfix to processed files.
  - Skips files that have already been formatted.

- **Future Updates:**
  - Support for additional file types (Excel, JSON, etc.).
  - Advanced data cleaning functionalities (e.g., handling missing data, deduplication, etc.).
  - Customizable cleaning rules.

## Usage
1. Place the script in the root directory containing your files.
2. Run the script:
   ```bash
   python dataCleaner.py
