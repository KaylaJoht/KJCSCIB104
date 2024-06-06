#Programmers Yessenia Bledsode-Becarra and Kayla Johnson
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Pie chart program
df = pd.read_csv ('Alcohol use vs sex partners.csv')

#add colors
Colors = ['#bd0000','#bdb400']

sums = df.groupby(df["Males with 1 sex partners"])["12"].sum()
plt.title('Project Questionsmales1sexpart')
plt.axis('equal')
plt.pie(sums, labels=sums.index, autopct='%1.1f%%', colors=Colors);
plt.show()

#Heat map program

HM = pd.read_csv('Risk.csv')

fig, ax = plt.subplots(figsize=(12,8))
sns.heatmap(HM.corr(), center=0, cmap='Blues', annot=True)
ax.set_title('Risky behavior in teens')

#Data compiling program
data = pd.read_csv('ProjectQuestions.csv')
data.head()
df = data['q62'].value_counts()
print(df)


#Source on the Heatmap:
#https://medium.com/@rokaandy/python-data-visualization-heatmaps-79fa7506c410
#Source on the data compiling program:
#https://docs.python.org/3/library/csv.html
