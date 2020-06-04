


from pandas import DataFrame


# TODO helper function from assignment
# State abbreviation -> Full Name and visa versa. 
# FL -> Florida, etc. (Handle Washington DC and territories like Puerto Rico etc.)

def add_state_names_colum(my_df):
    """
    Add a column of corresponding state names to a dataframe.

    Params (my_df) a DataFrame with a column called "abbrev" that has state abbreviations

    Return a copy of the original dataframe, with an extra column.
    """
    # TODO: 

    new_df = my_df.copy()

    names_map = {"CA": "Cali", "CO": "Colo", "CT": "Conn"}

    new_df["name"] = new_df["abbrev"].map(names_map)

    breakpoint()

    return new_df 

if __name__ == '__main__':
    df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(df.head())
    add_state_names_colum(df)
    print(df.head())

    mapped_df = add_state_names_column(df)
    print(mapped_df.head())

    df2 = DataFrame({"other_col":[1,2,3]})
    df2.head()

    breakpoint()

