
"""
Assignment: Homework 3 - Exercise 1
Name: Spencer Moon
"""

import matplotlib.pyplot as plt
import requests

# Pulling data from the web API
zipcode = ['60606', '94102', '10001', '75201', '20036'] # CHI, SF, NYC, DAL, DC
daterange = [20170901, 20170930] # [Begin Date, End Date]
key = '4f4aa9a49372300e' # This is my key


def temp(zipcode, daterange, key):
    fulldata = {}
    
    for i in zipcode:
        dailydata = {}
        
        for j in range(daterange[0], daterange[1] + 1):
            response = requests.get('http://api.wunderground.com/api/' + key 
                                    + '/history_' + str(j) + '/q/' + i + '.json')
            raw = response.json()
            dailydata.update({j:int(raw['history']['dailysummary'][0]['meantempi'])})
    
        fulldata.update({i:dailydata})
    
    return fulldata


# Please note that running this function without threading will take some time
monthlydata = temp(zipcode, daterange, key)


# Creating a data summary table
def summary(data):
    global zipcode
    global daterange
    
    for i in zipcode:
        temp = [data[i][j] for j in range(daterange[0], daterange[1] + 1)]
        print('Summary statistics for : ', '\t', i)
        print('Minimum temperature: ','\t', '\t', str(min(temp)), ' F')
        print('Maximum temperature: ','\t', '\t', str(max(temp)), ' F')
        print('Mean temperature: ','\t', '\t', str(round(sum(temp)/len(temp))), ' F', '\n')

summary(monthlydata)


# Plotting temperture trend for five locations
x = [j for j in range(daterange[0], daterange[1] + 1)]
y1 = [monthlydata[zipcode[0]][j] for j in range(daterange[0], daterange[1] + 1)]
y2 = [monthlydata[zipcode[1]][j] for j in range(daterange[0], daterange[1] + 1)]
y3 = [monthlydata[zipcode[2]][j] for j in range(daterange[0], daterange[1] + 1)]
y4 = [monthlydata[zipcode[3]][j] for j in range(daterange[0], daterange[1] + 1)]
y5 = [monthlydata[zipcode[4]][j] for j in range(daterange[0], daterange[1] + 1)]
plt.plot(x, y1, label = 'Chicago')
plt.plot(x, y2, label = 'San Francisco')
plt.plot(x, y3, label = 'New York')
plt.plot(x, y4, label = 'Dallas')
plt.plot(x, y5, label = 'Washington DC')
plt.legend(loc = 'lower left')
plt.title('Temperature Trend for September 2017')
plt.xlabel('Day')
plt.ylabel('Temperature (F)')
plt.ylim(0, 100)
plt.show()