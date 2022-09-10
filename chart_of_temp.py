import matplotlib.pyplot as plt
import numpy as np

data={'jan':10,'feb':15,'march':22,'april':30}
data1={'jan':76,'feb':78,'march':86,'april':88}
month=list(data.keys())
temp=list(data.values())
hum=list(data1.values())
fig=plt.figure(figsize=(8,8))
x_axis=np.arrange(len(month))
plt.bar(x_axis-0.2,month, temp, color='blue')
plt.bar(x_axis+0.2,month, hum, color='red')
plt.xlabel("months")
plt.ylabel("tempertor and humidity")
plt.title("monthly data of frequncy of temprator and humidity")
plt.show()
