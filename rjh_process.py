#!/bin/evn python
#codign=utf8

import sys
import pandas as pd
import numpy as np
import sklearn as sl
import scipy.stats as ss
import logging
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn import preprocessing


class RJH():
    
    def __init__(self, table):
        """
        init prams
        """
        self.__htArray = table

        self.__table = self.preprocess()

        self.name = "hetong rijihua"


    def getWholeTable(self):

        """fetch the whole table!"""

        return self.__htArray


    def getTable(self):
        
        """fetch the preprocessed table"""
        
        return self.__table

    

    def getColume(self, columnName=None, columnNumber=None):

        """fetch one column of the table either by Name for ny column index""" 

        data = getTable()
        
        if columnName and columnNumber:

            print "Only one prameter needed!!!"

            raise ValueError

        elif columnName:

            return data[columnName]

        elif columnNumber:

            return data[:,columnNumber]

        else:
            
            print "You should give either the columnName or the columnNumber!!!"
            raise IOError
        
        


    def processWithNull(self):
        
        data = getTable()

        inputs = preprocessing.Imputer(missing_values='NaN', strategy='mean', axis=0)

        new_data = inputs.fit(data)
        
        return new_data
        

    def preprocess(self):
        
        data = self.getWholeTable()

        data["month"] = pd.Series(["0"+x if int(x)<10 else x for x in data["month"]])

        data["day"] = pd.Series(["0"+x if int(x)<10 else x for x in data["day"]])

        data["time"] = data["year"] + data["month"] + data["day"]

        return data
        

    def getMean(self, arr, weights=None):

        if not weights:
            
            return arr.sum()/len(arr)
        
        else:

            return np.mean(arr, weights) 

    def getMeanByDay(self, date=None):
        
        data = getTable()

        if date:

            dayData = data.values[data.values[:,5] == date]

        else:

            print "you should specify a datetime that you concern!!!"
            raise IOError

        pass

    def getMeanByCompany(self, companyName=None, companyId=None):
        
        pass

    def getMedianByDay(self, arr, date=None):
        
        pass 
    
    def getMedian(self, MedianPoint=5):

        pass

    def getVariance(self):

        pass

    def predict(self):

        pass
       
def main():

    ######get the filename######
    filename = sys.argv[1]
    #print filename
    
    ###################################################################################
    ######read file into dataFrame#######
    data = pd.read_csv(filename, sep='\t', 
                        header=0, dtype={"year":str, "month":str, "day":str})
    #print(data)

    ##################################################################################
    ######Function Test######
    ######preprocess######
    rjh = RJH(data)
    print rjh.name
    rjh.preprocess()


if __name__ == "__main__":
    main()
    
