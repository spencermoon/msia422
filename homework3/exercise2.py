
"""
Assignment: Homework 3 - Exercise 2
Name: Spencer Moon
"""

from threading import Thread
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import requests
import time


url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'


# Scraping Boone County site
def scrape(url):
    response = requests.get(url)
    html = response.content.decode('ascii')
    soup = BeautifulSoup(html, 'html.parser')
    
    lastname = [i.string for i in soup.find_all('td', 
                                                attrs={'data-th':'Last Name'})]
    firstname = [i.string for i in soup.find_all('td', 
                                                 attrs={'data-th':'First Name'})]
    age = [i.string for i in soup.find_all('td', attrs={'data-th':'Age'})]
    link = ['https://report.boonecountymo.org/mrcjava/servlet/'
            + i.get('href') for i in soup.find_all('a', attrs={'class':'_lookup btn btn-primary'})]

    return [lastname, firstname, age, link]

rawdata = scrape(url) 


# Using sequential method
chargebail = {}

def detail_sequential(data):
    global chargebail
    start = time.time()
    
    for j in data[3]:
        subresponse = requests.get(j)
        subhtml = subresponse.content.decode('ascii')
        subsoup = BeautifulSoup(subhtml, 'html.parser')
        chargebail.update({j:[[x.string for x in subsoup.find_all('td', attrs={'data-th':'CHARGE DESCRIPTION'})],
                              [x.string.replace('\n','').replace(',','').strip() for x in subsoup.find_all('td', attrs={'data-th':'BAIL'})]]})

    print('Sequential Function Job Time:', time.time() - start, '\n')

detail_sequential(rawdata)


# Using threading method
link = rawdata[3]
chargebail = {}

def detail_threading(link):
    global chargebail
    
    subresponse = requests.get(link)
    subhtml = subresponse.content.decode('ascii')
    subsoup = BeautifulSoup(subhtml, 'html.parser')
    chargebail.update({link:[[x.string for x in subsoup.find_all('td', attrs={'data-th':'CHARGE DESCRIPTION'})],
                             [x.string.replace('\n','').replace(',','').strip() for x in subsoup.find_all('td', attrs={'data-th':'BAIL'})]]})


threadlist = []
start = time.time()

for i in link:
    t = Thread(target = detail_threading, args = (i,))
    t.start()
    threadlist.append(t)

for t in threadlist:
    t.join()

print("Threading Function Job time:", time.time() - start, '\n')


# Combining dataset
def combine(data, detail):
    result = []
    
    for l in range(len(data[0])):
        result += [[data[0][l], data[1][l], data[2][l], 
                    detail[data[3][l]][0], detail[data[3][l]][1]]]
    
    return result

combined = combine(rawdata, chargebail)


# Extracting dataset
def dataextract(raw):
    
    for i in raw:
        totbail = 0
        for j in i[4]:
            if j == '':
                totbail += 0
            else:
                totbail += float(j)
        
        print('Last Name:','\t', i[0])  
        print('First Name: ','\t', i[1])  
        print('Age: ','\t','\t', i[2])  
        print('Total Cases: ','\t', str(len(i[3])))  
        print('Total Bail: ','\t', str(totbail), '\n')  
        
dataextract(combined)    


# Plotting top 10 crime types
crime = [j for i in combined for j in i[3]]
unique = set(crime)
lst = sorted([[i, crime.count(i)] for i in unique], 
               key = lambda x: x[1], reverse = True)
total = sum(lst[j][1] for j in range(len(lst)))

x = range(10)
y = [i[1] for i in lst[:10]]
label = [str(round(i[1]/total*100, 1)) + '%' for i in lst[:10]]

plt.bar(x, y, align = 'center')
plt.xticks(x, [i[0] for i in lst[:10]], rotation = 'vertical')
plt.title('Top 10 Crime Types')
plt.xlabel('Crime')
plt.ylabel('Count')

for a,b,c in zip(x,y,label):
    plt.text(a,b,c, ha = 'center')

plt.show()
    
