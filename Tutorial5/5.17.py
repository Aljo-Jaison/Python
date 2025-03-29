import pandas as pd

# Read the CSV file
df = pd.read_csv("student.csv")

#  1) Find the average CGPA of all students
average_cgpa = df["CGPA"].mean()
print(" Average CGPA of Students:", round(average_cgpa, 2))

#  2) Display details of students with CGPA > 9
high_cgpa_students = df[df["CGPA"] > 9]
print("\n Students with CGPA > 9:\n", high_cgpa_students)

#  3) Display details of CSE students with CGPA > 9
cse_high_cgpa = df[(df["Branch"] == "CSE") & (df["CGPA"] > 9)]
print("\n CSE Students with CGPA > 9:\n", cse_high_cgpa)

#  4) Display details of the student with the maximum CGPA
max_cgpa_student = df[df["CGPA"] == df["CGPA"].max()]
print("\n Student with Maximum CGPA:\n", max_cgpa_student)

#  5) Display average CGPA of each branch
branch_avg_cgpa = df.groupby("Branch")["CGPA"].mean()
print("\n Average CGPA of Each Branch:\n", branch_avg_cgpa)
