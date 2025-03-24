import pandas as pd
from sklearn.model_selection import train_test_split
import wget
import os

url = "https://assets-datascientest.s3.eu-west-1.amazonaws.com/MLOPS/bentoml/admission.csv"

filename = "../data/raw/admission.csv"

if os.path.exists(filename):
    os.remove(filename) # if exist, remove it directly
wget.download(url, out=filename)


df_admission = pd.read_csv(filename)
df_admission = df_admission.drop(columns=['Serial No.'])
df_admission.columns = df_admission.columns.str.strip()

X = df_admission.drop(columns=["Chance of Admit"])
y = df_admission['Chance of Admit']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

X_train.to_csv("../data/processed/X_train.csv", index=False)
X_test.to_csv("../data/processed/X_test.csv", index=False)
y_train.to_csv("../data/processed/y_train.csv", index=False)
y_test.to_csv("../data/processed/y_test.csv", index=False)