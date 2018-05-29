# -*- coding: utf-8 -*-
"""
Cycle Indicators
"""
import pandas as pd
from talib.abstract import Function

__all__ = ['HT_DCPERIOD', 'HT_DCPHASE', 'HT_SINE', 'HT_TRENDMODE', 'HT_PHASOR']


def HT_DCPERIOD(data):
    """
    Hilbert Transform

    Dominant Cycle Period

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('HT_DCPERIOD')
    return fn(data)


def HT_DCPHASE(data):
    """
    Hilbert Transform

    Dominant Cycle Phase

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('HT_DCPHASE')
    return fn(data)


def HT_PHASOR(data):
    """
    Hilbert Transform

    In-Phase Indicator.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('HT_PHASOR')
    return fn(data)


def HT_SINE(data):
    """
    Hilbert Transform - SineWave Indicator

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('HT_SINE')
    return fn(data)


def HT_TRENDMODE(data):
    """
    Hilbert Transform

    Trend vs Cycle Mode.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('HT_TRENDMODE')
    return fn(data)



