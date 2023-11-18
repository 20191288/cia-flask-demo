import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from config.app_config import FLASK_APP_PATH

class RegressionModel:
    def __init__(self):
        self.model = self.create_pipeline()

    def prepare_data(self):
        data = pd.read_csv(os.path.join(FLASK_APP_PATH, 'app_regression/titanic.csv'))
        features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'Survived']

        data = data[features].dropna()

        X = data.drop('Survived', axis=1)
        y = data['Survived']

        X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

        return X_train, y_train

    def create_pipeline(self):
        numeric_features = ['Age', 'SibSp', 'Parch', 'Fare']
        categorical_features = ['Sex', 'Embarked']

        numeric_transformer = Pipeline(steps=[
            ('scaler', StandardScaler())
        ])

        categorical_transformer = Pipeline(steps=[
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ])

        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numeric_features),
                ('cat', categorical_transformer, categorical_features)
            ])

        model = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('classifier', LogisticRegression(max_iter=1000))
        ])

        return model

    def train(self):
        X_train, y_train = self.prepare_data()
        self.model.fit(X_train, y_train)

    def predict(self, passenger_data):
        data = pd.DataFrame(passenger_data, index=[0])
        prediction = self.model.predict(data)
        return prediction

def get_data():
    return(pd.read_csv(os.path.join(FLASK_APP_PATH, 'app_regression/titanic.csv')))