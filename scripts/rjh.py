#!/bin/env python 
#coding = utf8

import sys
import pandas as pd
import numpy as np
import sklearn as sl
import scipy.stats as ss
import collections
import logging
import matplotlib.pyplot as plt
from datetime import datetime
from basic_model import Basic

class Rjhb(Basic):

    def __init__(self, table):
        """
        paras:
            table: numpy array or DataFrame that contains info of rijihuabiao;       
        """
        super(Rjhb, self).__init__(table)
        self.preprocess()
        self.__groupByCompany = None
        self.groupByCo()

    
  # def getTable(self):
  #      """
  #      fetch whole content of the table
  #      """
  #      return self.__table

    def preprocess(self):
        """
        preprocesses;
        """
        data  = self.getTable()
        data["month"] = pd.Series(["0"+x if int(x)<10 and len(x)<2 else x for x in data["month"]])
        data["day"] = pd.Series(["0"+x if int(x)<10 and len(x)<2 else x for x in data["day"]])
        data["time"] = data["year"] + data["month"] + data["day"]
        self.__table = data



    def groupByCo(self):
        """
        return:
            groups given class by Company;
        """
        data = self.getTable()
        gdata  = data.groupby(data['company'])
        ret = dict(list(gdata))
        self.__groupByCompany = ret
        #comInfo = gdata[companyId]

    def groupByDate(self, *args):
        """
        return:dict,grouped data by date; 
        """
        data = self.getTable()
        if isinstance(args[0], tuple):
            args = args[0]
        #print args
        keys = [data[x] for x in args]
        gdata = data.groupby(keys)
        return dict(list(gdata))

    def getCoInfo(self, companyId):
        """
        paras:
            companyId: id of company;
        return:
            Company infomation of given company Id;
        """
        data = self.__groupByCompany
        companyInfo = data[companyId]
        return companyInfo

    def getStats_skew(self, data):
        pass

    def getStatsByCo(self, companyId):
        """
        paras:
            companyId: id of company;
        """

        coInfo = self.getCoInfo(companyId)

        return coInfo['volume'].describe()
    
    def getStatsByDate(self, *args, **kwargs):
        """
        paras:
            year:'year', optional;
            month:'month', optional;
            day:'day', optional;
        return:
            stats info of specified date;
        demo:
            ss = self.getStatsByDate('year', 'month', year="2018", month="05");
        """
        data = self.groupByDate(args)
        dates = tuple([kwargs[x] for x in args])
        #print dates
        stats = data[dates]['volume'].describe()
        return stats

def main():
    pass

if __name__ == '__main__':
    main()
