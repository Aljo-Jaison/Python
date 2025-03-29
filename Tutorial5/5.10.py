import pandas as pd

# Creating sample student data
data = {
    "rollno": [101, 102, 103, 104, 105],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "place": ["New York", "Los Angeles", "Chicago", "Houston", "Miami"],
    "mark": [85, 92, 78, 88, 95]
}

df = pd.DataFrame(data)

df.to_csv("stud.csv", index=False)
print("✅ 'stud.csv' created successfully!")

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stud.csv")

# a) Read and display file contents
print("📄 File Contents:")
print(df)

# b) Set rollno as index
df.set_index("rollno", inplace=True)
print("\n🔢 Data with rollno as index:")
print(df)

# c) Display name and mark
print("\n Name & Mark:")
print(df[["name", "mark"]])

# d) Display rollno, Name, and Mark in order of Name
df_sorted_by_name = df.sort_values(by="name")
print("\nRollno, Name, Mark sorted by Name:")
print(df_sorted_by_name[["name", "mark"]])

# e) Display rollno, Name, Mark in descending order of Mark
df_sorted_by_mark = df.sort_values(by="mark", ascending=False)
print("\nRollno, Name, Mark sorted by Mark (Descending):")
print(df_sorted_by_mark[["name", "mark"]])

# f) Find average, median, and mode of marks
average_mark = df["mark"].mean()
median_mark = df["mark"].median()
mode_mark = df["mark"].mode()[0] 

print("\nStatistics:")
print(f"Average Mark: {average_mark}")
print(f"Median Mark: {median_mark}")
print(f"Mode Mark: {mode_mark}")

# g) Find minimum and maximum marks
min_mark = df["mark"].min()
max_mark = df["mark"].max()

print("\n Min & Max Marks:")
print(f"Minimum Mark: {min_mark}")
print(f"Maximum Mark: {max_mark}")

# h) Variance and Standard Deviation of Marks
variance_mark = df["mark"].var()
std_dev_mark = df["mark"].std()

print("\n Variance & Standard Deviation:")
print(f"Variance of Marks: {variance_mark}")
print(f"Standard Deviation of Marks: {std_dev_mark}")

# i) Display the histogram of marks
plt.hist(df["mark"], bins=5, color='skyblue', edgecolor='black')
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Histogram of Marks")
plt.show()

# j) Remove the place column
df.drop(columns=["place"], inplace=True)
print("\n Data after removing 'place' column:")
print(df)

