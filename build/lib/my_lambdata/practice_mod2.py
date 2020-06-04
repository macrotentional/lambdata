\\\\\\\\\\\\\\\\\\\\\\\\\
import numpy as np

#df = pd.DataFrame(np.random.rand(100, 100))

#df[df > .9] = pd.np.nan
 
#print("number of null values:", df.isnull().values.sum())

def checkfornulls(df):
    """
    df is a dataframe
    function will return sum of NaN values within the df
    """

    df = pd.DataFrame(df)

    return df.isnull().values.sum())

if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another script

y = df(input("Please choose a number"))
print(y, check(y))

