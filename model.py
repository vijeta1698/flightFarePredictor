import numpy as np
import pandas as pd
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


class flightModel():
    def model_creation(self):
        flight_data = pd.read_excel("Dataset/Data_Train.xlsx")
        flight_data.dropna(inplace=True)
        flight_data['Journey_day'] = pd.to_datetime(flight_data.Date_of_Journey,format = "%d/%m/%Y").dt.day
        flight_data['Journey_month'] = pd.to_datetime(flight_data.Date_of_Journey,format = "%d/%m/%Y").dt.month
        flight_data.drop(columns = ['Date_of_Journey'],axis = 1,inplace=True)
        flight_data['Dep_hour'] = pd.to_datetime(flight_data['Dep_Time']).dt.hour
        flight_data['Dep_min'] = pd.to_datetime(flight_data['Dep_Time']).dt.minute
        flight_data.drop(['Dep_Time'],axis=1,inplace=True)
        flight_data['Arrival_hour'] = pd.to_datetime(flight_data['Arrival_Time']).dt.hour
        flight_data['Arrival_min'] = pd.to_datetime(flight_data['Arrival_Time']).dt.minute
        flight_data.drop(columns = ['Arrival_Time'],axis=1,inplace=True)

        duration = list(flight_data['Duration'])

        for i in range(len(duration)):
            if len(duration[i].split()) != 2:    # Check if duration contains only hour or mins
                if "h" in duration[i]:
                    duration[i] = duration[i].strip() + " 0m"   # Adds 0 minute
                else:
                    duration[i] = "0h " + duration[i]           # Adds 0 hour
        duration_hours = []
        duration_mins = []
        for i in range(len(duration)):
            duration_hours.append(int(duration[i].split(sep = "h")[0]))    # Extract hours from duration
            duration_mins.append(int(duration[i].split(sep = "m")[0].split()[-1]))   # Extracts only minutes from duration

        flight_data['Duration_hours'] = duration_hours
        flight_data['Duration_mins'] = duration_mins

        source = flight_data[['Source']]
        source = pd.get_dummies(source,drop_first = True)
        source.head()

        destination = flight_data['Destination']
        destination = pd.get_dummies(destination,drop_first = True)
        Airline = flight_data[['Airline']]
        Airline = pd.get_dummies(Airline,drop_first=True)

        flight_data.drop(['Route','Additional_Info'],axis = 1, inplace=True)
        flight_data['Total_Stops'].replace({'non-stop':0,'1 stop' : 1,'2 stops':2,'3 stops':3,'4 stops':4},inplace=True)
        data_train  = pd.concat([flight_data,Airline,source,destination],axis=1)

        test_data = pd.read_excel('Dataset/Test_set.xlsx')
        test_data.dropna(inplace=True)
        test_data['Journey_day'] = pd.to_datetime(test_data.Date_of_Journey,format = '%d/%m/%Y').dt.day
        test_data['Journey_month'] = pd.to_datetime(test_data.Date_of_Journey,format = '%d/%m/%Y').dt.day

        test_data['Dep_hour'] = pd.to_datetime(test_data.Dep_Time).dt.hour
        test_data['Dep_min'] = pd.to_datetime(test_data.Dep_Time).dt.minute
        test_data['Arrival_min'] = pd.to_datetime(test_data.Arrival_Time).dt.minute
        test_data['Arrival_hour'] = pd.to_datetime(test_data.Arrival_Time).dt.hour
        duration = list(test_data["Duration"])

        for i in range(len(duration)):
            if len(duration[i].split()) != 2:
                if "h" in duration[i]:
                    duration[i] = duration[i].strip() + " 0m"
                else:
                    duration[i] = "0h " + duration[i]

        duration_hours = []
        duration_mins = []
        for i in range(len(duration)):
            duration_hours.append(int(duration[i].split(sep = "h")[0]))
            duration_mins.append(int(duration[i].split(sep = "m")[0].split()[-1]))
        test_data['Duration_hours'] = duration_hours
        test_data['Duration_mins'] =duration_mins

        Airline = pd.get_dummies(test_data['Airline'],drop_first=True)
        Source = pd.get_dummies(test_data['Source'],drop_first=True)
        Destination = pd.get_dummies(test_data['Destination'],drop_first=True)

        test_data['Total_Stops'].replace({"non-stop": 0, "1 stop": 1, "2 stops": 2, "3 stops": 3, "4 stops": 4}, inplace = True)
        test_data.drop(columns = ['Route','Additional_Info'],axis=1,inplace=True)
        test_data1 = pd.concat([test_data,Airline,Source,Destination],axis=1)

        test_data1.drop(columns = ['Airline','Source','Destination'],inplace=True)

        test_data1.drop(['Duration','Arrival_Time','Dep_Time'],axis=1,inplace=True)
        test_data1.rename({'Cochin':'Destination_Cochin', 'Delhi':'Destination_Delhi', 'Hyderabad':'Destination_Hyderabad', 'Kolkata':'Destination_Kolkata', 'New Delhi':'Destination_New Delhi'},axis=1,inplace=True)
        data_train.rename({'Cochin':'Destination_Cochin', 'Delhi':'Destination_Delhi', 'Hyderabad':'Destination_Hyderabad', 'Kolkata':'Destination_Kolkata', 'New Delhi':'Destination_New Delhi'},axis=1,inplace=True)

        X = data_train[['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour',
               'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
               'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
               'Airline_Jet Airways', 'Airline_Jet Airways Business',
               'Airline_Multiple carriers',
               'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
               'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
               'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
               'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
               'Destination_Kolkata', 'Destination_New Delhi']]
        y = data_train[['Price']]
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 42)
        self.reg_rf = RandomForestRegressor()
        self.reg_rf.fit(X_train,y_train)
        self.reg_rf.score(X_test,y_test)
        return self.reg_rf
