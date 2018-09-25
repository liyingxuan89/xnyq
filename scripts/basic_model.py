#!/bin/env python 
#coding = utf8

import pandas as pd
import numpy as np
import logging
from datetime import datetime



class Basic(object):
    
    def __init__(self, table):
        """inin process"""
        if isinstance(table, np.ndarray):
            self.__table = pd.DataFrame(table)
        if isinstance(table, pd.DataFrame):
            self.__table = table

    def getTable(self):
        """
        fetch whole content of the table
        """
        return self.__table


    def getItem(self, columnName):
        """
        fetch one column of the table by name;
        paras:
            column keyword;
        return:
            A Series of specified column;
        """
        data = self.getTable()
        if columnName in data.columns:
            return data[columnName]
        else:
            print columnName + " if an invalid keyword!!!"
            raise KeyError


    def displayItem(self):
        """
        display features of this class;
        """
        data = self.getTable()
        return data.columns


    def NumOfRows(self):
        """
        get the total number of records;
        """
        data = self.getTable()
        return len(data.index)


    
