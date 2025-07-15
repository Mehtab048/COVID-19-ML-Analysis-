import os
import pandas as pd

# Path to your dataset folder
data_folder = "D:\Machine Learning\Assignments\MLAssignment02\Dataset"

# List all CSV files in the folder
files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]

# Create an empty list to store the DataFrames
dataframes = []

# Loop through each file and load it into a DataFrame
for file in files:
    file_path = os.path.join(data_folder, file)
    df = pd.read_csv(file_path)  # Load the CSV into a DataFrame
    dataframes.append(df)  # Append to the list of DataFrames

# Concatenate all DataFrames into a single DataFrame
final_data = pd.concat(dataframes, ignore_index=True)

# Print the first few rows of the combined dataset
print(final_data.head())

#python3 ML_Assignment.py
