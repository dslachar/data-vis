# David LaCharite

import numpy as np
import pandas as pd
import math

# Part 1
print('-----------------------PART 1-----------------------')
# Read Elements CSV into a pandas data frame
df_elements = pd.read_csv('elements.csv')

# add ninth and tenth elements to dataframe
df_elements.loc[len(df_elements)]=['Fluorine','F', 9]
df_elements.loc[len(df_elements)]=['Neon','Ne', 10]

# add a column with the atomic weights rounded to the nearest inetger
df_elements['atomic_weight'] = ['1','4','7','9','11','12','14','16','19','20']


print(df_elements)

# Part2
print('-----------------------PART 2-----------------------')
# Make a list of strings for nine Greek letters, ‘alpha’, for example.
# Make that list such that they are not in alphabetic order
greekLetters = ['delta','alpha','phi','iota','lambda',
                'gamma','eta','tau','epsilon']
# Make two 9-element numpy arrays of random floating-point numbers with the
# estimated mean 10 and standard deviation 1.5
mu = 10
sigma = 1.5
NPTS = 9
random1 = [sigma * x + mu for x in np.random.randn(NPTS)]
random2 = [sigma * x + mu for x in np.random.randn(NPTS)]
# Make an array of nine elements ranging from zero to two times pi
range_low = 0
range_high = 2*math.pi
angle = np.random.uniform(range_low, range_high, NPTS)
# Make another array holding the cosine of that ‘angle’ array.
cosine = [math.cos(x) for x in angle]

# Construct a dictionary from all of the above
dict = d = {'Letter':greekLetters,
            'Random_1':random1,
            'Random_2':random2,
            'Angle' : angle,
            'Cosine' : cosine}

# Form a DataFrame from that dictionary and print it out
df_letters = pd.DataFrame(dict)
print(df_letters)

# Sort the DataFrame ascending on the Greek letters,
trimmed_df = df_letters.sort_values(by=['Letter'])

# drop two columns of your choice
trimmed_df.drop(['Random_2', 'Cosine'], axis=1, inplace=True)

# drop one of the rows
trimmed_df.drop(trimmed_df[trimmed_df['Letter'] == 'eta'].index, inplace=True)

# and print that out
print(trimmed_df)

# Part 3
print('-----------------------PART 3-----------------------')
# Write a program in Python to create and print out the first twelve Fibonacci numbers
numFibs = 12
fibsList = [0, 1]
while len(fibsList) < numFibs:
    fibsList.append(sum(fibsList[-2:]))

print(fibsList)

# iterate over the last five numbers to build another list with the ratio of each number to its predecessor
numRatios = 5
ratioList = []
for i in range(numFibs - numRatios, numFibs):
    ratioList.append(fibsList[i] / fibsList[i-1])

print(ratioList)

# What do you observe about this latter list?
#The latter list is a convergent sequence with a limit of 1.618 which is  ≈  the Golden Ratio.

# Part 4
print('-----------------------PART 4-----------------------')

# Provide a function that converts temperature in Kelvin to Rankine


def kelvin_to_rankin(K):
    return K * 1.8


# Make a list of five Kelvin temperatures and print out their values in Rankine
kelvinTemps = [0, 223, 283, 333, 373]
print(kelvinTemps)
rankinTemps1 = [kelvin_to_rankin(K) for K in kelvinTemps]
print(rankinTemps1)

# Repeat using a lambda function.
rankinTemps2 = list(map(lambda x: x * 1.8, kelvinTemps))
print(rankinTemps2)







