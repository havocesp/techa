# -*- coding:utf-8 -*-
"""
Statistic Functions
"""
import pandas as pd
from talib.abstract import Function

__all__ = ['BETA', 'CORREL', 'LINEARREG', 'LINEARREG_ANGLE', 'LINEARREG_INTERCEPT', 'LINEARREG_SLOPE']


def BETA(data, period=5):
    """
    Beta function

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('BETA')
    return fn(data, timeperiod=period)


def CORREL(data, period=30):
    """
    Pearson's Correlation Coefficient (r)

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CORREL')
    return fn(data, timeperiod=period)


def LINEARREG(data, period=14):
    """
    Linear Regression

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('LINEARREG')
    return fn(data, timeperiod=period)


def LINEARREG_ANGLE(data, period=14):
    """
    Linear Regression Angle

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('LINEARREG_ANGLE')
    return fn(data, timeperiod=period)


def LINEARREG_INTERCEPT(data, period=14):
    """
    Linear Regression Intercept

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('LINEARREG_INTERCEPT')
    return fn(data, timeperiod=period)


def LINEARREG_SLOPE(data, period=14):
    """
    Linear Regression Slope

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('LINEARREG_SLOPE')
    return fn(data, timeperiod=period)


def STDDEV(data, period=5, nbdev=1):
    """
    Standard Derivation

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :param float, int nbdev: deviation
    :return pd.Series: with indicator data calculation results
     """
    fn = Function('STDDEV')
    return fn(data, timeperiod=period, nbdev=nbdev)


def TSF(data, period=14):
    """
    Time Series Forecast

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('TSF')
    return fn(data, timeperiod=period)


def VAR(data, period=5, nbdev=1):
    """
    Variance

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :param float, int nbdev: deviation
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('VAR')
    return fn(data, timeperiod=period, nbdev=nbdev)
