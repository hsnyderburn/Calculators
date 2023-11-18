# -*- coding: utf-8 -*-
"""
Spyder Editor

Made by Hannah Snyderburn 

AeroCalcs

Goal: Produce a way of inputting altitude and receiving 
output data, linear regressed, to be used to find Mach no.

Output Data will include:
    Density
    Viscosity
    Temperature
"""

import numpy as np
import pandas
import matplotlib.pyplot as plt
import pandas

densTable = pandas.read_csv('C:/Users/Bohob/Documents/gitClones/Calculators/Tables/AltDensTable.csv')
print(densTable.dtypes)
#
#df['column_name'] = df['column_name'].astype(float)

altx = densTable['Altitude (meters)'] = densTable['Altitude (meters)'].astype(float)
densy = densTable['Density (kg/m3)'] = densTable['Density (kg/m3)'].astype(float)


plt.plot(altx, densy)
plt.show()

#alt = #altitude
#vel = 118 #mph #freestream velocity
#c = np.sqrt(gam*R*T)#speedOfSoundInMedium

#Mach = vel/np.sqrt()