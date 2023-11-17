from flask_sqlalchemy import SQLAlchemy
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from .views import get_all_data 

class RegressionModel:
    def __init__(self):
        self.model = LogisticRegression()

    def train(self):
        data = get_all_data()



    def predict(self, passenger_data):
        # 'passenger_data' should be a dictionary with keys: 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare'
        data = pd.DataFrame(passenger_data, index=[0])
        prediction = self.model.predict(data)
        return prediction[0]