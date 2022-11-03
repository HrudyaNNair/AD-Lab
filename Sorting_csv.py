import pandas as pd
df=pd.read_csv('csvFile.csv')
print(df)
h=df.sort_values(["area"],ascending=[True])
print("\t\nSorted csv file\n",h)
