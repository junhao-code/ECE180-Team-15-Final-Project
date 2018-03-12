import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
Info = pd.read_csv('2017_01_ONTIME.csv')
print(Info.columns)
DepDelay=Info['DEP_DELAY_NEW']
DepAddr=Info['ORIGIN']
nDepDelay=DepDelay.values
nDepAddr=DepAddr.values    #departure airport
cnt=0
for i in range (len(nDepAddr)):
    if nDepAddr[i]=='ATL':
        cnt+=1
DAddrIndATL = np.zeros((1,cnt))
j=0
for i in range (len(nDepAddr)):
    if nDepAddr[i]=='ATL':
        DAddrIndATL[0][j]=i
        j+=1
DAddrIndATLi=DAddrIndATL.astype(int)
nDepDelayATL=nDepDelay[DAddrIndATLi]
nDepDelayATLi=nDepDelayATL.astype(int)
ma=np.amax(nDepDelayATLi)
print nDepDelayATLi.size
cntt=np.zeros((1,29))

for i in range (28):
    for j in range(nDepDelayATLi.size):
        if (nDepDelayATLi[0][j]>10*i) and (nDepDelayATLi[0][j]<=10*(i+1)):
            cntt[0][i]+=1
sumcntmp=0
for i in range (28):
    sumcntmp += cntt[0][i]
cnttp=cntt*100/sumcntmp
#cntt[0][34]=nDepDelayATLi.size-sumcntmp
xd=['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90',
    '90-100','100-110','110-120','120-130','130-140','140-150','150-160','160-170',
    '170-180','180-190','190-200','200-210','210-220','220-230','230-240','240-250',
    '250-260','260-270','270-280','280-290']
x=range(len(xd))

plt.plot(x,cnttp[0])
plt.xlabel('delay time/min') # apply label
plt.xticks(x,xd,rotation = -45)
plt.ylabel('percentage/%')
plt.title('percentage of delay time in Jan. 2017')
plt.show() # show figure