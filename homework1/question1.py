
"""
Assignment: Homework 1 - Question 1
Name: Spencer Moon
"""

import matplotlib.pyplot as plt
import timeit
import random

#Question 1

#1) Creating a list of N random numbers and words
def randomlist(N):
    
    words = ['python', 'word', 'programming', 
             'language', 'java', 'apple', 'banana']

    nl = [random.randint(-100, 100) for _ in range(0,random.randint(0,N))]
    nllen = len(nl)    
    wl = [random.choice(words) for _ in range(0,N - nllen)]
    wnl = nl + wl
    random.shuffle(wnl)
    
    return wnl


l = randomlist(int(input('Specify N (enter a number): '))) # Please specify N
print('\n')

#2) Procedurial programming
def numwordproc(ls):
    
    countnum = 0
    countword = 0
    
    for i in ls:
        if type(i) == int:
            countnum += 1
        else:
            countword += 1
    
    print('PROCEDURAL PROGRAMMING OUTPUT')        
    print('Count of numbers: ' + str(countnum))
    print('Count of words: ' + str(countword))
    print('\n')

numwordproc(l)


#2) Functional programming
def numwordfunc(ls):
    
    output = [sum(type(i) == int for i in ls), 
              sum(type(i) == str for i in ls)]
    
    print('FUNCTIONAL PROGRAMMING OUTPUT')   
    print('Count of numbers: ' + str(output[0]))
    print('Count of words: ' + str(output[1]))
    print('\n')                                 
    
numwordfunc(l)


#3) Timing and plotting both procedural and functional codes
x = [100, 1000, 10000, 100000]
lsts = [randomlist(i) for i in x]
y1 = [timeit.timeit(lambda: numwordproc(i), number = 1) for i in lsts]
y2 = [timeit.timeit(lambda: numwordfunc(i), number = 1) for i in lsts]
plt.xscale('log')
plt.scatter(x, y1, color='r', label='Procedural Programming')
plt.scatter(x, y2, color='b', label='Functional Programming')
plt.legend(loc='upper left')
plt.show()