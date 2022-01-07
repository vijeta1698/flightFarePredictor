import pandas as pd
from flask import Flask,render_template,request
from prediction import predictions
import joblib
import sklearn

from log import getLog,StreamHandler

app = Flask(__name__)

logger = getLog('flight_fare.py')
StreamHandler(logger)


@app.route('/',methods = ['GET','POST'])
def index():
    try:
        logger.info('site opened successfully')
        return render_template('home.html')
    except Exception as e:
        logger.error('error in opening site' +str(e))


@app.route('/predict',methods = ['GET','POST'])
def date():
    try:
        obj = predictions()
        if request.method == 'POST':
            try:
                Total_stops = request.form['stops']
                logger.info("total stops --->" +str(Total_stops))
                Departure_date = request.form['Dep_Time']
                logger.info("Departure --->" +str(Departure_date))
                Arrival_Date = request.form['Arrival_Time']
                logger.info("Arrival date --->" +str(Arrival_Date))
                Source = request.form['Source']
                logger.info("Source --->" +str(Source))
                Destination = request.form['Destination']
                logger.info("Destination --->" +str(Destination))
                airline = request.form['airline']
                logger.info("airline--->"+str(airline))
                departure_day = int(pd.to_datetime(Departure_date,format ="%Y-%m-%dT%H:%M").day)
                logger.info('departure_day---->'+str(departure_day))
                departure_month = int(pd.to_datetime(Departure_date,format ="%Y-%m-%dT%H:%M").month)
                logger.info('departure_month---->'+str(departure_month))
                arrival_day = int(pd.to_datetime(Arrival_Date, format="%Y-%m-%dT%H:%M").day)
                logger.info('arrival_day---->'+str(arrival_day))
                arrival_month = int(pd.to_datetime(Arrival_Date,format ="%Y-%m-%dT%H:%M").month)
                logger.info('arrival_month----->'+str(arrival_month))
                departure_year = int(pd.to_datetime(Departure_date, format="%Y-%m-%dT%H:%M").year)
                logger.info('departure_year----->'+str(departure_year))
                arrival_year = int(pd.to_datetime(Arrival_Date,format ="%Y-%m-%dT%H:%M").year)
                logger.info('arrival_year------>'+str(arrival_year))
                if (arrival_day< departure_day and arrival_month==departure_month) or (arrival_month<departure_month and departure_month!= 12
                                                                                       and arrival_year<departure_year) \
                        or (departure_month!=12 and arrival_year<departure_year):
                        error = "Please Check the Arrival Date and Try Again!!! "
                        logger.info('Re Check Arrival Date Error On Page')
                        return render_template('home.html',error = error)
                else:
                        logger.info('data inserted ---' + 'Total stops--> ' + Total_stops + ' Departure_date-->' +Departure_date
                                        + ' Arrival Date--->'+Arrival_Date + ' Source--->' +Source+' Destination-->' +Destination+
                                        ' Airline-->' +airline)
                        Journey_day = obj.departure_date_time(Departure_date)[0]
                        Journey_month = obj.departure_date_time(Departure_date)[1]
                        Dep_hour = obj.departure_date_time(Departure_date)[2]
                        Dep_min = obj.departure_date_time(Departure_date)[3]
                        Arrival_hour = obj.arrival_time(Arrival_Date)[0]
                        Arrival_min = obj.arrival_time(Arrival_Date)[1]
                        dur_hour = obj.duration()[0]
                        dur_min = obj.duration()[1]
                        airline = obj.Airline(airline)
                        source = obj.Source(Source)
                        dest = obj.destination(Destination)
                        logger.info('data from prediction fetched')

                        model = joblib.load(open("flight_model.pkl", 'rb'))
                        price = model.predict([[Total_stops,
                                                    Journey_day,
                                                    Journey_month,
                                                    Dep_hour,
                                                    Dep_min,
                                                    Arrival_hour,
                                                    Arrival_min,
                                                    dur_hour,
                                                    dur_min,
                                                    airline[0],
                                                    airline[1],
                                                    airline[2],
                                                    airline[3],
                                                    airline[4],
                                                    airline[5],
                                                    airline[6],
                                                    airline[7],
                                                    airline[8],
                                                    airline[9],
                                                    airline[10],
                                                    source[0], source[1], source[2], source[3],
                                                    dest[0], dest[1], dest[2], dest[3], dest[4]]])
                        logger.info('Predicted Price----> '+str(round(price[0],2)))
                        return render_template('home.html',price=round(price[0],2))
            except Exception as e:
                            logger.error('Error in data inserion ' + str(e))
    except Exception as e:
                logger.error('Error occurred' + str(e))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=False)

