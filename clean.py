import pandas as pd
df = pd.read_excel("disc_dataset.xlsx")
#df1=pd.read_csv("data1.csv")
df.dropna(inplace=True)
df.to_excel("disc_dataset.xlsx")
#df=pd.read_csv("test1.csv")
