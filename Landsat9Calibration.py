# Author:        Gabriel Peters            
# Version:       0.1.3 (8/10/2022)      
# Affiliation:   CIS, Rochester Institute of Technology

import matplotlib.pyplot as plt
from google.colab import drive
import os
import numpy as np

# mounting drive
drive.mount('/content/drive', force_remount=True)

# changing the directory to the file location
os.chdir('/content/drive/MyDrive/TidBitData')

# installing table tool (separate)
pip install tabulate

from tabulate import tabulate

table = [['TidBit', 'Date', 'Tidbit_SurfTemp (C)', 'Satellite_SurfTemp (C)'], 
         ['#3513', '7/11', 24.354, 25.002], 
         ['#1148', '7/11', 27.561, 26.779], 
         ['#3515', '7/11', 25.587, 25.135], 
         ['#5967', '7/11', 25.685, 25.614], 
         ['#5977', '7/11', 25.655, 25.446],          
         ['#3513', '7/2', 23.496, 24.533], 
         ['#1148', '7/2', 23.550, 26.031],
         ['#3515', '7/2', 23.131, 24.328],
         ['#5967', '7/2', 23.390, 25.118],
         ['#5977', '7/2', 23.475, 24.821]]
         
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

# x values
TidBits = ['#3513', '#1148', '#3515', '#5967', '#5977']

# y values - tidbit
TidTemp11 = [24.354, 27.561, 25.587, 25.685, 25.655]
TidTemp2 = [23.496, 23.55, 23.131, 23.39, 23.475]

# y values - satellite
SatTemp11 = [25.002, 26.779, 25.135, 25.614, 25.446]
SatTemp2 = [24.533, 26.031, 24.328, 25.118, 24.821]

colors1 = np.array(["blue","blue","blue","blue","blue"])
colors2 = np.array(["cyan","cyan","cyan","cyan","cyan"])
colors3 = np.array(["red","red","red","red","red"])
colors4 = np.array(["pink","pink","pink","pink","pink"])

plt.scatter(TidBits, TidTemp11, lineWidth = 1, c=colors1, label='TidBit 7/11')
plt.scatter(TidBits, SatTemp11, lineWidth = 1, c=colors2, label='Landsat9 7/11')
plt.scatter(TidBits, TidTemp2, lineWidth = 1, c=colors3, label='TidBit 7/2')
plt.scatter(TidBits, SatTemp2, lineWidth = 1, c=colors4, label='Landsat9 7/2')
plt.ylabel('Temperature (C)')
plt.xlabel('Tidbit')
plt.ylim(22.5, 28.5)
plt.legend(loc="upper right")
plt.title('Surface Temp Comparision Between Tidbits and Landsat 9')

#data_dir = '/content/drive/MyDrive/TidBitData'
#plt.savefig(f"{data_dir}/ST.jpg")
#print(f"Plot saved at {data_dir}")
