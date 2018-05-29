# -*- coding:utf-8 -*-
"""
Price transform functions

References:
    http://www.fmlabs.com/reference
    http://www.fmlabs.com/reference/default.htm?url=TypicalPrices.htm
    http://www.fmlabs.com/reference/default.htm?url=AvgPrices.htm
    http://www.fmlabs.com/reference/default.htm?url=MedianPrices.htm
    http://www.fmlabs.com/reference/default.htm?url=WeightedCloses.htm

"""
import pandas as pd

__all__ = ['AVGPRICE', 'WCLPRICE', 'TYPPRICE', 'MEDPRICE']


def AVGPRICE(data):
    """
    Average Price.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    avgprice_list = []
    i = 0
    while i < len(data['close']):
        avgprice = (data['open'][i] + data['high'][i] + data['low'][i] + data['close'][i]) / 4
        avgprice_list.append(avgprice)
        i += 1
    return pd.Series(avgprice_list, name='AVGPRICE')


def MEDPRICE(data):
    """
    Median Price

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    medprice_list = []
    i = 0
    while i < len(data['close']):
        medprice = (data['high'][i] + data['low'][i]) / 2
        medprice_list.append(medprice)
        i += 1
    return pd.Series(medprice_list, name='MIDPRICE')


def TYPPRICE(data):
    """
    Typical Price

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    typprice_list = []
    i = 0
    while i < len(data['close']):
        typprice = (data['high'][i] + data['low'][i] + data['close'][i]) / 3
        typprice_list.append(typprice)
        i += 1
    return pd.Series(typprice_list, name='TYPPRICE')


def WCLPRICE(data):
    """
    Weighted Close Price.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    wclprice_list = []
    i = 0
    while i < len(data['close']):
        wclprice = (data['high'][i] + data['low'][i] + (data['close'][i] * 2)) / 4
        wclprice_list.append(wclprice)
        i += 1
    return pd.Series(wclprice_list, name='WCLPRICE')

