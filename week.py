import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
Info1 = pd.read_csv('2017_01_ONTIME.csv')
Info2 = pd.read_csv('2017_02_ONTIME.csv')
Info3 = pd.read_csv('2017_03_ONTIME.csv')
Info4 = pd.read_csv('2017_04_ONTIME.csv')
Info5 = pd.read_csv('2017_05_ONTIME.csv')
Info6 = pd.read_csv('2017_06_ONTIME.csv')
Info7 = pd.read_csv('2017_07_ONTIME.csv')
Info8 = pd.read_csv('2017_08_ONTIME.csv')
Info9 = pd.read_csv('2017_09_ONTIME.csv')
Info10 = pd.read_csv('2017_10_ONTIME.csv')
Info11 = pd.read_csv('2017_11_ONTIME.csv')
Info12 = pd.read_csv('2017_12_ONTIME.csv')
Infot=[Info1,Info2,Info3,Info4,Info5,Info6,Info7,Info8,Info9,Info10,Info11,Info12]
Info=pd.concat(Infot)
DepDelay=Info['ARR_DELAY_NEW']
DepAddr=Info['ORIGIN']
dayofweek=Info['MONTH']
ndayofweek=dayofweek.values
nDepDelay=DepDelay.values
nDepAddr=DepAddr.values    #departure airport
cnt=np.zeros((1,12))
cnt2=np.zeros((1,12))
for w in range (12):
    for i in range (len(nDepAddr)):
        if nDepAddr[i]=='ATL'and ndayofweek[i]==w+1:
            cnt[0][w]+=1
    DAddrIndATL = np.zeros((1,cnt[0][w].astype(int)))
    j=0
    for i in range (len(nDepAddr)):
        if nDepAddr[i]=='ATL' and ndayofweek[i]==w+1:
            DAddrIndATL[0][j]=i
            j+=1
    DAddrIndATLi=DAddrIndATL.astype(int)
    nDepDelayATL=nDepDelay[DAddrIndATLi]
    nDepDelayATLi=nDepDelayATL.astype(int)
    ma=np.amax(nDepDelayATLi)
    print nDepDelayATLi.size

    for i in range (nDepDelayATLi.size):
        if nDepDelayATLi[0][i] > 15:
            cnt2[0][w]+=1

N = 5
y1 = [20, 10, 30, 25, 15]
y2 = [15, 14, 34, 10, 5]
index = np.arange(12)

bar_width = 0.3
plt.bar(index+1, cnt[0], width=0.3, color='y')
plt.bar(index+1, cnt2[0], width=0.3, color='b')
plt.legend(('all flights','delayed flights'))
plt.xlabel('month')
xd=['','Jan','Feb','Mar.','Apr.','May','Jun.','Jul.','Aug.','Sep.','Oct.','Nov.','Dec.']
x=range(len(xd))
plt.xticks(x,xd)
plt.ylabel('number of flights')
plt.title('arrival delay rate regarding month for 2017')
#plt.text(index+1,1.02*cnt[0],str(100*cnt2[0]/cnt[0])+'%')
rate=100*cnt2[0][0]/cnt[0][0]
plt.text(1-0.25,cnt[0][0],'%.2f'% rate+'%')
rate=100*cnt2[0][1]/cnt[0][1]
plt.text(2-0.25,cnt[0][1],'%.2f'% rate+'%')
rate=100*cnt2[0][2]/cnt[0][2]
plt.text(3-0.25,cnt[0][2],'%.2f'% rate+'%')
rate=100*cnt2[0][3]/cnt[0][3]
plt.text(4-0.25,cnt[0][3],'%.2f'% rate+'%')
rate=100*cnt2[0][4]/cnt[0][4]
plt.text(5-0.25,cnt[0][4],'%.2f'% rate+'%')
rate=100*cnt2[0][5]/cnt[0][5]
plt.text(6-0.25,cnt[0][5],'%.2f'% rate+'%')
rate=100*cnt2[0][6]/cnt[0][6]
plt.text(7-0.25,cnt[0][6],'%.2f'% rate+'%')

rate=100*cnt2[0][7]/cnt[0][7]
plt.text(8-0.25,cnt[0][7],'%.2f'% rate+'%')
rate=100*cnt2[0][8]/cnt[0][8]
plt.text(9-0.25,cnt[0][8],'%.2f'% rate+'%')
rate=100*cnt2[0][9]/cnt[0][9]
plt.text(10-0.25,cnt[0][9],'%.2f'% rate+'%')
rate=100*cnt2[0][10]/cnt[0][10]
plt.text(11-0.25,cnt[0][10],'%.2f'% rate+'%')
rate=100*cnt2[0][11]/cnt[0][11]
plt.text(12-0.25,cnt[0][11],'%.2f'% rate+'%')

plt.show()
#        j+=1
# cntt=np.zeros((1,29))
#
# for i in range (28):
#     for j in range(nDepDelayATLi.size):
#         if (nDepDelayATLi[0][j]>10*i) and (nDepDelayATLi[0][j]<=10*(i+1)):
#             cntt[0][i]+=1
# sumcntmp=0
# for i in range (28):
#     sumcntmp += cntt[0][i]
# cnttp=cntt*100/sumcntmp
# #cntt[0][34]=nDepDelayATLi.size-sumcntmp
# xd=['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90',
#     '90-100','100-110','110-120','120-130','130-140','140-150','150-160','160-170',
#     '170-180','180-190','190-200','200-210','210-220','220-230','230-240','240-250',
#     '250-260','260-270','270-280','280-290']
# x=range(len(xd))
#
# plt.plot(x,cnttp[0])
# plt.xlabel('delay time/min') # apply label
# plt.xticks(x,xd,rotation = -45)
# plt.ylabel('percentage/%')
# plt.title('percentage of delay time in Jan. 2012')
# plt.show() # show figure