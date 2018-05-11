"""
Cycle Indicators
"""
import pandas as pd
from talib.abstract import Function


class Cycle:
    """
    Cycle Indicators
    """


    @classmethod
    def HT_DCPERIOD(cls, data):
        """
        Hilbert Transform - Dominant Cycle Period

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('HT_DCPERIOD')
        return fn(data)


    @classmethod
    def HT_DCPHASE(cls, data):
        """
        Hilbert Transform - Dominant Cycle Phase

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('HT_DCPHASE')
        return fn(data)


    @classmethod
    def HT_PHASOR(cls, data):
        """
        Hilbert Transform - In-Phase Indicator

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('HT_PHASOR')
        return fn(data)


    @classmethod
    def HT_SINE(cls, data):
        """
        Hilbert Transform - SineWave Indicator

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('HT_SINE')
        return fn(data)


    @classmethod
    def HT_TRENDMODE(cls, data):
        """
        Hilbert Transform - Trend vs Cycle Mode

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('HT_TRENDMODE')
        return fn(data)


    @classmethod
    def WCLPRICE(cls, data):
        """
        Weighted Close Price

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('WCLPRICE')
        return fn(data)
