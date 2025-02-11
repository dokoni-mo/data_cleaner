# Data Cleaner

This Python script is a versatile tool for cleaning and formatting data from various file types. Currently, it supports CSV files, with plans to add support for more file types (e.g., Excel, JSON, etc.) and additional data cleaning functionalities in future updates.

## Attribution
This project uses the following datasets:

1. **Car Sales Report**  
   - Licensed under the **Apache 2.0 License**.  
   - The original dataset can be found on [Kaggle](https://www.kaggle.com/datasets/missionjee/car-sales-report).  
   - Attribution: [Mission Jee](https://www.kaggle.com/missionjee).

2. **Supermarket Sales**  
   - Licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)** License.  
   - The original dataset can be found on [Kaggle](https://www.kaggle.com/datasets/yapwh1208/supermarket-sales-data).  
   - Attribution: [Yap Wei Hong](https://www.kaggle.com/yapwh1208).  

For more details about the licenses, please refer to:
- [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
- [CC BY-NC-SA 4.0 License](https://creativecommons.org/licenses/by-nc-sa/4.0/)

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
