import pandas as pd

df = pd.read_csv("C:\\Users\\Uzytkownik\\Desktop\\CSIT2_LearningFromData\\Data\\movies.csv", sep=";", error_bad_lines=False)

df.columns = ["", "ID", "Title"]
print(df.head())
