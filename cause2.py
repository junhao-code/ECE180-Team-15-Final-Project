import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
Info1 = pd.read_csv('2017_01_ONTIME.csv')
DepDelay=Info1['DEP_DELAY_NEW']
carrier=Info1['CARRIER_DELAY']
ncarrier=carrier.values
where_are_nan = np.isnan(ncarrier)
ncarrier[where_are_nan] = 0
cntc=np.zeros((1,12))
weather=Info1['WEATHER_DELAY']
nweather=weather.values
where_are_nan = np.isnan(nweather)
nweather[where_are_nan] = 0
cntw=np.zeros((1,12))
nas=Info1['NAS_DELAY']
nnas=nas.values
where_are_nan = np.isnan(nnas)
nnas[where_are_nan] = 0
cntn=np.zeros((1,12))
security=Info1['SECURITY_DELAY']
nsecurity=security.values
where_are_nan = np.isnan(nsecurity)
nsecurity[where_are_nan] = 0
cnts=np.zeros((1,12))
lateaircraft=Info1['LATE_AIRCRAFT_DELAY']
nlateaircraft=lateaircraft.values
where_are_nan = np.isnan(nlateaircraft)
nlateaircraft[where_are_nan] = 0
cntl=np.zeros((1,12))
DepAddr=Info1['ORIGIN']
nDepDelay=DepDelay.values
nDepAddr=DepAddr.values
cnt=0
for i in range(len(nDepAddr)):
    if nDepAddr[i] == 'ATL':
        cnt += 1
    DAddrIndATL = np.zeros((1, cnt))
    j = 0
for i in range(len(nDepAddr)):
    if nDepAddr[i] == 'ATL':
        DAddrIndATL[0][j] = i
        j += 1
DAddrIndATLi = DAddrIndATL.astype(int)
nDepDelayATL = nDepDelay[DAddrIndATLi]
ncarrier=ncarrier[DAddrIndATLi]
nweather=nweather[DAddrIndATLi]
nnas=nnas[DAddrIndATLi]
nsecurity=nsecurity[DAddrIndATLi]
nlateaircraft=nlateaircraft[DAddrIndATLi]
nDepDelayATLi = nDepDelayATL.astype(int)
for i in range(nDepDelayATLi.size):
    if nDepDelayATLi[0][i] > 15:
        cntc[0][0] += ncarrier[0][i]
        cntw[0][0] += nweather[0][i]
        cntn[0][0] += nnas[0][i]
        cnts[0][0] += nsecurity[0][i]
        cntl[0][0] += nlateaircraft[0][i]

Info1 = pd.read_csv('2017_02_ONTIME.csv')
DepDelay=Info1['DEP_DELAY_NEW']
carrier=Info1['CARRIER_DELAY']
ncarrier=carrier.values
where_are_nan = np.isnan(ncarrier)
ncarrier[where_are_nan] = 0
weather=Info1['WEATHER_DELAY']
nweather=weather.values
where_are_nan = np.isnan(nweather)
nweather[where_are_nan] = 0
nas=Info1['NAS_DELAY']
nnas=nas.values
where_are_nan = np.isnan(nnas)
nnas[where_are_nan] = 0
security=Info1['SECURITY_DELAY']
nsecurity=security.values
where_are_nan = np.isnan(nsecurity)
nsecurity[where_are_nan] = 0
lateaircraft=Info1['LATE_AIRCRAFT_DELAY']
nlateaircraft=lateaircraft.values
where_are_nan = np.isnan(nlateaircraft)
nlateaircraft[where_are_nan] = 0
DepAddr=Info1['ORIGIN']
nDepDelay=DepDelay.values
nDepAddr=DepAddr.values
cnt=0
for i in range(len(nDepAddr)):
    if nDepAddr[i] == 'ATL':
        cnt += 1
    DAddrIndATL = np.zeros((1, cnt))
    j = 0
for i in range(len(nDepAddr)):
    if nDepAddr[i] == 'ATL':
        DAddrIndATL[0][j] = i
        j += 1
DAddrIndATLi = DAddrIndATL.astype(int)
nDepDelayATL = nDepDelay[DAddrIndATLi]
ncarrier=ncarrier[DAddrIndATLi]
nweather=nweather[DAddrIndATLi]
nnas=nnas[DAddrIndATLi]
nsecurity=nsecurity[DAddrIndATLi]
nlateaircraft=nlateaircraft[DAddrIndATLi]
nDepDelayATLi = nDepDelayATL.astype(int)
for i in range(nDepDelayATLi.size):
    if nDepDelayATLi[0][i] > 15:
        cntc[0][1] += ncarrier[0][i]
        cntw[0][1] += nweather[0][i]
        cntn[0][1] += nnas[0][i]
        cnts[0][1] += nsecurity[0][i]
        cntl[0][1] += nlateaircraft[0][i]

Info1 = pd.read_csv('2017_03_ONTIME.csv')
DepDelay=Info1['DEP_DELAY_NEW']
carrier=Info1['CARRIER_DELAY']
ncarrier=carrier.values
where_are_nan = np.isnan(ncarrier)
ncarrier[where_are_nan] = 0
weather=Info1['WEATHER_DELAY']
nweather=weather.values
where_are_nan = np.isnan(nweather)
nweather[where_are_nan] = 0
nas=Info1['NAS_DELAY']
nnas=nas.values
where_are_nan = np.isnan(nnas)
nnas[where_are_nan] = 0
security=Info1['SECURITY_DELAY']
nsecurity=security.values
where_are_nan = np.isnan(nsecurity)
nsecurity[where_are_nan] = 0
lateaircraft=Info1['LATE_AIRCRAFT_DELAY']
nlateaircraft=lateaircraft.values
where_are_nan = np.isnan(nlateaircraft)
nlateaircraft[where_are_nan] = 0
DepAddr=Info1['ORIGIN']
nDepDelay=DepDelay.values
nDepAddr=DepAddr.values
cnt=0
for i in range(len(nDepAddr)):
    if nDepAddr[i] == 'ATL':
        cnt += 1
    DAddrIndATL = np.zeros((1, cnt))
    j = 0
for i in range(len(nDepAddr)):
    if nDepAddr[i] == 'ATL':
        DAddrIndATL[0][j] = i
        j += 1
DAddrIndATLi = DAddrIndATL.astype(int)
nDepDelayATL = nDepDelay[DAddrIndATLi]
ncarrier=ncarrier[DAddrIndATLi]
nweather=nweather[DAddrIndATLi]
nnas=nnas[DAddrIndATLi]
nsecurity=nsecurity[DAddrIndATLi]
nlateaircraft=nlateaircraft[DAddrIndATLi]
nDepDelayATLi = nDepDelayATL.astype(int)
for i in range(nDepDelayATLi.size):
    if nDepDelayATLi[0][i] > 15:
        cntc[0][2] += ncarrier[0][i]
        cntw[0][2] += nweather[0][i]
        cntn[0][2] += nnas[0][i]
        cnts[0][2] += nsecurity[0][i]
        cntl[0][2] += nlateaircraft[0][i]

Info1 = pd.read_csv('2017_04_ONTIME.csv')
DepDelay=Info1['DEP_DELAY_NEW']
carrier=Info1['CARRIER_DELAY']
ncarrier=carrier.values
where_are_nan = np.isnan(ncarrier)
ncarrier[where_are_nan] = 0
weather=Info1['WEATHER_DELAY']
nweather=weather.values
where_are_nan = np.isnan(nweather)
nweather[where_are_nan] = 0
nas=Info1['NAS_DELAY']
nnas=nas.values
where_are_nan = np.isnan(nnas)
nnas[where_are_nan] = 0
security=Info1['SECURITY_DELAY']
nsecurity=security.values
where_are_nan = np.isnan(nsecurity)
nsecurity[where_are_nan] = 0
lateaircraft=Info1['LATE_AIRCRAFT_DELAY']
nlateaircraft=lateaircraft.values
where_are_nan = np.isnan(nlateaircraft)
nlateaircraft[where_are_nan] = 0
DepAddr=Info1['ORIGIN']
nDepDelay=DepDelay.values
nDepAddr=DepAddr.values
cnt=0
for i in range(len(nDepAddr)):
    if nDepAddr[i] == 'ATL':
        cnt += 1
    DAddrIndATL = np.zeros((1, cnt))
    j = 0
for i in range(len(nDepAddr)):
    if nDepAddr[i] == 'ATL':
        DAddrIndATL[0][j] = i
        j += 1
DAddrIndATLi = DAddrIndATL.astype(int)
nDepDelayATL = nDepDelay[DAddrIndATLi]
ncarrier=ncarrier[DAddrIndATLi]
nweather=nweather[DAddrIndATLi]
nnas=nnas[DAddrIndATLi]
nsecurity=nsecurity[DAddrIndATLi]
nlateaircraft=nlateaircraft[DAddrIndATLi]
nDepDelayATLi = nDepDelayATL.astype(int)
for i in range(nDepDelayATLi.size):
    if nDepDelayATLi[0][i] > 15:
        cntc[0][3] += ncarrier[0][i]
        cntw[0][3] += nweather[0][i]
        cntn[0][3] += nnas[0][i]
        cnts[0][3] += nsecurity[0][i]
        cntl[0][3] += nlateaircraft[0][i]

Info1 = pd.read_csv('2017_05_ONTIME.csv')
DepDelay=Info1['DEP_DELAY_NEW']
carrier=Info1['CARRIER_DELAY']
ncarrier=carrier.values
where_are_nan = np.isnan(ncarrier)
ncarrier[where_are_nan] = 0
weather=Info1['WEATHER_DELAY']
nweather=weather.values
where_are_nan = np.isnan(nweather)
nweather[where_are_nan] = 0
nas=Info1['NAS_DELAY']
nnas=nas.values
where_are_nan = np.isnan(nnas)
nnas[where_are_nan] = 0
security=Info1['SECURITY_DELAY']
nsecurity=security.values
where_are_nan = np.isnan(nsecurity)
nsecurity[where_are_nan] = 0
lateaircraft=Info1['LATE_AIRCRAFT_DELAY']
nlateaircraft=lateaircraft.values
where_are_nan = np.isnan(nlateaircraft)
nlateaircraft[where_are_nan] = 0
DepAddr=Info1['ORIGIN']
nDepDelay=DepDelay.values
nDepAddr=DepAddr.values
cnt=0
for i in range(len(nDepAddr)):
    if nDepAddr[i] == 'ATL':
        cnt += 1
    DAddrIndATL = np.zeros((1, cnt))
    j = 0
for i in range(len(nDepAddr)):
    if nDepAddr[i] == 'ATL':
        DAddrIndATL[0][j] = i
        j += 1
DAddrIndATLi = DAddrIndATL.astype(int)
nDepDelayATL = nDepDelay[DAddrIndATLi]
ncarrier=ncarrier[DAddrIndATLi]
nweather=nweather[DAddrIndATLi]
nnas=nnas[DAddrIndATLi]
nsecurity=nsecurity[DAddrIndATLi]
nlateaircraft=nlateaircraft[DAddrIndATLi]
nDepDelayATLi = nDepDelayATL.astype(int)
for i in range(nDepDelayATLi.size):
    if nDepDelayATLi[0][i] > 15:
        cntc[0][4] += ncarrier[0][i]
        cntw[0][4] += nweather[0][i]
        cntn[0][4] += nnas[0][i]
        cnts[0][4] += nsecurity[0][i]
        cntl[0][4] += nlateaircraft[0][i]

Info1 = pd.read_csv('2017_06_ONTIME.csv')
DepDelay=Info1['DEP_DELAY_NEW']
carrier=Info1['CARRIER_DELAY']
ncarrier=carrier.values
where_are_nan = np.isnan(ncarrier)
ncarrier[where_are_nan] = 0
weather=Info1['WEATHER_DELAY']
nweather=weather.values
where_are_nan = np.isnan(nweather)
nweather[where_are_nan] = 0
nas=Info1['NAS_DELAY']
nnas=nas.values
where_are_nan = np.isnan(nnas)
nnas[where_are_nan] = 0
security=Info1['SECURITY_DELAY']
nsecurity=security.values
where_are_nan = np.isnan(nsecurity)
nsecurity[where_are_nan] = 0
lateaircraft=Info1['LATE_AIRCRAFT_DELAY']
nlateaircraft=lateaircraft.values
where_are_nan = np.isnan(nlateaircraft)
nlateaircraft[where_are_nan] = 0
DepAddr=Info1['ORIGIN']
nDepDelay=DepDelay.values
nDepAddr=DepAddr.values
cnt=0
for i in range(len(nDepAddr)):
    if nDepAddr[i] == 'ATL':
        cnt += 1
    DAddrIndATL = np.zeros((1, cnt))
    j = 0
for i in range(len(nDepAddr)):
    if nDepAddr[i] == 'ATL':
        DAddrIndATL[0][j] = i
        j += 1
DAddrIndATLi = DAddrIndATL.astype(int)
nDepDelayATL = nDepDelay[DAddrIndATLi]
ncarrier=ncarrier[DAddrIndATLi]
nweather=nweather[DAddrIndATLi]
nnas=nnas[DAddrIndATLi]
nsecurity=nsecurity[DAddrIndATLi]
nlateaircraft=nlateaircraft[DAddrIndATLi]
nDepDelayATLi = nDepDelayATL.astype(int)
for i in range(nDepDelayATLi.size):
    if nDepDelayATLi[0][i] > 15:
        cntc[0][5] += ncarrier[0][i]
        cntw[0][5] += nweather[0][i]
        cntn[0][5] += nnas[0][i]
        cnts[0][5] += nsecurity[0][i]
        cntl[0][5] += nlateaircraft[0][i]

Info1 = pd.read_csv('2017_07_ONTIME.csv')
DepDelay=Info1['DEP_DELAY_NEW']
carrier=Info1['CARRIER_DELAY']
ncarrier=carrier.values
where_are_nan = np.isnan(ncarrier)
ncarrier[where_are_nan] = 0
weather=Info1['WEATHER_DELAY']
nweather=weather.values
where_are_nan = np.isnan(nweather)
nweather[where_are_nan] = 0
nas=Info1['NAS_DELAY']
nnas=nas.values
where_are_nan = np.isnan(nnas)
nnas[where_are_nan] = 0
security=Info1['SECURITY_DELAY']
nsecurity=security.values
where_are_nan = np.isnan(nsecurity)
nsecurity[where_are_nan] = 0
lateaircraft=Info1['LATE_AIRCRAFT_DELAY']
nlateaircraft=lateaircraft.values
where_are_nan = np.isnan(nlateaircraft)
nlateaircraft[where_are_nan] = 0
DepAddr=Info1['ORIGIN']
nDepDelay=DepDelay.values
nDepAddr=DepAddr.values
cnt=0
for i in range(len(nDepAddr)):
    if nDepAddr[i] == 'ATL':
        cnt += 1
    DAddrIndATL = np.zeros((1, cnt))
    j = 0
for i in range(len(nDepAddr)):
    if nDepAddr[i] == 'ATL':
        DAddrIndATL[0][j] = i
        j += 1
DAddrIndATLi = DAddrIndATL.astype(int)
nDepDelayATL = nDepDelay[DAddrIndATLi]
ncarrier=ncarrier[DAddrIndATLi]
nweather=nweather[DAddrIndATLi]
nnas=nnas[DAddrIndATLi]
nsecurity=nsecurity[DAddrIndATLi]
nlateaircraft=nlateaircraft[DAddrIndATLi]
nDepDelayATLi = nDepDelayATL.astype(int)
for i in range(nDepDelayATLi.size):
    if nDepDelayATLi[0][i] > 15:
        cntc[0][6] += ncarrier[0][i]
        cntw[0][6] += nweather[0][i]
        cntn[0][6] += nnas[0][i]
        cnts[0][6] += nsecurity[0][i]
        cntl[0][6] += nlateaircraft[0][i]

Info1 = pd.read_csv('2017_08_ONTIME.csv')
DepDelay=Info1['DEP_DELAY_NEW']
carrier=Info1['CARRIER_DELAY']
ncarrier=carrier.values
where_are_nan = np.isnan(ncarrier)
ncarrier[where_are_nan] = 0
weather=Info1['WEATHER_DELAY']
nweather=weather.values
where_are_nan = np.isnan(nweather)
nweather[where_are_nan] = 0
nas=Info1['NAS_DELAY']
nnas=nas.values
where_are_nan = np.isnan(nnas)
nnas[where_are_nan] = 0
security=Info1['SECURITY_DELAY']
nsecurity=security.values
where_are_nan = np.isnan(nsecurity)
nsecurity[where_are_nan] = 0
lateaircraft=Info1['LATE_AIRCRAFT_DELAY']
nlateaircraft=lateaircraft.values
where_are_nan = np.isnan(nlateaircraft)
nlateaircraft[where_are_nan] = 0
DepAddr=Info1['ORIGIN']
nDepDelay=DepDelay.values
nDepAddr=DepAddr.values
cnt=0
for i in range(len(nDepAddr)):
    if nDepAddr[i] == 'ATL':
        cnt += 1
    DAddrIndATL = np.zeros((1, cnt))
    j = 0
for i in range(len(nDepAddr)):
    if nDepAddr[i] == 'ATL':
        DAddrIndATL[0][j] = i
        j += 1
DAddrIndATLi = DAddrIndATL.astype(int)
nDepDelayATL = nDepDelay[DAddrIndATLi]
ncarrier=ncarrier[DAddrIndATLi]
nweather=nweather[DAddrIndATLi]
nnas=nnas[DAddrIndATLi]
nsecurity=nsecurity[DAddrIndATLi]
nlateaircraft=nlateaircraft[DAddrIndATLi]
nDepDelayATLi = nDepDelayATL.astype(int)
for i in range(nDepDelayATLi.size):
    if nDepDelayATLi[0][i] > 15:
        cntc[0][7] += ncarrier[0][i]
        cntw[0][7] += nweather[0][i]
        cntn[0][7] += nnas[0][i]
        cnts[0][7] += nsecurity[0][i]
        cntl[0][7] += nlateaircraft[0][i]

Info1 = pd.read_csv('2017_09_ONTIME.csv')
DepDelay=Info1['DEP_DELAY_NEW']
carrier=Info1['CARRIER_DELAY']
ncarrier=carrier.values
where_are_nan = np.isnan(ncarrier)
ncarrier[where_are_nan] = 0
weather=Info1['WEATHER_DELAY']
nweather=weather.values
where_are_nan = np.isnan(nweather)
nweather[where_are_nan] = 0
nas=Info1['NAS_DELAY']
nnas=nas.values
where_are_nan = np.isnan(nnas)
nnas[where_are_nan] = 0
security=Info1['SECURITY_DELAY']
nsecurity=security.values
where_are_nan = np.isnan(nsecurity)
nsecurity[where_are_nan] = 0
lateaircraft=Info1['LATE_AIRCRAFT_DELAY']
nlateaircraft=lateaircraft.values
where_are_nan = np.isnan(nlateaircraft)
nlateaircraft[where_are_nan] = 0
DepAddr=Info1['ORIGIN']
nDepDelay=DepDelay.values
nDepAddr=DepAddr.values
cnt=0
for i in range(len(nDepAddr)):
    if nDepAddr[i] == 'ATL':
        cnt += 1
    DAddrIndATL = np.zeros((1, cnt))
    j = 0
for i in range(len(nDepAddr)):
    if nDepAddr[i] == 'ATL':
        DAddrIndATL[0][j] = i
        j += 1
DAddrIndATLi = DAddrIndATL.astype(int)
nDepDelayATL = nDepDelay[DAddrIndATLi]
ncarrier=ncarrier[DAddrIndATLi]
nweather=nweather[DAddrIndATLi]
nnas=nnas[DAddrIndATLi]
nsecurity=nsecurity[DAddrIndATLi]
nlateaircraft=nlateaircraft[DAddrIndATLi]
nDepDelayATLi = nDepDelayATL.astype(int)
for i in range(nDepDelayATLi.size):
    if nDepDelayATLi[0][i] > 15:
        cntc[0][8] += ncarrier[0][i]
        cntw[0][8] += nweather[0][i]
        cntn[0][8] += nnas[0][i]
        cnts[0][8] += nsecurity[0][i]
        cntl[0][8] += nlateaircraft[0][i]

Info1 = pd.read_csv('2017_10_ONTIME.csv')
DepDelay=Info1['DEP_DELAY_NEW']
carrier=Info1['CARRIER_DELAY']
ncarrier=carrier.values
where_are_nan = np.isnan(ncarrier)
ncarrier[where_are_nan] = 0
weather=Info1['WEATHER_DELAY']
nweather=weather.values
where_are_nan = np.isnan(nweather)
nweather[where_are_nan] = 0
nas=Info1['NAS_DELAY']
nnas=nas.values
where_are_nan = np.isnan(nnas)
nnas[where_are_nan] = 0
security=Info1['SECURITY_DELAY']
nsecurity=security.values
where_are_nan = np.isnan(nsecurity)
nsecurity[where_are_nan] = 0
lateaircraft=Info1['LATE_AIRCRAFT_DELAY']
nlateaircraft=lateaircraft.values
where_are_nan = np.isnan(nlateaircraft)
nlateaircraft[where_are_nan] = 0
DepAddr=Info1['ORIGIN']
nDepDelay=DepDelay.values
nDepAddr=DepAddr.values
cnt=0
for i in range(len(nDepAddr)):
    if nDepAddr[i] == 'ATL':
        cnt += 1
    DAddrIndATL = np.zeros((1, cnt))
    j = 0
for i in range(len(nDepAddr)):
    if nDepAddr[i] == 'ATL':
        DAddrIndATL[0][j] = i
        j += 1
DAddrIndATLi = DAddrIndATL.astype(int)
nDepDelayATL = nDepDelay[DAddrIndATLi]
ncarrier=ncarrier[DAddrIndATLi]
nweather=nweather[DAddrIndATLi]
nnas=nnas[DAddrIndATLi]
nsecurity=nsecurity[DAddrIndATLi]
nlateaircraft=nlateaircraft[DAddrIndATLi]
nDepDelayATLi = nDepDelayATL.astype(int)
for i in range(nDepDelayATLi.size):
    if nDepDelayATLi[0][i] > 15:
        cntc[0][9] += ncarrier[0][i]
        cntw[0][9] += nweather[0][i]
        cntn[0][9] += nnas[0][i]
        cnts[0][9] += nsecurity[0][i]
        cntl[0][9] += nlateaircraft[0][i]

Info1 = pd.read_csv('2017_11_ONTIME.csv')
DepDelay=Info1['DEP_DELAY_NEW']
carrier=Info1['CARRIER_DELAY']
ncarrier=carrier.values
where_are_nan = np.isnan(ncarrier)
ncarrier[where_are_nan] = 0
weather=Info1['WEATHER_DELAY']
nweather=weather.values
where_are_nan = np.isnan(nweather)
nweather[where_are_nan] = 0
nas=Info1['NAS_DELAY']
nnas=nas.values
where_are_nan = np.isnan(nnas)
nnas[where_are_nan] = 0
security=Info1['SECURITY_DELAY']
nsecurity=security.values
where_are_nan = np.isnan(nsecurity)
nsecurity[where_are_nan] = 0
lateaircraft=Info1['LATE_AIRCRAFT_DELAY']
nlateaircraft=lateaircraft.values
where_are_nan = np.isnan(nlateaircraft)
nlateaircraft[where_are_nan] = 0
DepAddr=Info1['ORIGIN']
nDepDelay=DepDelay.values
nDepAddr=DepAddr.values
cnt=0
for i in range(len(nDepAddr)):
    if nDepAddr[i] == 'ATL':
        cnt += 1
    DAddrIndATL = np.zeros((1, cnt))
    j = 0
for i in range(len(nDepAddr)):
    if nDepAddr[i] == 'ATL':
        DAddrIndATL[0][j] = i
        j += 1
DAddrIndATLi = DAddrIndATL.astype(int)
nDepDelayATL = nDepDelay[DAddrIndATLi]
ncarrier=ncarrier[DAddrIndATLi]
nweather=nweather[DAddrIndATLi]
nnas=nnas[DAddrIndATLi]
nsecurity=nsecurity[DAddrIndATLi]
nlateaircraft=nlateaircraft[DAddrIndATLi]
nDepDelayATLi = nDepDelayATL.astype(int)
for i in range(nDepDelayATLi.size):
    if nDepDelayATLi[0][i] > 15:
        cntc[0][10] += ncarrier[0][i]
        cntw[0][10] += nweather[0][i]
        cntn[0][10] += nnas[0][i]
        cnts[0][10] += nsecurity[0][i]
        cntl[0][10] += nlateaircraft[0][i]

Info1 = pd.read_csv('2017_12_ONTIME.csv')
DepDelay=Info1['DEP_DELAY_NEW']
carrier=Info1['CARRIER_DELAY']
ncarrier=carrier.values
where_are_nan = np.isnan(ncarrier)
ncarrier[where_are_nan] = 0
weather=Info1['WEATHER_DELAY']
nweather=weather.values
where_are_nan = np.isnan(nweather)
nweather[where_are_nan] = 0
nas=Info1['NAS_DELAY']
nnas=nas.values
where_are_nan = np.isnan(nnas)
nnas[where_are_nan] = 0
security=Info1['SECURITY_DELAY']
nsecurity=security.values
where_are_nan = np.isnan(nsecurity)
nsecurity[where_are_nan] = 0
lateaircraft=Info1['LATE_AIRCRAFT_DELAY']
nlateaircraft=lateaircraft.values
where_are_nan = np.isnan(nlateaircraft)
nlateaircraft[where_are_nan] = 0
DepAddr=Info1['ORIGIN']
nDepDelay=DepDelay.values
nDepAddr=DepAddr.values
cnt=0
for i in range(len(nDepAddr)):
    if nDepAddr[i] == 'ATL':
        cnt += 1
    DAddrIndATL = np.zeros((1, cnt))
    j = 0
for i in range(len(nDepAddr)):
    if nDepAddr[i] == 'ATL':
        DAddrIndATL[0][j] = i
        j += 1
DAddrIndATLi = DAddrIndATL.astype(int)
nDepDelayATL = nDepDelay[DAddrIndATLi]
ncarrier=ncarrier[DAddrIndATLi]
nweather=nweather[DAddrIndATLi]
nnas=nnas[DAddrIndATLi]
nsecurity=nsecurity[DAddrIndATLi]
nlateaircraft=nlateaircraft[DAddrIndATLi]
nDepDelayATLi = nDepDelayATL.astype(int)
for i in range(nDepDelayATLi.size):
    if nDepDelayATLi[0][i] > 15:
        cntc[0][11] += ncarrier[0][i]
        cntw[0][11] += nweather[0][i]
        cntn[0][11] += nnas[0][i]
        cnts[0][11] += nsecurity[0][i]
        cntl[0][11] += nlateaircraft[0][i]

# bar_width = 0.3
# index = np.arange(12)
# plt.bar(index+1, cntc[0], width=0.3, color='y')
# print 0
# plt.bar(index+1, cntw[0], width=0.3, color='b',bottom=cntc[0])
# print 1
# plt.bar(index+1, cntn[0], width=0.3, color='r',bottom=cntw[0]+cntc[0])
# print 2
# plt.bar(index+1, cnts[0], width=0.3, color='g',bottom=cntn[0]+cntw[0]+cntc[0])
# print 3
# plt.bar(index+1, cntl[0], width=0.3, color='m',bottom=cnts[0]+cntn[0]+cntw[0]+cntc[0])
# print 4
# plt.legend(('carrier','weather','nas','security','late aircraft'))
# plt.xlabel('month')
# xd=['','Jan','Feb','Mar.','Apr.','May','Jun.','Jul.','Aug.','Sep.','Oct.','Nov.','Dec.']
# x=range(len(xd))
# plt.xticks(x,xd)
# plt.ylabel('minutes delayed')
# plt.title('causes of departure delay vs. month for 2017')
# plt.show()

labels = 'carrier','weather','nas','security','late aircraft'
sc=np.sum(cntc)
sw=np.sum(cntw)
sn=np.sum(cntn)
ss=np.sum(cnts)
sl=np.sum(cntl)
st=sc+sw+sn+ss+sl
fc=100*sc/st
fw=100*sw/st
fn=100*sn/st
fs=100*ss/st
fl=100*sl/st
fracs = [fc,fw,fn,fs,fl]
explode = [0, 0.1, 0, 0, 0]
plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse

plt.pie(x=fracs, labels=labels, explode=explode, autopct='%3.1f %%',
        shadow=True, labeldistance=1.1, startangle=90, pctdistance=0.6
        )
plt.show()