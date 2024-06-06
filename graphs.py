#import matplotlib.pyplot as plt
# import csv

#Bar chart  
# x = []
# y = []
  
# with open('Data.csv','r') as csvfile:
#     plots = csv.reader(csvfile, delimiter = ',')
      
#     for row in plots:
#         x.append(row[4])
#         y.append(int(row[5]))
        
# plt.bar(x, y, color = 'g', width = 0.72, label = "Respondents #")
# plt.xlabel('Number of Partners')
# plt.ylabel('Number of Respondents')
# plt.title('Number of sexual partners by respondents')
# plt.legend()
# plt.show()

#Heat Map
#https://medium.com/@rokaandy/python-data-visualization-heatmaps-79fa7506c410

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Project Questionsfemale.csv')
#print(data.head(5))

fig, ax = plt.subplots(figsize=(12,8))
sns.heatmap(data.corr(), center=0, cmap='Blues')
ax.set_title('Data on Females')

fig, ax = plt.subplots(figsize=(12,8))
sns.heatmap(data.corr(), center=0, cmap='BrBG', annot=True)