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
print(elements_csv)

