import pandas as pd
import numpy as np
import time
import sys

def get_flight_time(string):
    hour = 100
    if len(string)==1 or len(string)==2:
        hour = 0
        if int(string)>30:
            hour += 1
    elif len(string)==3:
        hour = int(string[0])
        if int(string[-2:])>30:
            hour += 1
    elif len(string)==4:
        hour = int(string[0:2])
        if int(string[-2:])>30:
            hour += 1
    if hour ==24:
        hour = 0
    return hour

def get_weather_time(string):
    hour = 100
    if len(string) == 7:
        hour = int(string[0])
        if int(string[2:4])>30:
            hour += 1
    elif len(string) == 8:
        hour = int(string[0:2])
        if int(string[3:5])>30:
            hour += 1
    if string[-2:]=='PM':
        if hour<12:
            hour += 12
    elif string[-2:]=='AM':
        if hour==12:
            hour=0
        elif hour>12:
            hour=1
    return hour


def mark_condition(year, month, airport):
    # read files
    if month<10:
        m_str = '0'+str(month)  
    else: 
        m_str = str(month)
    f_fname = 'FlightData/'+str(year)+'_'+m_str+'_ONTIME.csv'
    with open(f_fname,'rb') as fflight: 
        #fd = pd.read_csv(fflight)
        fdata = pd.read_csv(fflight)

    # add colume of weather condition, wind speed, visibility
    fdata['CONDITION'] = None
    fdata['WINDSPEED'] = None
    fdata['VISIBILITY'] = None

    # read time of each flight
    fl_day = fdata['DAY_OF_MONTH']
    fl_dep_time = fdata['CRS_DEP_TIME']
    fl_arr_time = fdata['CRS_ARR_TIME']
    fl_dep_airport = fdata['ORIGIN']
    fl_arr_airport = fdata['DEST']

    # extract row with this airpot
    data_dep = fdata.loc[lambda df: df['ORIGIN'] == airport , :]
    data_arr = fdata.loc[lambda df: df['DEST'] == airport , :]
    fdata = pd.concat([data_dep, data_arr])

    # file size
    (row_f, col_f) = fdata.shape
    print row_f, col_f

    # find the weather of the time
    for i in fdata.index.values:
        w_fname = 'web_scraping/'+str(year)+'_'+airport+'/weather_'+str(year)+'_'+str(month)+'_'+str(fl_day[i])+'_'+airport+'.csv'
        with open(w_fname,'rb') as fweather:
            wdata = pd.read_csv(fweather)
        (row_w, col_w) = wdata.shape
        w_time = wdata['Time (EST)']
        w_cond = wdata['Conditions']
        w_wind = wdata['Wind Speed']
        w_visi = wdata['Visibility']

        for j in wdata.index.values:
            # departure at the airport
            if fl_dep_airport[i]==airport:
                f_hr = get_flight_time(str(fl_dep_time[i]))
            # arrival at the airport
            elif fl_arr_airport[i]==airport:
                f_hr = get_flight_time(str(fl_arr_time[i]))
            w_hr = get_weather_time(str(w_time[j]))
            if f_hr==w_hr:
                fdata.at[i, 'CONDITION'] = w_cond[j]
                fdata.at[i, 'WINDSPEED'] = w_wind[j]
                fdata.at[i, 'VISIBILITY'] = w_visi[j]
        print str(i)+'\n', np.array(fdata.loc[i])
    return fdata

def main():
    # parameters
    year = range(2012,2018)
    month =  range(1,13)
    airport = ['ATL','DFW','ORD','DEN','LAX']
    # initialize
    #for y in year:
    #    for m in month:
    #        mark_condition(y, m)
    
    # mark the weather conditions in each flight
    datas = mark_condition(year[0], month[0], airport[0])

    # group each weather conditions "Clear" "Partly Cloudy" "Overcast" "" ...

    # count the fligth delay rate in each group : (num of flight delay)/(num of total flight)

    
    
if __name__ == "__main__":
    # execute only if run as a script
    main()