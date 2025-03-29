import pandas as pd

df = pd.read_csv("employee.csv")

print(" Employee Data Preview:")
print(df.head())

#1. print first 7 records from employees file
print(" First 7 Records:")
print(df.head(7))

#2. print all employee names in alphabetical order
print(" Employee Names in Alphabetical Order:")
print(df["name"].sort_values().tolist())

#3.find the name of the employee with highest salary
highest_paid_employee = df[df["salary"] == df["salary"].max()]["name"].values[0]
print(" Employee with the Highest Salary:", highest_paid_employee)

#4.list the names of male employees
male_employees = df[df["gender"] == "Male"]["name"].tolist()
print(" Male Employees:", male_employees)

#5. Display to which all teams employees belong
teams = df["team"].unique().tolist()
print(" Teams Employees Belong To:", teams)

