# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
#Code starts here 
data['Gender'].replace('-','Agender',inplace=True)
gender_count = data['Gender'].value_counts() 
gender_count.plot(kind='bar')
plt.show


# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
alignment.plot(kind='pie')
plt.title('Character Aligment')
plt.show()


# --------------
#Code starts here
sc_df = data[['Strength','Combat']].copy()
sc_covariance = sc_df.cov().iloc[0,1]
sc_strength = sc_df['Strength'].std()
sc_combat = sc_df['Combat'].std()
sc_pearson = sc_covariance/(sc_combat*sc_strength)
ic_df = data[['Intelligence','Combat']].copy()
ic_covariance = ic_df.cov().iloc[0,1]
ic_intelligence = ic_df['Intelligence'].std()
ic_combat = ic_df['Combat'].std()
ic_pearson = ic_covariance/(ic_combat*ic_intelligence)



# --------------
#Code starts here
total_high = data.Total.quantile(.99)
super_best = data[data['Total']>total_high]
super_best_names = []
super_best_names = list(super_best['Name'])

print(super_best_names)



# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(3,1, figsize=(20,10))
ax_1.boxplot(super_best['Intelligence'])
ax_2.boxplot(super_best['Speed'])
ax_3.boxplot(super_best['Power'])
plt.show()


