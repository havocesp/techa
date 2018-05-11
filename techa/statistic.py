"""
Statistic Functions
"""
import pandas as pd
from talib.abstract import *


class Statistic:
    """
    Statistic Functions
    """


    @classmethod
    def BETA(cls, data, period=5):
        """
        Beta function

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('BETA')
        return fn(data, timeperiod=period)


    @classmethod
    def CORREL(cls, data, period=30):
        """
        Pearson's Correlation Coefficient (r)

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('CORREL')
        return fn(data, timeperiod=period)


    @classmethod
    def LINEARREG(cls, data, period=14):
        """
        Linear Regression

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('LINEARREG')
        return fn(data, timeperiod=period)


    @classmethod
    def LINEARREG_ANGLE(cls, data, period=14):
        """
        Linear Regression Angle

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('LINEARREG_ANGLE')
        return fn(data, timeperiod=period)


    @classmethod
    def LINEARREG_INTERCEPT(cls, data, period=14):
        """
        Linear Regression Intercept

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('LINEARREG_INTERCEPT')
        return fn(data, timeperiod=period)


    @classmethod
    def LINEARREG_SLOPE(cls, data, period=14):
        """
        Linear Regression Slope

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('LINEARREG_SLOPE')
        return fn(data, timeperiod=period)


    @classmethod
    def STDDEV(cls, data, period=5, nbdev=1):
        """
        Standard Derivation

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :param float, int nbdev: deviation
        :return pd.Series: with indicator data calculation results
         """
        fn = Function('STDDEV')
        return fn(data, timeperiod=period, nbdev=nbdev)


    @classmethod
    def TSF(cls, data, period=14):
        """
        Time Series Forecast

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('TSF')
        return fn(data, timeperiod=period)


    @classmethod
    def VAR(cls, data, period=5, nbdev=1):
        """
        Variance

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :param float, int nbdev: deviation
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('VAR')
        return fn(data, timeperiod=period, nbdev=nbdev)

