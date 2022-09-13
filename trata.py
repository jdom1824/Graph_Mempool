from encodings import utf_8
import json
from mimetypes import init
from turtle import color
import matplotlib.pyplot as plt
import requests
import random
import datetime
import numpy as np
import random
time = []
fee = []
rtime = []
rfee = []
txid = []
rojo = []
bl = []
tiblock = []
heblock = []
datimeblock = []
clock = []
clockb = []
color_list = ["navy", "mediumpurple", "indigo", "purple", "aqua", "orange", "turquoise", "slategrey", "olive", "chartreuse"]

transaction = requests.get("https://mempool.observer/api/getMempoolEntries")
transaction =  transaction.json()
with open('getMempoolEntries.json', 'w') as f:
    json.dump(transaction, f)


blockes = requests.get("https://mempool.observer/api/getBlockEntries")
blockes =  blockes.json()
with open('getBlockEntries.json', 'w') as f:
    json.dump(blockes, f)

with open('getMempoolEntries.json', 'r', encoding="utf_8") as file:
    data = file.read()
    transa = json.loads(data)

with open('getBlockEntries.json', 'r', encoding="utf_8") as file:
    data = file.read()
    block = json.loads(data)

    
for n in range(0,10):
    blocki = block[n]
    bl.append(blocki["shortTXIDs"])
    tiblock.append(blocki["timestamp"])
    date_time = datetime.datetime.fromtimestamp(tiblock[n])
    datimeblock.append(date_time.strftime('%H:%M'))
    print(datimeblock)
    heblock.append(blocki["height"])
bl = str(bl)[1:-1]
print(tiblock)
for w in range(0, len(transa)):
    datato = transa[w]
    if (datato["fee"]/datato["size"]) < 150 and datato["entryTime"] >= 10:
        fee.append(datato["fee"]/datato["size"])
        time.append(datato["entryTime"])
        if datato["txid"][0:16] in bl:
            rfee.append(datato["fee"]/datato["size"])
            rtime.append(datato["entryTime"])
print(time[1])
print(time[-1])
variable = 1382

for i in range(0,6):
    cl = (time[-1] + variable * i)
    clockb.append(cl)
    cl = datetime.datetime.fromtimestamp(cl)
    clock.append(cl.strftime('%H:%M'))
print(clock)

plt.scatter(time,fee, s=0.5, color='grey')
plt.scatter(rtime,rfee, s=0.5, color='red')
plt.xlabel("Time(Hour:Minutes)")
plt.ylabel("Satoshi/Byte")
#plt.xticks(tiblock, datimeblock, rotation=20)
plt.xticks(clockb, clock)
plt.title("Analysis of Bitcoin Transactions")
for i in range (0,10):
    plt.bar(tiblock[i], 150, color=random.choice(color_list), width=40)
plt.show()


