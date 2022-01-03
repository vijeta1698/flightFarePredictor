import pandas as pd
from log import getLog,StreamHandler

logger = getLog('flight_fare.py')
StreamHandler(logger)


class predictions():
    try:
        def departure_date_time(self,dep_date):
            self.dep_date = dep_date
            self.journey_day = int(pd.to_datetime(dep_date,format ="%Y-%m-%dT%H:%M").day)
            self.journey_month = int(pd.to_datetime(dep_date,format = "%Y-%m-%dT%H:%M").month)
            self.dep_hour = int(pd.to_datetime(dep_date,format = "%Y-%m-%dT%H:%M").hour)
            self.dep_minutes = int(pd.to_datetime(dep_date,format = "%Y-%m-%dT%H:%M").minute)
            return self.journey_day,self.journey_month , self.dep_hour,self.dep_minutes
    except Exception as e:
        logger.error('error in fetching departure date and time '+str(e))

    def arrival_time(self,time):
        try:
            self.time = time
            self.arrival_hour = int(pd.to_datetime(time, format ="%Y-%m-%dT%H:%M").hour)
            self.arrival_min =  int(pd.to_datetime(time, format ="%Y-%m-%dT%H:%M").minute)
            return self.arrival_hour,self.arrival_min
        except Exception as e:
            logger.info('error in fetching arrival time '+str(e))

    def duration(self):
        try:
            self.dur_hour = abs(self.arrival_hour-self.dep_hour)
            self.dur_min = abs(self.arrival_min-self.dep_minutes)
            return self.dur_hour,self.dur_min
        except Exception as e:
            logger.error('error in duration counting '+str(e))

    def total_stops(self,stops):
        try:
            self.stops = stops
            return stops
        except Exception as e:
            logger.error('error in total stops '+str(e))

    def Airline(self,airline):
        try:
            self.airline = airline
            if airline == 'Jet Airways':
                return 1,0,0,0,0,0,0,0,0,0,0
            elif airline=='IndiGO':
                return 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0
            elif airline == 'Air India':
                return 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0
            elif airline == 'Multiple carriers':
                return 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0
            elif airline == 'SpiceJet':
                return 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0
            elif airline == 'Vistara':
                return 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0
            elif airline == 'GoAir':
                return 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0
            elif airline == 'Multiple carriers Premium economy':
                return 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0
            elif airline == 'Jet Airways Business':
                return 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0
            elif airline == 'Vistara Premium economy':
                return 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0
            elif airline == 'Trujet':
                return 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
            elif airline == 'Air Asia':
                return 0,0,0,0,0,0,0,0,0,0,0
        except Exception as e:
            logger.error('error in airline options '+str(e))

    def Source(self,source):
        try:
            self.source = source
            if source=='Delhi':
                return 1,0,0,0
            elif source == 'Kolkata':
                return 0,1,0,0
            elif source == 'Mumbai':
                return 0,0,1,0
            elif source == 'Chennai':
                return 0,0,0,1
            elif source == 'Banglore':
                return 0,0,0,0
        except Exception as e:
            logger.error('error in source option '+str(e))

    def destination(self,dest):
        try:
            self.dest = dest
            if dest == 'Delhi':
                return 0,1,0,0,0
            elif dest == 'Kolkata':
                return 0,0,0,1,0
            elif dest == 'Hyderabad':
                return 0,0,1,0,0
            elif dest == 'New Delhi':
                return 0,0,0,0,1
            elif dest == 'Cochin':
                return 1,0,0,0,0
            elif dest == 'Banglore':
                return 0,0,0,0,0
        except Exception as e:
            logger.error('error in destination option '+str(e))



