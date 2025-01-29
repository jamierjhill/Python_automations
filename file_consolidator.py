import os
import pandas as pd
from openpyxl import load_workbook

def consolidate_excel_files(source_folder, output_file, sheet_name):
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        # Loop through each file in the source folder
        for file in os.listdir(source_folder):
            if file.endswith(".xlsx") and not file.startswith("~"):  # Ignore temporary files
                file_path = os.path.join(source_folder, file)
                
                try:
                    # Read the specific sheet as a DataFrame
                    df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
                    sheet_title = os.path.splitext(file)[0]  # Use file name as sheet name
                    df.to_excel(writer, sheet_name=sheet_title, index=False)
                except Exception as e:
                    print(f"Error reading {file}: {e}")
    
    print(f"Consolidation complete! Saved to {output_file}")

# Example usage
source_folder = "C:/Users/JamieHill/OneDrive - UNYBRANDS Operations Ltd/Documents/Python Code Test"  # Update with actual path
output_file = "C:/Users/JamieHill/OneDrive - UNYBRANDS Operations Ltd/Documents/Python Code Test/consolidated.xlsx"  # Update with desired output file
sheet_name = "Model Tab"  # Update with the specific sheet name

consolidate_excel_files(source_folder, output_file, sheet_name)