import pandas as pd
import json


def csv_to_json():
    df = pd.read_csv("C:\\Users\\Uzytkownik\\Desktop\\CSIT2_LearningFromData\\Data\\movies.csv", sep=";")
    df.columns = ["order", "ID", "Title"]
    df = df.drop(["order"], axis=1)

    result = df.to_json(orient="records")
    parsed = json.loads(result)

    return parsed

