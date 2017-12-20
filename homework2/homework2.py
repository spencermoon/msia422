
"""
Assignment: Homework 2
Name: Spencer Moon
"""

import matplotlib.pyplot as plt
import random
import timeit
import pandas as pd

# Bubble sort
def bubblesort(iterable, key = None, reverse = False):
    comparison = 0
    swap = 0
    
    def sorting():
        nonlocal comparison
        nonlocal swap
        copy = [x for x in iterable]
        
        if key == None: 
            for num in range(len(copy)-1, 0, -1):
                for i in range(num):
                    comparison += 1
                    if reverse == True:
                        if copy[i] < copy[i+1]:
                            copy[i], copy[i+1] = copy[i+1], copy[i]
                            swap += 1              
                    elif reverse == False:
                        if copy[i] > copy[i+1]:
                            copy[i], copy[i+1] = copy[i+1], copy[i]
                            swap += 1                          
        else: 
            for num in range(len(copy)-1, 0, -1):
                for i in range(num):
                    comparison += 1
                    if reverse == True:
                        if key(copy[i]) < key(copy[i+1]):
                            copy[i], copy[i+1] = copy[i+1], copy[i]
                            swap += 1              
                    elif reverse == False:
                        if key(copy[i]) > key(copy[i+1]):
                            copy[i], copy[i+1] = copy[i+1], copy[i]
                            swap += 1
        
        return copy
    
    # Print statements below will be printed everytime the function is called    
    print('Bubble Sort')    
    print('Timer measure: ', timeit.timeit(lambda: sorting(), number = 1))
    print('Number of comparisons: ', str(comparison))
    print('Number of swaps: ', str(swap))
    return sorting()
        

# Merge sort
def mergesort(iterable, key = None, reverse = False):
    copy = [x for x in iterable]
    comparison = 0
    
    def sorting(copy, key, reverse):    
        nonlocal comparison

        if key == None:
            
            if reverse == True:
                if len(copy) > 1:
                    mid = len(copy) // 2
                    left_half = copy[:mid]
                    right_half = copy[mid:]
                    sorting(left_half, key, reverse)
                    sorting(right_half, key, reverse)
            
                    i = 0
                    j = 0
                    k = 0
                    
                    while i < len(left_half) and j < len(right_half):
                        comparison += 1
                        if left_half[i] > right_half[j]:
                            copy[k] = left_half[i]
                            i += 1
                        else:
                            copy[k] = right_half[j]
                            j += 1
                        k += 1
                    while i < len(left_half):
                        copy[k] = left_half[i]
                        i += 1
                        k += 1
                    while j < len(right_half):
                        copy[k] = right_half[j]
                        j += 1
                        k += 1
            else:            
                if len(copy) > 1:
                    mid = len(copy) // 2
                    left_half = copy[:mid]
                    right_half = copy[mid:]
                    sorting(left_half, key, reverse)
                    sorting(right_half, key, reverse)
            
                    i = 0
                    j = 0
                    k = 0
                    
                    while i < len(left_half) and j < len(right_half):
                        comparison += 1
                        if left_half[i] < right_half[j]:
                            copy[k] = left_half[i]
                            i += 1
                        else:
                            copy[k] = right_half[j]
                            j += 1
                        k += 1
            
                    while i < len(left_half):
                        copy[k] = left_half[i]
                        i += 1
                        k += 1
                    while j < len(right_half):
                        copy[k] = right_half[j]
                        j += 1
                        k += 1
    
        else:
            
            if reverse == True:
                if len(copy) > 1:
                    mid = len(copy) // 2
                    left_half = copy[:mid]
                    right_half = copy[mid:]
                    sorting(left_half, key, reverse)
                    sorting(right_half, key, reverse)
            
                    i = 0
                    j = 0
                    k = 0
                    
                    while i < len(left_half) and j < len(right_half):
                        comparison += 1
                        if key(left_half[i]) > key(right_half[j]):
                            copy[k] = left_half[i]
                            i += 1
                        else:
                            copy[k] = right_half[j]
                            j += 1
                        k += 1
            
                    while i < len(left_half):
                        copy[k] = left_half[i]
                        i += 1
                        k += 1
                    while j < len(right_half):
                        copy[k] = right_half[j]
                        j += 1
                        k += 1
            else:            
                if len(copy) > 1:
                    mid = len(copy) // 2
                    left_half = copy[:mid]
                    right_half = copy[mid:]
                    sorting(left_half, key, reverse)
                    sorting(right_half, key, reverse)
            
                    i = 0
                    j = 0
                    k = 0
                    
                    while i < len(left_half) and j < len(right_half):
                        comparison += 1
                        if left_half[i] < right_half[j]:
                            copy[k] = left_half[i]
                            i += 1
                        else:
                            copy[k] = right_half[j]
                            j += 1
                        k += 1
                    while i < len(left_half):
                        copy[k] = left_half[i]
                        i += 1
                        k += 1
                    while j < len(right_half):
                        copy[k] = right_half[j]
                        j += 1
                        k += 1
                
        return copy
    
    # Print statements below will be printed everytime the function is called 
    print('Merge Sort')
    print('Timer measure: ', 
          timeit.timeit(lambda: sorting(copy, key, reverse), number = 1))
    print('Number of comparisons: ', str(comparison))
    return sorting(copy, key, reverse)


# Random list generator
def randomlist(N):

    nl = [random.randint(-100, 100) for _ in range(0,N)]

    return nl


# Comparison of sorting functions
l = randomlist(15) # This list can be changed to test the sort functions
print('Sorted Function')
print('Timer measure: ', timeit.timeit(lambda: sorted(l), number = 1))
print(sorted(l))
print('\n')
print(bubblesort(l))
print('\n')
print(mergesort(l))
print('\n')
# It's clear that Python's sorted() function runs the fastest


# Plots and summary table
x = [1, 10, 100, 500, 1000]
lsts = [randomlist(i) for i in x]
# Print statements in below functions will be printed before the plot
y1 = [timeit.timeit(lambda: bubblesort(i), number = 1) for i in lsts]
y2 = [timeit.timeit(lambda: mergesort(i), number = 1) for i in lsts]
y3 = [timeit.timeit(lambda: sorted(i), number = 1) for i in lsts]
plt.scatter(x, y1, color = 'r', label = 'Bubble Sort')
plt.scatter(x, y2, color = 'b', label = 'Merge Sort')
plt.scatter(x, y3, color = 'g', label = 'Sorted Function')
plt.legend(loc = 'upper left')
plt.title('Efficiency Comparison for Sorting Functions')
plt.xlabel('Length of Randomly Generated List')
plt.ylabel('Time')
plt.show()

time = [('Bubble Sort', y1[0], y1[1], y1[2], y1[3], y1[4]),
        ('Merge Sort', y2[0], y2[1], y2[2], y2[3], y2[4]),
        ('Sorted Function', y3[0], y3[1], y3[2], y3[3], y3[4])]
label = ['Function', 'N=1', 'N=10', 'N=100', 'N=500', 'N=1000']

def summarytable():   
    global time
    global label
    
    print('\n')
    print('Below is a summary table comparing the efficiency (measured in time)', 
          'of each sort function. N refers to the length of randomly generated lists.',
          '\n')
    df = pd.DataFrame.from_records(time, columns = label)
    return df

print(summarytable())