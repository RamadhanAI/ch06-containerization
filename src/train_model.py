import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import mlflow
import mlflow.sklearn

def main():
    df = pd.read_csv("https://raw.githubusercontent.com/datablist/sample-csv-files/main/files/people/people-100.csv")
    df = df.dropna()
    X = df[["Age"]]
    y = (df["Gender"] == "Female").astype(int)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestClassifier(n_estimators=10)
    model.fit(X_train, y_train)

    mlflow.set_experiment("Chapter6-Containerization")
    with mlflow.start_run():
        mlflow.log_param("model_type", "RandomForest")
        mlflow.sklearn.log_model(model, "model")

    joblib.dump(model, "model.joblib")

if __name__ == "__main__":
    main()