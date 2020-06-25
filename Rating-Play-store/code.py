# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Code starts here
data = pd.read_csv(path)
data['Rating'].plot(kind='hist')

plt.show()


#Subsetting the dataframe based on `Rating` column
data=data[data['Rating']<=5]

#Plotting histogram of Rating
data['Rating'].plot(kind='hist')   

#Code ends here


# --------------
# code starts here

total_null = data.isnull().sum()
print(total_null)

percent_null = total_null / (data.isnull().count()) 
print(percent_null)

missing_data = pd.concat([total_null, percent_null], keys = ['Total', 'Percent'], axis =1)
print(missing_data)

data =data.dropna()

total_null_1 = data.isnull().sum()
print(total_null_1)

percent_null_1 = total_null_1 / (data.isnull().count()) 
print(percent_null)

missing_data_1 = pd.concat([total_null_1, percent_null_1], keys = ['Total', 'Percent'], axis =1)
print(missing_data_1)
# code ends here


# --------------

#Code starts here

plot = sns.catplot(x='Category', y='Rating', data = data, kind = 'box', height = 10)
plot.set_xticklabels(rotation = 90)
plot.set_titles('Rating vs category [Boxplot]')

plt.plot()
#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
print(data['Installs'].value_counts())

data['Installs']=data['Installs'].str.replace('+','')
data['Installs']=data['Installs'].str.replace(',','')
data['Installs'] = data['Installs'].astype(int)

print(data['Installs'].value_counts())

le = LabelEncoder()

data['Installs'] = le.fit_transform(data['Installs'])

plot2 = sns.regplot(x = 'Installs', y = 'Rating', data = data)
plot2.title.set_text('Rating vs Installs [RegPlot]')

plot2.plot()
#Code ends here



# --------------
#Code starts here

print(data['Price'].value_counts())

data['Price']=data['Price'].str.replace('$','')
data['Price'] = data['Price'].astype(float)

print(data['Price'].value_counts())

plot2 = sns.regplot(x = 'Price', y = 'Rating', data = data)
plot2.title.set_text('Price vs Installs [RegPlot]')

plot2.plot()

#Code ends here


# --------------

#Code starts here

print(data['Genres'].unique)

data['Genres'] = data['Genres'].str.split(';').str.get(0)

print(data['Genres'].unique)

gr_mean = data[['Genres', 'Rating']].groupby(['Genres'], as_index=False).mean()

print(gr_mean.describe())

gr_mean = gr_mean.sort_values(by = ['Rating'])

print(gr_mean.iloc[0])
print(gr_mean.iloc[-1])
#Code ends here


# --------------

#Code starts here
print(data['Last Updated'])

data['Last Updated'] =pd.to_datetime(data['Last Updated'])

print(data['Last Updated'])

max_date = max(data['Last Updated'])
print(max_date)
data['Last Updated Days'] = (max_date - data['Last Updated']).dt.days
#Code ends here


