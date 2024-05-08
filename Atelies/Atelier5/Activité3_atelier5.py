# Activité 3 :
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
Maths= [] 
Physique= [] 

with open('notes_combined.csv','r') as csvfile: 
	plots = csv.reader(csvfile, delimiter = ',') 
	
	for row in plots: 
		Maths.append(row[0]) 
		Physique.append(row[1]) 

plt.plot(Maths, color = 'b', linestyle = 'dotted',label = "line1-dotted")
plt.plot(Physique, color = 'r', linewidth = 2,linestyle = 'dashed',label = "line1-dashed")
plt.xlabel('x-axis') 
plt.ylabel('y-axis') 
plt.title('Plot with two or more lines with different styles') 
plt.legend() 
plt.show() 
