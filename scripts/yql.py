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

class Yql(Basic):

    def __init__(self, table):
        """
        paras:
            table: numpy array or DataFrame that contains info of rijihuabiao;       
        """
        super(Yql, self).__init__(table)
        self.preprocess()
        self.__groupByCompany = None
        self.groupByCo()


    def preprocess(self):
        """
        preprocesses;
        """
        data  = self.getTable()
        data = data.dropna(axis=0, how='all')
        tempData = data[['online','lastMonthComsuption','delta','monthLastYear','tiaofeng']].fillna(value=0)
        data[['online','lastMonthComsuption','delta','monthLastYear','tiaofeng']] = tempData
        self.__table = data


    def groupByCo(self):
        """
        return:
            groups given class by Company;
        """
        data = self.getTable()
        gdata  = data.groupby(data['companyId'])
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

    def consumptionProportion(self, companyId, year=None):
        """
        paras:
            companyId: int, Id of the company you want to caculate;
            year: int, specify a year, otherwise the whole timelime will be caculate;
        return:
            the consumption proportion of one company in a year, which decript the inportance of that company;
        """
        data = self.getTable()
        
        if companyId:
            companyInfo = data[data.companyId==companyId].groupby(['year']).sum()
            consumption = companyInfo[companyInfo.index==year].loc[year,'consumption'] 
        if year:
            yearInfo = data.groupby(['year']).sum()
            yearConsumption = yearInfo[yearInfo.index==year].loc[year,'consumption']
        
        return '{:.4%}'.format(consumption/yearConsumption)

def main():
    pass

if __name__ == '__main__':
    main()
