import pandas as pd
df=pd.read_csv('lois_continuous.csv')
#print(df.head())
swale_data=df[df['Unnamed: 2']=='Swale at Catterick Bridge']
#print(swale_data)
print(df.columns)
swale_data.loc[:, 'Temperature water continuous']=pd.to_numeric(swale_data['Temperature water continuous'], errors='coerce')
swale_data.loc[:, 'Oxygen dissolved continuous']=pd.to_numeric(swale_data['Oxygen dissolved continuous'], errors='coerce')
mean_temperature=swale_data['Temperature water continuous'].mean()
median_dissolved_oxygen=swale_data['Oxygen dissolved continuous'].mean()
print(mean_temperature)
print(median_dissolved_oxygen) 
import matplotlib.pyplot as plt
plt.hist(swale_data['Temperature water continuous'], bins=30, edgecolor='black')
plt.title('Temperature distribution graph')
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.show()