from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import pandas as pd
import bentoml



df_X_train = pd.read_csv("../data/processed/X_train.csv")
df_y_train = pd.read_csv("../data/processed/y_train.csv")
df_X_test = pd.read_csv("../data/processed/X_test.csv")
df_y_test = pd.read_csv("../data/processed/y_test.csv")

parameters = {'kernel':('linear', 'rbf', 'poly'), 'C':[0.1, 1, 10]}
svr = svm.SVR()
reg = GridSearchCV(svr, parameters)
reg.fit(df_X_train, df_y_train.values.ravel())
r2 = reg.score(df_X_test, df_y_test)

print("Performance ----> R2 Score on test data: ", r2)
print("Best parameters of the model: ", reg.best_params_)

model_ref = bentoml.sklearn.save_model("examen_bentoml_model", reg)

print(model_ref)