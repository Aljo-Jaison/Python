import pandas as pd

df = pd.read_csv("auto.csv")

# 1️ Clean and Update the CSV file (Remove Duplicates & Missing Values)
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df.to_csv("cleaned_auto.csv", index=False)
print(" Cleaned and updated CSV file saved as 'cleaned_auto.csv'.")

# 2️ Find the most expensive car company
most_expensive = df.loc[df["price"].idxmax(), "company"]
print(f"Most Expensive Car Company: {most_expensive}")

# 3️ Print all Toyota car details
toyota_cars = df[df["company"].str.lower() == "toyota"]
print("Toyota Cars Details:")
print(toyota_cars)

# 4️ Print total cars of all companies
car_counts = df["company"].value_counts()
print("Total Cars by Company:")
print(car_counts)

# 5️ Find the highest priced car of all companies
highest_priced_cars = df.loc[df.groupby("company")["price"].idxmax()]
print("Highest Priced Car from Each Company:")
print(highest_priced_cars[["company", "price"]])

# 6️ Find the average mileage of all companies
avg_mileage = df.groupby("company")["average-mileage"].mean()
print("Average Mileage by Company:")
print(avg_mileage)

# 7️ Sort all cars by the Price column
df_sorted = df.sort_values(by="price", ascending=False)
print("Cars Sorted by Price:")
print(df_sorted)
