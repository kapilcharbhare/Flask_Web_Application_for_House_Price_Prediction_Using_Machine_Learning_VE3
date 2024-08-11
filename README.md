# Flask_Web_Application_for_House_Price_Prediction_Using_Machine_Learning_VE3

#House Price Prediction Web Application

#This project is a Flask-based web application that predicts house prices based on user input features using a machine learning model. The application uses a linear regression model trained on the California Housing Prices dataset.

#Table of Contents
#Project Overview
#Dataset
#Model
#Installation
#Usage
#Snapshots

# This project demonstrates a simple machine learning application where users can input features related to a house (such as median income, total rooms, etc.), and the app predicts the house's price. The Flask web application is easy to set up and serves as a basic introduction to deploying machine learning models in a web environment.

#Dataset
The dataset used in this project is the California Housing Prices dataset from Kaggle. It includes various features of houses in California and the corresponding median house values.

#Key Features Used:

#median_income: Median income of households in the block.
#total_rooms: Total number of rooms in the block.
#housing_median_age: Median age of the houses in the block.
#ocean_proximity_INLAND: Whether the house is located inland (1 for yes, 0 for no).

#Model
A simple linear regression model is used for predicting house prices based on the features mentioned above. The model is trained using the scikit-learn library.

#Installation
#Prerequisites
#Python 3.8 or higher
#Virtual environment (optional but recommended)
#Steps
#Create a virtual environment (optional but recommended):

#bash
#python3 -m venv venv
#source venv/bin/activate  # On Windows: venv\Scripts\activate
#Install the required packages:

#bash
#pip install -r requirements.txt
#Download the dataset: Download the California Housing Prices dataset and place it in the project directory as housing.csv.

#Run the Flask app:

#bash
#python app.py
#The application will be available at http://127.0.0.1:5000/.

#Usage
#Access the Application: Open your browser and navigate to http://127.0.0.1:5000/.

#Enter House Features: Fill out the form with relevant house features such as median income, total rooms, housing median age, and inland location status.

#Predict House Price: Submit the form to get the predicted house price.

#Snapshots
Include snapshots of the form and the prediction result here.
