import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error
from joblib import load
import numpy as np

df = pd.read_csv("data/processed/housing_clean.csv")
X = df.drop('price', axis=1)
y = df['price']

model = load("models/trained_model.pkl")
preds = model.predict(X)

mae = mean_absolute_error(y, preds)
rmse = np.sqrt(mean_squared_error(y, preds))

with open("outputs/metrics.txt", "w") as f:
    f.write(f"MAE: {mae}\n")
    f.write(f"RMSE: {rmse}\n")
