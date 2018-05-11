"""
Volume Indicators
"""
import pandas as pd
from finta import TA
from talib.abstract import Function


class Volume:
    """
    Volume Indicators
    """


    @classmethod
    def AD(cls, data):
        """
        Accumulation Distribution Line Indicator

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        ad_list = []
        i = 0
        while i < len(data['close']):
            ad = 0
            if i > 0:
                clv = ((data['close'][i] - data['low'][i]) - (data['high'][i] - data['close'][i])) / (
                        data['high'][i] - data['low'][i])
                ad = ad_list[i - 1] + clv * data['volume'][i]
            ad_list.append(ad)
            i += 1
        return pd.Series(ad_list, name='AD')


    @classmethod
    def WOBV(cls, data):
        """
        Weighted On Balance Volume

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """

        return TA.WOBV(data)


    @classmethod
    def ADOSC(cls, data, fast_period=3, slow_period=10):
        """
        Accumulation/Distribution Oscillator

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int fast_period: fast period used for indicator calculation
        :param int slow_period: slow period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        fn = Function('ADOSC')
        return fn(data, fastperiod=fast_period, slowperiod=slow_period)


    @classmethod
    def OBV(cls, data):
        """
        On Balance Volume

        OBV measures buying and selling pressure as a cumulative indicator that adds volume on up days and subtracts
        volume on down days.

        OBV was developed by Joe Granville and introduced in his 1963 book, Granville's New Key to Stock Market Profits.

        It was one of the first indicators to measure positive and negative volume flow.

        Chartists can look for divergences between OBV and price to predict price movements or use OBV to confirm price
        trends.

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        obv_list = []
        i = 0
        while i < len(data['close']):
            obv = 0
            if i > 0:
                if data['close'][i] > data['close'][i - 1]:
                    obv = obv_list[i - 1] + data['volume'][i]
                elif data['close'][i] < data['close'][i - 1]:
                    obv = obv_list[i - 1] - data['volume'][i]
                else:
                    obv = obv_list[i - 1]
            obv_list.append(obv)
            i += 1
        return pd.Series(obv_list, name='OBV')
        # fn = Function('OBV')
        # return fn(data)
