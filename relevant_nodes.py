import pandas as pd

cities = [
    "Zaanstad",
    "Amsterdam Centraal",
    "Haarlem",
    "Schiphol Airport",
    "Leiden Centraal",
    "Den Haag Centraal",
    "Zoetermeer",
    "Delft",
    "Rotterdam Centraal",
    "Spijkenisse",
    "Dordrecht",
    "Vlaardingen",
    "Alphen a/d Rijn",
    "Gouda",
    "Woerden",
    "Utrecht Centraal",
    "Hilversum",
    "Almere Centrum",
    "Amersfoort Centraal"
]

# Load the CSV file
df = pd.read_csv("nodes.csv")

# Filter rows where 'station' is in the cities list
filtered_df = df[df["station"].isin(cities)]

# Save to a new CSV file
filtered_df.to_csv("filtered_nodes.csv", index=False)

print("Filtered file saved as filtered_nodes.csv")