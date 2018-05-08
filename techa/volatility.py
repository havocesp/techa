"""
Volatility Indicators
"""
from finta import TA
from talib.abstract import *


class Volatility:
    """
    Volatility Indicators
    """


    @classmethod
    def ATR(cls, data, period=14):
        """
        Average True Range

        ATR is moving average of True Range.

        :param pd.DataFrame data:
        :return pd.Series:
        """
        return globals().get('ATR')(data, timeperiod=period)


    @classmethod
    def NATR(cls, data, period=14):
        """
        Normalized Average True Range

        :param pd.DataFrame data:
        :return pd.Series:
        """
        return globals().get('NATR')(data, timeperiod=period)


    @classmethod
    def TRANGE(cls, data, **kwargs):
        """
        True Range
        TR or TRANGE is the maximum of three price ranges.

        Most recent period's high minus the most recent period's low.

        Absolute value of the most recent period's high minus the previous close.

        Absolute value of the most recent period's low minus the previous close.

        :param pd.DataFrame data:
        :param kwargs:
        :return pd.Series:
        """
        return globals().get('TRANGE')(data, **kwargs)


if __name__ == '__main__':
    print(Volatility)
