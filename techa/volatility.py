# -*- coding: utf-8 -*-
"""
Volatility Indicators
"""
import pandas as pd
from talib.abstract import *

__all__ = ['ATR', 'NATR', 'TRANGE']


def ATR(data, period=14):
    """
    Average True Range

    ATR is moving average of True Range.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    tr_list = TRANGE(data)
    atr_list = []
    i = 0
    while i < len(data['close']):
        if i + 1 < period:
            atr = float('NaN')
        else:
            atr = ((tr_list[i - 1] * (period - 1)) + tr_list[i]) / period
        atr_list.append(atr)
        i += 1
    return pd.Series(atr_list, name='ATR')


def NATR(data, period=14):
    """
    Normalized Average True Range

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('NATR')
    return fn(data, timeperiod=period)


def TRANGE(data):
    """
    True Range
    TR or TRANGE is the maximum of three price ranges.

    Most recent period's high minus the most recent period's low.

    Absolute value of the most recent period's high minus the previous close.

    Absolute value of the most recent period's low minus the previous close.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close, data
    :return pd.Series: with indicator data calculation results.
    """
    tr_list = []
    i = 0
    while i < len(data['close']):
        if i < 1:
            tr = float('NaN')
        else:
            true_high = data['high'][i]
            if data['close'][i - 1] > data['high'][i]:
                true_high = data['close'][i - 1]
            true_low = data['low'][i]
            if data['close'][i - 1] < data['low'][i]:
                true_low = data['close'][i - 1]
            tr = true_high - true_low
        tr_list.append(tr)
        i += 1
    return pd.Series(tr_list, name='TRANGE')
