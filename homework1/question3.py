
"""
Assignment: Homework 1 - Question 3
Name: Spencer Moon
"""


"""
The library "wordsegment" can be mainly used to divide a phrase without spaces
back into its constituent parts. For example, consider a phrase like "itisus."
Althuogh this is easy for humans to parse, it requires some work for a machine
to parse. Function segment() can be used to parse out this phrase. The result 
is a list with each element being a word in the phrase. Every word and phrase
is lowercased with punctuations removed. This library relies on datasets that
include 330,000 most common words and 250,000 most common phrases. 
"""


#Example

#1) First install the library by running the following command

# pip install wordsegment

#2) Import the library and the following functions

from wordsegment import load, segment
load() #This function loads the datasets with common words and phrases

#3) Use the segment 

phrase = 'Spenceristhebest!'
print(segment(phrase)) #output: ['spencer', 'is', 'the', 'best']


"""
As seen above, this library can be particularly helpful when you are cleansing
data and a field includes concatenated strings. Using this library, there is no
need to specifiy how the strings need to be segmented.
"""