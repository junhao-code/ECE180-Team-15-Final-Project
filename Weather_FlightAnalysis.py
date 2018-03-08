import pandas as pd
import numpy as np
import time
import sys
import re

def calculate_flight_delay_rate_bygroup(data, group_type, airport):
    gb = data.groupby(group_type)
    print '\nFlight Delay Rate (in each weather condition):'
    for i in gb.groups.keys():
        num_dep_del = 0
        num_arr_del = 0
        ggp = gb.get_group(i)
        # number of total flights in the group
        total = len(ggp)
        # group departure & count delay flights
        gb_temp = ggp.groupby(ggp['ORIGIN']==airport)
        for k in gb_temp.groups.keys():
            if k==True:
                gb_dep = gb_temp.get_group(True)
                gb_temp1 = gb_dep.groupby([int(r)>=15 for r in gb_dep['DEP_DELAY_NEW']])
                for k1 in gb_temp1.groups.keys():
                    if k1==True:
                        gb_dep_del = gb_temp1.get_group(True)

                        num_dep_del = len(gb_dep_del)
        # group arrival & count delay flights
        gb_temp2 = ggp.groupby(ggp['DEST']==airport)
        for k in gb_temp2.groups.keys():
            if k==True:
                gb_arr = gb_temp2.get_group(True)
                gb_temp3 = gb_arr.groupby(gb_arr['ARR_DELAY_NEW']>=15)
                for k1 in gb_temp3.groups.keys():
                    if k1==True:
                        gb_arr_del = gb_temp3.get_group(True)
                        num_arr_del = len(gb_arr_del)
        # flight delay rate in the group
        del_rate = float(num_dep_del+num_arr_del)/float(total)
        print i, del_rate


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

def clean_data(data, airport):
    # add colume of weather condition, wind speed, visibility
    data['CONDITION'] = None
    data['WINDSPEED'] = None
    data['VISIBILITY'] = None

    # extract row with this airpot
    data_dep = data.loc[lambda df: df['ORIGIN'] == airport , :]
    data_arr = data.loc[lambda df: df['DEST'] == airport , :]
    data_dep_arr = pd.concat([data_dep, data_arr])
    clean_data = data_dep_arr.dropna(axis=0, subset=['DEP_DELAY_NEW','ARR_DELAY_NEW'])
    return clean_data


def mark_condition(year, month, airport):
    # read files
    if month<10:
        m_str = '0'+str(month)  
    else: 
        m_str = str(month)
    f_fname = 'FlightData/'+str(year)+'_'+m_str+'_ONTIME.csv'
    with open(f_fname,'rb') as fflight: 
        #fd = pd.read_csv(fflight)
        fread = pd.read_csv(fflight)

    # ================= test =================
    fread = fread.iloc[1:20000]
    # ================= test =================

    fdata = clean_data(fread, airport)

    # read time of each flight
    fl_day = fdata['DAY_OF_MONTH']
    fl_dep_time = fdata['CRS_DEP_TIME']
    fl_arr_time = fdata['CRS_ARR_TIME']
    fl_dep_airport = fdata['ORIGIN']
    fl_arr_airport = fdata['DEST']

    # file size
    (row_f, col_f) = fdata.shape
    print '\nData Size:'
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
                # set condition
                fdata.at[i, 'CONDITION'] = w_cond[j]
                # set wind speed
                if w_wind[j]=='Calm':
                    fdata.at[i, 'WINDSPEED'] = w_wind[j]
                else:
                    wind = re.findall(r"\d+\.?\d*", w_wind[j])
                    fdata.at[i, 'WINDSPEED'] = wind[0]
                # set visibility
                visi = re.findall(r"\d+\.?\d*", w_visi[j])
                fdata.at[i, 'VISIBILITY'] = visi[0]
        #print str(i)+'\n', np.array(fdata.loc[i])
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
    
    # ================= parameters =================
    # mark the weather conditions in each flight
    datas = mark_condition(year[0], month[0], airport[0])
    
    # group each weather conditions "Clear" "Partly Cloudy" "Overcast" "" ...
    # and count the fligth delay rate in each group : (num of flight delay)/(num of total flight)
    calculate_flight_delay_rate_bygroup(datas, 'CONDITION', airport[0])

    # ================= parameters =================

    
    
if __name__ == "__main__":
    # execute only if run as a script
    main()