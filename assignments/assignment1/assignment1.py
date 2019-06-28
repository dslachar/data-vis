import numpy as np
import pandas as pd

#Part 1
#Read Elements CSV into a pandas data frame
elements_csv = pd.read_csv('elements.csv')

# add ninth and tenth elements to dataframe
elements_csv.loc[len(elements_csv)]=['Fluorine','F', 9]
elements_csv.loc[len(elements_csv)]=['Neon','Ne', 10]

# add a column with the atomic weights rounded to the nearest inetger
elements_csv['atomic_weight'] = ['1','4','7','9','11','12','14','16','19','20']
print('------PART 1------')
print(elements_csv)

#Part2
#Make a list of strings for nine Greek letters, ‘alpha’, for example.
#Make that list such that they are not in alphabetic order
greekLetters = ['delta','alpha','phi','iota','lambda','gamma','eta','tau','epsilon']
#Make two 9-element numpy arrays of random floating-point numbers with the
#estimated mean 10 and standard deviation 1.5
mu = 10
sd = 1.5
random1 = [x * sd + mu for x in np.random.randn(9)]
print(random1)
random2 = [x * sd + mu for x in np.random.randn(9)]
print(random2)


