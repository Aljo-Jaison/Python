import pandas as pd

data = [
    [1, "Linus Torvalds", "Finland", "Linux Kernel", 1991],
    [2, "Tim Berners-Lee", "England", "World Wide Web", 1990],
    [3, "Guido van Rossum", "Netherlands", "Python", 1991]
]

columns = ["SN", "Name", "Country", "Contribution", "Year"]

df = pd.DataFrame(data, columns=columns)

df.to_csv("university_data.csv", index=False)

print("Data written to university_data.csv successfully!")


"""
import csv

data = [
    ["SN", "Name", "Country", "Contribution", "Year"],
    [1, "Linus Torvalds", "Finland", "Linux Kernel", 1991],
    [2, "Tim Berners-Lee", "England", "World Wide Web", 1990],
    [3, "Guido van Rossum", "Netherlands", "Python", 1991]
]

with open("university_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data written to university_data.csv successfully!")
"""