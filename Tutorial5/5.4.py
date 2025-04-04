import pandas as pd

data = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
label = ['A', 'B', 'C']

df = pd.DataFrame(data, index=label, columns=[f'Col{i+1}' for i in range(len(data[0]))])
df.to_excel("C:\\Users\\aljoj\\Desktop\\Python\\Tutorial5\\output3.xlsx", index=True)
print("Data written to o/p.xlsx")

