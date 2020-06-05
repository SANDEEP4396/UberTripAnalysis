import pandas as pd
import seaborn as sea
import matplotlib.pyplot as mat

'''This will load the csv file into the memory '''
uberTripData = pd.read_csv('uber-raw-data.csv')

# Converting the Date/Time value to Timestamp using pandas functions
uberTripData['Date/Time'] = uberTripData['Date/Time'].map(pd.to_datetime)


# These Functions are used to get the Day, Weekday, and Hour separately

def get_dateofmonth(dt):
    return dt.day


def get_weekday(dt):
    return dt.weekday()


def get_hour(dt):
    return dt.hour


uberTripData['DayofMonth'] = uberTripData['Date/Time'].map(get_dateofmonth)
uberTripData['Weekday'] = uberTripData['Date/Time'].map(get_weekday)
uberTripData['Hour'] = uberTripData['Date/Time'].map(get_hour)
print(uberTripData.tail())

# Analyse the Day of the Month
mat.hist(uberTripData.DayofMonth, bins=30, rwidth=0.8, range=(0.5, 30.5), color='orange', alpha=.7)
mat.xlabel('Day of the Month')
mat.ylabel('Frequency')
mat.title('Frequency by Day of Month')
mat.show()  # Represents the frequency of days using Bar graph


# Function to count occurrence of that particular day so that we can sort the days in ascending or descending order


def count_days(days):
    return len(days)


by_days = uberTripData.groupby('DayofMonth').apply(count_days)
sorted_days = by_days.sort_values()
mat.bar(range(1, 31), sorted_days)
mat.xticks(range(1, 31), sorted_days.index)
mat.xlabel('Day of the Month')
mat.ylabel('Frequency')
mat.title('Frequency by Day of Month in increasing order')
mat.show()

# Analyse the Frequency taken by passengers of Cabs at particular hour
mat.hist(uberTripData.Hour, bins=24, range=(1, 24), rwidth=1, color='red', alpha=.6)
mat.xlabel('Hour')
mat.ylabel('Number of cabs')
mat.title('Number of cabs taken in that particular hour')
mat.show()

# Analyse the Frequency of Cabs taken by passengers at a particular weekday
mat.hist(uberTripData.Weekday, bins=7, range=(-.5, 6.5), rwidth=.8, color='green', alpha=.4)
mat.xticks(range(7), 'Mon,Tue,Wed,Thur,Fri,Sat,Sun'.split(','))
mat.xlabel('Weekday')
mat.ylabel('Number of cabs')
mat.title('Number of cabs taken in that particular Weekday')
mat.show()
print()

# Creating a table by combining Weekday Data and Hourly Data
table_by_weekday_hour = uberTripData.groupby('Weekday Hour'.split()).apply(count_days).unstack()
print(table_by_weekday_hour)

# Using Heat Map for the above table
sea.heatmap(table_by_weekday_hour, cmap="YlGnBu")
mat.title('Number of cabs taken in that Weekday in that particular Hour')
mat.show()

# Analysing Longitude and Latitude
mat.hist(uberTripData['Lon'], bins=100, range=(-74.1, -73.9), color='g', alpha=.5, label='Longitude')
mat.legend(loc='upper left')
mat.twiny()
mat.hist(uberTripData['Lat'], bins=100, range=(40.5, 41), color='b', alpha=.5, label='Latitude')
mat.legend(loc='best')
mat.title('Analysing Longitude and Latitude')
mat.xlabel('Latitude')
mat.show()
