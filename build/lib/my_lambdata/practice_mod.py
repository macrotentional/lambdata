import pandas as pd

class Holiday():
    def __init__(self, name, date, day, month, day):
        self.holiday
        self.date
        self.day
        self.month
        self.year

    @property
    def holiday_date(self):
            return f"{holiday.name} {holiday.date}"

    def advertise(self):
        print("BE READY FOR", self.name.upper(), "AND BUY BEFORE" self.date.upper())
    
 if __name__ == "__main__":

     holidays = [
         {"name": 'Memorial Day', "date": '5/24/2020'}
         {"name": 'Independence Day', "date": '7/4/2020'}
         {"name": 'Labor Day', "date": '9/7/2020'}
         {"name": 'Halloween', "date": '10/31/2020'}
         {"name": 'Thanksgiving', "date": '11/26/2020'}
     ]

for d in holidays:
    holiday = Holiday(d["name"], d["date"])
    #print(holiday.date)
    #print(holiday.holiday_date)
    holiday.advertise()