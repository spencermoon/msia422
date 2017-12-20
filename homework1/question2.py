
"""
Assignment: Homework 1 - Question 2
Name: Spencer Moon
"""

import statistics as s
import matplotlib.pyplot as plt

#Question 2

#Loading raw data
def readdata(path='exams.csv'):
    
    with open(path,'r') as f:
        raw = f.readlines()
        studentid = [i.split(',')[0] for i in raw[1:]]
        name = [i.split(',')[1] for i in raw[1:]]
        quiz = [int(i.split(',')[2]) for i in raw[1:]]
        project = [int(i.split(',')[3]) for i in raw[1:]]
        exam = [int(j.replace('\n','')) 
                    for j in [i.split(',')[4] 
                    for i in raw[1:]]]
        finalscore = list(map(lambda x, y, z: 
                              round(.4*x + .3*y + .3*z, 1), 
                              exam, project, quiz))
        finalgrade = []
        
        for i in finalscore:
            if i >= 90:
                finalgrade += 'A'
            elif i >= 80:
                finalgrade += 'B'
            elif i >= 20:
                finalgrade += 'C'
            elif i >= 10:
                finalgrade += 'D'
            else:
                finalgrade += 'F'
        
    return [studentid, name, quiz, project, exam, finalscore, finalgrade]

rawdata = readdata()


#Creating a nested dictionary
def dictnested(data):
    
    d = {}
    
    for i in range(len(data[0])):      
        d.update({data[0][i]:{'Name': data[1][i], 
#                              'Quiz Score': data[2][i], 
#                              'Project Score': data[3][i], 
#                              'Exam Score': data[4][i], 
                              'Final Score': data[5][i], 
                              'Final Grade': data[6][i]}})
        
    return d    

dictionary = dictnested(rawdata)

#Creating a console-based menu
print('========================================================', '\n')
print('Menu', '\n')
print('Please load the data first before selecting options 2 through 7', '\n')
print('1', ' ', 'Load student dataset')
print('2', ' ', 'View student names, final scores, and letter grades')
print('3', ' ', 'View score summary')
print('4', ' ', 'View values larger than mean and two times SD')
print('5', ' ', 'View pie chart of final letter distribution')
print('6', ' ', 'View box plot parameters')
print('7', ' ', 'Exit', '\n')
print('========================================================', '\n')

menu = input('ENTER MENU NUMBER: ')

while True:
    try:
        if menu == '1':
            dictionary = dictnested(readdata())
            print('Dataset loaded.')
            menu = input('ENTER MENU NUMBER: ')
        elif menu == '2': 
            summary = list(list(i.values()) for i in dictionary.values())
            summary.sort()
            
            for i in summary:
                print('Name: {} \t Final Score: {} \t Final Grade: {}'
                      .format(i[0],i[1],i[2]))
                
            menu = input('ENTER MENU NUMBER: ')
        elif menu == '3':
            print('Student Count: ', str(len(rawdata[0])))
            print('Min Score: ', str(min(rawdata[5])))
            print('Max Score: ', str(max(rawdata[5])))
            print('Mean Score: ' , str(round(s.mean(rawdata[5]), 1)))
            print('Mode Grade: ' , str(s.mode(rawdata[6])))
            print('Standard Deviation: ', str(round(s.stdev(rawdata[5]), 1)))
            menu = input('ENTER MENU NUMBER: ')
        elif menu == '4':
            summary = list(list(i.values()) for i in dictionary.values())
            summary.sort()
            print('Students with final score greater than the mean:', '\n')
            
            for i in summary:
                if i[1] > s.mean(rawdata[5]):
                    print('Name: {} \t Final Score: {} \t Final Grade: {}'
                      .format(i[0], i[1], i[2]))
            
            print('\n')
            print('Students with final score of 2 SDs above the mean:',
                  '\n')
            
            for i in summary:
                if i[1] > s.mean(rawdata[5]) + 2*s.stdev(rawdata[5]):
                    print('Name: {} \t Final Score: {} \t Final Grade: {}'
                      .format(i[0], i[1], i[2]))
            
            menu = input('ENTER MENU NUMBER: ')
        elif menu == '5':
            labels = 'A', 'B', 'C', 'D', 'F'
            sizes = [sum(i == 'A' for i in rawdata[6]),
                     sum(i == 'B' for i in rawdata[6]),
                     sum(i == 'C' for i in rawdata[6]),
                     sum(i == 'D' for i in rawdata[6]),
                     sum(i == 'F' for i in rawdata[6])]   
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
            ax1.axis('equal')
            plt.title('Letter Grade Distribution')
            plt.show()
            menu = input('ENTER MENU NUMBER: ')
        elif menu == '6':
            print('Min Score: ', str(min(rawdata[5])))
            print('Max Score: ', str(max(rawdata[5]))) 
            print('Median Score: ' , str(round(s.median(rawdata[5]), 1)))
            
            if (len(rawdata[5])/2)%2 == 0:
                q1 = s.mean([sorted(rawdata[5])[round(len(rawdata[5])/4)],
                            sorted(rawdata[5])[round(len(rawdata[5])/4 - 1)]])
                q3 = s.mean([sorted(rawdata[5])[round(len(rawdata[5])*3/4)],
                            sorted(rawdata[5])[round(len(rawdata[5])*3/4 - 1)]])
            
            print('Lower Quartile (Q1): ', str(round(q1, 1)))
            print('Upper Quartile (Q3): ', str(round(q3, 1)))
            menu = input('ENTER MENU NUMBER: ')
        elif menu == '7':
            break
        else:
            print('That is not a valid number. Refer to the menu above.')
            menu = input('ENTER MENU NUMBER: ')
    except NameError:
        print('Please load the data first.')
        menu = input('ENTER MENU NUMBER: ')