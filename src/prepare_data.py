import pandas as pd
from sklearn.model_selection import train_test_split

df_admission = pd.read_csv("/home/ubuntu/examen_bentoml/data/raw/admission.csv")
df_admission = df_admission.drop(columns=['Serial No.'])
df_admission.columns = df_admission.columns.str.strip()

X = df_admission.drop(columns=["Chance of Admit"])
y = df_admission['Chance of Admit']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

X_train.to_csv("../data/processed/X_train.csv", index=False)
X_test.to_csv("../data/processed/X_test.csv", index=False)
y_train.to_csv("../data/processed/y_train.csv", index=False)
y_test.to_csv("../data/processed/y_test.csv", index=False)