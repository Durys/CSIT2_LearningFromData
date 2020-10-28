import pandas as pd
import json


def csv_to_json():
    df = pd.read_csv("C:\\Users\\Uzytkownik\\Desktop\\CSIT2_LearningFromData\\Data\\movies.csv", sep=";")

    df.columns = ["order", "ID", "Title"]
    print(df.head())

    result = df.to_json()
    parsed = json.loads(result)
    print(json.dumps(parsed, indent=4))

