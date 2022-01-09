# flightFarePredictor
# Overview
This is a Flask web app which predicts fare of Flight ticket.<br>
Proper Logging has been used to log each and every step.<br>
Exception hanling is the important aspect which i took into consideration while building this application
# introduction 
Created a tool that estimates Flight Prices to help users look for best prices when booking flight tickets.
Engineered features from the Departure Time, Date of Journey, to quantify the data and make it more understandable.
Optimized multiple Regression models using GridsearchCV to reach the best model.
Built a client facing API using flask
# Codes and Resources Used
Python Version: 3.8.5
Packages: pandas, numpy, sklearn, matplotlib, seaborn, flask, json, pickle<br>
For Web Framework Requirements: pip install -r requirements.txt<br>
Dataset: https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh<br>
# Problem Statement
Flight ticket prices can be something hard to guess, today we might see a price, check out the price of the same flight tomorrow, it will be a different story. We might have often heard travelers saying that flight ticket prices are so unpredictable. As data scientists, we are gonna prove that given the right data anything can be predicted. Here you will be provided with prices of flight tickets for various airlines between the months of March and June of 2019 and between various cities. Size of training set: 10683 records

Size of test set: 2671 records<br>
FEATURES: Airline: The name of the airline.<br>
Date_of_Journey: The date of the journey<br>
Source: The source from which the service begins.<br>
Destination: The destination where the service ends.<br>
Route: The route taken by the flight to reach the destination.<br>
Dep_Time: The time when the journey starts from the source.<br>
Arrival_Time: Time of arrival at the destination.<br>
Duration: Total duration of the flight.<br>
Total_Stops: Total stops between the source and destination.<br>
Additional_Info: Additional information about the flight<br>
Price: The price of the ticket<br>
# Productionization
In this step, I built a flask API endpoint that was hosted on a heroku via CircleCi. The API endpoint takes in a request with a list of values from a flight and returns an estimated price.
# OPS pipeline
i have used Circleci for cicd pipeline.
the <b>".circleci" </b> folder has <b>config.yml</b> file for implementing it.
