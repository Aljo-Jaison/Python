import pandas as pd

data = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

index = ['A', 'B', 'C']

column = ['Col1', 'Col2', 'Col3']

df = pd.DataFrame(data, index=index, columns=column)

print("DataFrame:")
print(df)
