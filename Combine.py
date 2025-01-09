import pandas as pd
import glob

# Get a list of all text files in the directory
txt_files = sorted(glob.glob("webpage_content_*.txt"))

# Initialize an empty list to hold dataframes
dfs = []

# Loop through the text files
for i, file in enumerate(txt_files):
    if i == 0:
        # Read the first file and keep the first line
        df = pd.read_csv(file, delimiter="\t", header=None)
    else:
        # Read the remaining files, skipping the first line
        df = pd.read_csv(file, delimiter="\t", header=None, skiprows=1)
    dfs.append(df)

# Concatenate all dataframes
combined_df = pd.concat(dfs, ignore_index=True)

# Write the combined dataframe to an Excel file
combined_df.to_excel("combined.xlsx", index=False, header=False)