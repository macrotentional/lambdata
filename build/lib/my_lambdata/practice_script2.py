import pandas

from my_lambdata.practice_mod2 import checkfornulls

df = [[5, NaN, 9, 4, NaN], [3, 9, 15, NaN, 2]]

print("total number of null values:", checkfornulls(df))