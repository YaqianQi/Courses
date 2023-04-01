import pandas as pd
from constant import full_dataset, sample_dataset

sample_num = 10000

# Load the CSV file into a pandas dataframe
df = pd.read_csv(full_dataset)

# Randomly select 1000 rows
sample_df = df.sample(n=sample_num, random_state=42)

# Save the selected rows to a new CSV file
sample_df.to_csv(sample_dataset, index=False)