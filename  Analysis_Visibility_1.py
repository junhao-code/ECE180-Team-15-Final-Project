import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time
import sys
import re


def get_flight_time(string): # 0~23hr
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

def get_weather_time(string): # 0~23hr
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
    print '\nStart cleaning data...'
    # add colume of weather condition, wind speed, visibility
    data['CONDITION'] = None
    data['WINDSPEED'] = None
    data['VISIBILITY'] = None
    data['PERIOD'] = None

    # extract row with this airpot
    data_dep = data.loc[lambda df: df['ORIGIN'] == airport , :]
    #data_dep = data.loc[data['ORIGIN'] == airport , :]
    data_arr = data.loc[lambda df: df['DEST'] == airport , :]
    data_dep_arr = pd.concat([data_dep, data_arr])
    clean_data = data_dep_arr.dropna(axis=0, subset=['DEP_DELAY_NEW','ARR_DELAY_NEW'])
    return clean_data


def mark_condition(year, month, airport):
    print '\nStart marking weather condition...'
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
    #fread = fread.iloc[1:20000]
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
    print '\nMonthly Data Size:', row_f, col_f

    # find the weather of the time
    print '\nStart assigning data...'
    for i in fdata.index.values:
        w_fname = 'web_scraping/'+str(year)+'_'+airport+'/weather_'+str(year)+'_'+str(month)+'_'+str(fl_day[i])+'_'+airport+'.csv'
        with open(w_fname,'rb') as fweather:
            wdata = pd.read_csv(fweather)
        (row_w, col_w) = wdata.shape
        #w_time = wdata['Time (EST)']
        w_time = wdata.ix[:,0]
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
                # set period in the day
                fdata.at[i, 'PERIOD'] = int(f_hr)
                # set condition
                fdata.at[i, 'CONDITION'] = w_cond[j]
                # set wind speed
                if w_wind[j]=='Calm':
                    fdata.at[i, 'WINDSPEED'] = w_wind[j]
                else:
                    wind = re.findall(r"\d+\.?\d*", w_wind[j])
                    if wind != []:
                        fdata.at[i, 'WINDSPEED'] = float(wind[0])
                # set visibility
                visi = re.findall(r"\d+\.?\d*", w_visi[j])
                if visi != []:
                    fdata.at[i, 'VISIBILITY'] = float(visi[0])
        #print str(i)+'\n', np.array(fdata.loc[i])
    return fdata

def group_data_by_period(data, period_hr): #1,2,3,4,6,8,12,24
    assert isinstance(period_hr,int)
    assert 24%period_hr==0
    assert period_hr<=24 and period_hr>0
    gp_num = 24/period_hr
    frames = {}
    # groupby period
    gb_period = data.groupby(data['PERIOD'])
    print '\nTime period of data:', gb_period.groups.keys(), '\n'
    for i in range(gp_num): 
        # concat group 
        dfs = []
        for p in range(period_hr):
            gname = i*period_hr+p
            if gname in gb_period.groups.keys():
                df = gb_period.get_group(gname)
                dfs.append(df)
        # create group dictionary
        dict_name = str(i*period_hr)+'-'+str((i+1)*period_hr-1)
        if dfs==[]:
            df_temp = data.head(1)
            df_temp.at[data.head(1).index.values,:] = None
            frames[dict_name] = df_temp
        else:
            frames[dict_name] = pd.concat(dfs)
    return gp_num, frames


def calculate_flight_delay_rate_bygroup(data, group_type, airport, orig_data):
    tp_name = []
    tp_rate = []
    gb = data.groupby(group_type)
    or_gb = orig_data.groupby(group_type)
    print '\nFlight Delay Rate (in each '+group_type+'):'
    for i in or_gb.groups.keys():
        if i in gb.groups.keys():
            num_dep_del = 0
            num_arr_del = 0
            ggp = gb.get_group(i)
            # number of total flights in the group
            total = len(or_gb.get_group(i))
            #total = len(ggp)
            # group departure & count delay flights
            gb_temp = ggp.groupby(ggp['ORIGIN']==airport)
            if True in gb_temp.groups.keys():
                gb_dep = gb_temp.get_group(True)
                gb_temp1 = gb_dep.groupby([int(r)>=15 for r in gb_dep['DEP_DELAY_NEW']])
                if True in gb_temp1.groups.keys():
                    gb_dep_del = gb_temp1.get_group(True)
                    num_dep_del = len(gb_dep_del)
            # group arrival & count delay flights
            gb_temp2 = ggp.groupby(ggp['DEST']==airport)
            if True in gb_temp2.groups.keys():
                gb_arr = gb_temp2.get_group(True)
                gb_temp3 = gb_arr.groupby(gb_arr['ARR_DELAY_NEW']>=15)
                if True in gb_temp3.groups.keys():
                    gb_arr_del = gb_temp3.get_group(True)
                    num_arr_del = len(gb_arr_del)
            # flight delay rate in the group
            del_rate = float(num_dep_del+num_arr_del)/float(total)
        else:
            del_rate = 0.0
        #print i, del_rate
        tp_name.append(i)
        tp_rate.append(del_rate)
    #print tp_name, tp_rate
    return tp_name, tp_rate

def plot_bar_condition(type_name, type_rate, year, month, airport):
    plt.figure(figsize=(15,8))
    plt.xlabel('CONDITION of weather')
    plt.ylabel('Flight delay rate')
    index = np.arange(len(type_name))
    plt.ylim( (0, 1) )
    plt.xticks(index, type_name, size='small', rotation=60)
    plt.bar(index, type_rate, 0.2, alpha=0.4, color='r')#label=dict_data.keys()[i]
    plt.tight_layout()
    plt.subplots_adjust(wspace=0.8, top=0.9)
    if month>12:
        plt.suptitle(str(year)+' Flight delay rate in each CONDITION at '+airport,fontsize=20) 
        plt.savefig('CONDITION_'+str(year)+'_'+airport+'.png', dpi = 300)
    else:
        plt.suptitle(str(year)+'/'+str(month)+' Flight delay rate in each CONDITION at '+airport,fontsize=20) 
        plt.savefig('CONDITION_'+str(year)+'_'+str(month)+'_'+airport+'.png', dpi = 300)
    plt.close()
    #plt.show()

def plot_pie_condition(type_name, type_rate, year,month, airport):
    rate = list(np.array(type_rate)/np.array(type_rate).sum())
    plt.figure(figsize=(15,8))
    patches,text1,text2 = plt.pie(rate,labels=type_name,autopct = '%3.2f%%', shadow = False, startangle =90, pctdistance = 0.8) 
    for t in text1:
        t.set_size=(30)
    for t in text2:
        t.set_size=(10)
    plt.axis('equal')
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.subplots_adjust(wspace=0.8, top=0.9)
    if month>12:
        plt.suptitle(str(year)+' Factors of Flight delay in each CONDITION at '+airport,fontsize=20)
        plt.savefig('CONDITION_'+str(year)+'_'+airport+'_pie.png', dpi = 300)
    else:
        plt.suptitle(str(year)+'/'+str(month)+' Factors of Flight delay in each CONDITION at '+airport,fontsize=20)
        plt.savefig('CONDITION_'+str(year)+'_'+str(month)+'_'+airport+'_pie.png', dpi = 300)
    plt.close()
    #plt.show()

def plot_scatter_windspeed(tp_name, tp_rate, year, month, airport):
    if tp_name[-1]=='Calm':
        tp_name = tp_name[0:-1]
        tp_rate = tp_rate[0:-1]
    plt.figure(figsize=(15,8))
    plt.xlabel('WIND SPEED (mph)')
    plt.ylabel('Flight delay rate')
    plt.ylim( (-0.05, 1.05) )
    plt.subplots_adjust(wspace=0.8, top=0.9)
    plt.scatter(tp_name, tp_rate, 40, marker='o',color='b')
    plt.grid(axis='y', linestyle='--', color='0.3', linewidth=0.25)
    if month>12:
        plt.suptitle(str(year)+' Flight delay rate in each WINDSPEED at '+airport,fontsize=20)
        plt.savefig('WINDSPEED_'+str(year)+'_'+airport+'_scatter.png', dpi = 300)
    else:
        plt.suptitle(str(year)+'/'+str(month)+' Flight delay rate in each WINDSPEED at '+airport,fontsize=20)
        plt.savefig('WINDSPEED_'+str(year)+'_'+str(month)+'_'+airport+'_scatter.png', dpi = 300)
    #plt.show()
    plt.close()

def plot_scatter_visibility(tp_name, tp_rate, year, month, airport):
    plt.figure(figsize=(15,8))
    plt.xlabel('VISIBILITY (mi)')
    plt.ylabel('Flight delay rate')
    plt.ylim( (-0.05, 1.05) )
    plt.subplots_adjust(wspace=0.8, top=0.9)
    plt.scatter(tp_name, tp_rate, 40, marker='v',color='g')
    plt.grid(axis='y', linestyle='--', color='0.3', linewidth=0.25)
    if month>12:
        plt.suptitle(str(year)+' Flight delay rate in each VISIBILITY at '+airport,fontsize=20)
        plt.savefig('VISIBILITY_'+str(year)+'_'+airport+'_scatter.png', dpi = 300)
    else:
        plt.suptitle(str(year)+'/'+str(month)+' Flight delay rate in each VISIBILITY at '+airport,fontsize=20)
        plt.savefig('VISIBILITY_'+str(year)+'_'+str(month)+'_'+airport+'_scatter.png', dpi = 300)
    #plt.show()
    plt.close()

def group_calculation(data, weather_type, year, month, airport):
    group_num, dict_data = group_data_by_period(data, period_hr=24)
    for i in range(group_num):
        print dict_data.keys()[i]
        input_data = dict_data[dict_data.keys()[i]]
        tp_name, tp_rate = calculate_flight_delay_rate_bygroup(input_data, weather_type, airport, data)
        tp_name, tp_rate = zip(*sorted(zip(tp_name, tp_rate)))
        print tp_name, tp_rate
        if weather_type=='CONDITION':
            # PLOT HIST - http://blog.csdn.net/wishchin/article/details/24906175
            plot_bar_condition(tp_name, tp_rate, year, month, airport)
            plot_pie_condition(tp_name, tp_rate, year, month, airport)
        if weather_type=='WINDSPEED':
            plot_scatter_windspeed(tp_name, tp_rate, year, month, airport)
        if weather_type=='VISIBILITY':
            plot_scatter_visibility(tp_name, tp_rate, year, month, airport)

def main():
    # parameters
    year = range(2012,2018)
    month =  range(1,13)
    airport = ['ATL','DFW','ORD','DEN','LAX']
    weather_tp = ['CONDITION','WINDSPEED','VISIBILITY']
    
    # ================= parameters =================
    for i in range(1,5):
        y = year[5]
        ap = airport[i]
        w = weather_tp[2]
        # merge datas in a year
        ad = []

        for m in month:
            print '\nDate: ', y, m
            # mark the weather conditions in each flight
            datas = mark_condition(y, m, ap)
            ad.append(datas)

            # group each weather conditions ...
            # and count the fligth delay rate in each group : (num of flight delay)/(num of total flight)
            group_calculation(datas, w, y, m, ap)

        alldata = pd.concat(ad)
        alldata.reset_index(drop=True)
    
        # file size
        (row_f, col_f) = alldata.shape
        print '\nALL Data Size:', row_f, col_f

        # group each weather conditions ...
        # and count the fligth delay rate in each group : (num of flight delay)/(num of total flight)
        m = 100
        group_calculation(alldata, w, y, m, ap)
    
    # ================= parameters =================

    
    
if __name__ == "__main__":
    # execute only if run as a script
    main()