import csv
import os
import datetime

class filehandler:

    def __init__(self, filename):
        self.filename = filename

    def getData(self, csv_reader, kwargs):
        data = []
        index = {}
        date_key = None
        date_index = None

        header = next(csv_reader)

        for val, key in kwargs.items():
            index[val] = header.index(key)

        # Find the index of the date in the list
        if 'date' in kwargs.values():
            date_index = 3

        for row in csv_reader:
            # Convert the date string to a datetime object
            if 'date' in kwargs.values():
                row[date_index] = datetime.datetime.strptime(row[date_index], "%Y-%m-%d")
            data.append({key: row[index[key]] for key in kwargs.keys()})

        return data

    def readfile(self,**kwargs):
        with open(self.filename, newline='') as csvfile:
        # Create a CSV reader object
            csv_reader = csv.reader(csvfile)
            data = self.getData(csv_reader,kwargs)

        return data

def question1():
    primaryschool = '/home/myproject/chart/assets/schools.csv'
    file = filehandler(primaryschool)
    data = file.readfile(district_name='district_name',category='cat',language='moi',school_name='name')
    return data

def question2():
    matches = '/home/myproject/chart/assets/matches.csv'
    file = filehandler(matches)
    data = file.readfile(season='season',winner='winner',date='date')
    return data

