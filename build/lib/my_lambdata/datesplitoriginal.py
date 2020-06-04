import pandas as pd

def datesplit(holidays):
  """param date is a date column formatted as MM/DD/YYYY
  function will convert to datetime format, then split date column into three additional columns for month, day, year
  """

#s = pd.Series(['11/27/1993', '5/20/2009', '2/11/1843', '6/2/2020', '1/31/1940'])
  data = {'2020 holidays': ['Memorial Day', 'Independence Day', 'Labor Day', 'Halloween', 'Thanksgiving'],
          'date': ['5/24/2020', '7/4/2020', '9/7/2020', '10/31/2020', '11/26/2020']}
  
  holidays = pd.DataFrame(data, columns = ['2020 holidays', 'date'])

  new_df = holidays.copy()

  new_df['date'] = pd.to_datetime(new_df['date'])

  new_df['month'] = new_df['date'].dt.month
  new_df['day'] = new_df['date'].dt.day
  new_df['year'] = new_df['date'].dt.year
 
  return holidays
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another script