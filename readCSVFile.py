#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 23:13:02 2020

@author: Parveen

This is read csv script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeClassifier

def function1(csvfile):
    """
    

    Parameters
    ----------
    csvfile : Path of csv file
        DESCRIPTION:Reading the csv file

    Returns
    -------
    Pandas Dataframe

    """
    df= pd.read_csv(csvfile,header=0)
    return df

if __name__=="__main__":
    
    print(function1("/Users/c088259/Downloads/datasets_3681_5854_breastCancer.csv"))



