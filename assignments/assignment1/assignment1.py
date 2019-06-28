import numpy as np
import pandas as pd
import math

#Part 1
#Read Elements CSV into a pandas data frame
df_elements = pd.read_csv('elements.csv')

# add ninth and tenth elements to dataframe
df_elements.loc[len(df_elements)]=['Fluorine','F', 9]
df_elements.loc[len(df_elements)]=['Neon','Ne', 10]

# add a column with the atomic weights rounded to the nearest inetger
df_elements['atomic_weight'] = ['1','4','7','9','11','12','14','16','19','20']

#print('-----------------------PART 1-----------------------')
#print(df_elements)

#Part2
#Make a list of strings for nine Greek letters, ‘alpha’, for example.
#Make that list such that they are not in alphabetic order
greekLetters = ['delta','alpha','phi','iota','lambda',
                'gamma','eta','tau','epsilon']
#Make two 9-element numpy arrays of random floating-point numbers with the
#estimated mean 10 and standard deviation 1.5
mu = 10
sigma = 1.5
NPTS = 9
random1 = [sigma * x + mu for x in np.random.randn(NPTS)]
random2 = [sigma * x + mu for x in np.random.randn(NPTS)]
#Make an array of nine elements ranging from zero to two times pi
range_low = 0
range_high = 2*math.pi
angle = np.random.uniform(range_low, range_high, NPTS)
# Make another array holding the cosine of that ‘angle’ array.
cosine = [math.cos(x) for x in angle]

#  Construct a dictionary from all of the above
dict = d = {'Letter':greekLetters,
            'Random_1':random1,
            'Random_2':random2,
            'Angle' : angle,
            'Cosine' : cosine}

#Form a DataFrame from that dictionary and print it out
df_letters = pd.DataFrame(dict)
print(df_letters)

#Sort the DataFrame ascending on the Greek letters, drop two columns of your
#choice, drop one of the rows, and print that out
sorted_df = 




