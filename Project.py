#Programmers Yessenia Bledsode-Becarra and Kayla Johnson
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Heat map program
HM = pd.read_csv('riskybehaviors.csv')

fig, ax = plt.subplots(figsize=(12,8))
sns.heatmap(HM.corr(), center=0, cmap='Blues', annot=True)
ax.set_title('Risky behavior in teens')

#Table program
data = pd.read_csv('ProjectQuestions.csv')
data.head()
df = data['q62'].value_counts()
print(df)

#Pie chart program
df = pd.read_csv ('Alcohol use vs sex partners.csv')

#add colors
Colors = ['#003c30','#aee0d8']

sums = df.groupby(df["Females with 6 sex partners"])["1"].sum()
plt.title('Project Questionsfemales6sexpart')
plt.axis('equal')
plt.pie(sums, labels=sums.index, autopct='%1.1f%%', colors=Colors);
plt.show()



#Source on the Heatmap:
#https://medium.com/@rokaandy/python-data-visualization-heatmaps-79fa7506c410
#Source on the data compiling program:
#https://docs.python.org/3/library/csv.html
