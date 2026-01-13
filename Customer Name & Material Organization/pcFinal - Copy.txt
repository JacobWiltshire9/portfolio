import pandas as pd

# load and read the excel file for the code
input_file = "Name List.xlsx"
df = pd.read_excel(input_file)

# sepereate the names and initials depending on the spaces
name_splits = df['Subject Name'].str.split(' ', expand=True)
name_splits.columns = [f"Name{i+1}" for i in range(name_splits.shape[1])]

# to add the material and method columns
processed_df = pd.concat([name_splits, df[['Material', 'Method']]], axis=1)

# sort whether the method is either shipped or in the store
processed_df_sorted = processed_df.sort_values(by='Method')

# save these files to excel and text file
processed_df_sorted.to_excel("pcFinal.xlsx", index=False)
processed_df_sorted.to_csv("pcFinal.txt", index=False, sep='\t')

# show the files are then saved
print("Files created: pcFinal.xlsx and pcFinal.txt")