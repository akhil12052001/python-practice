from cProfile import label
from turtle import color
import matplotlib.pyplot as plt
import numpy as np

data = {'jan': 10, 'feb': 15, 'march': 22, 'april': 30}
data1 = {'may': 76, 'june': 78, 'july': 86, 'august': 88}

month = list(data.keys())
month1=list(data1.keys())
temp = list(data.values())
hum = list(data1.values())

fig = plt.figure(figsize=(10, 5))
#x_axis=np.arange(len(month))

#plt.bar(x_axis-0.2, temp, color='blue',width=0.1,label="teemprator")
#plt.bar(x_axis+0.2, hum, color='red',width=0.1,label="humidity")
#plt.xticks(x_axis,month)

plt.pie(temp,labels=month,colors=['red','blue','black','yellow'])
plt.pie(hum,labels=month1,colors=['#4287f5','#42f566','#7e42f5','#f5429e'])



#plt.xlabel("months")
#plt.ylabel("tempertor and humidity")

plt.title("monthly data of frequncy of temprator and humidity")
plt.show()
