import pandas as pd

# Load the CSV
df = pd.read_csv("raw_connections_roads.csv")

# Ensure there are no NaNs and drop the 'time' column if empty
df = df.drop(columns=['time'], errors='ignore').dropna()

# Make each connection unordered (so ALM-ASD and ASD-ALM are considered the same)
df['sorted_pair'] = df.apply(lambda x: tuple(sorted([x['from'], x['to']])), axis=1)

# Drop duplicates
df_unique = df.drop_duplicates('sorted_pair')

# Keep only the original columns
df_unique = df_unique[['from', 'to']]

# Sort alphabetically by 'from' then 'to'
df_unique = df_unique.sort_values(by=['from', 'to']).reset_index(drop=True)

# Save to a new CSV
df_unique.to_csv("network_edges_car.csv", index=False)

print("Deduplicated and sorted CSV saved as 'connections_unique.csv'.")