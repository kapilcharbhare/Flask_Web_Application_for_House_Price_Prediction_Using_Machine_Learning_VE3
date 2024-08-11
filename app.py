from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load and preprocess data
data = pd.read_csv('housing.csv')
data.fillna(data.mean(), inplace=True)
data = pd.get_dummies(data, columns=['ocean_proximity'])

# Select features and target
X = data[['median_income', 'total_rooms', 'housing_median_age', 'ocean_proximity_INLAND']]
y = data['median_house_value']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    
    # Make prediction
    prediction = model.predict(final_features)

    return render_template('index.html', prediction_text=f'Predicted House Price: ${prediction[0]:,.2f}')

if __name__ == "__main__":
    app.run(debug=True)
