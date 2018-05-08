"""
Volume Indicators
"""
from talib.abstract import Function
from finta import TA


class Volume:
    """
    Volume Indicators
    """

    AD = TA.ADL
    WOBV = TA.WOBV

    @classmethod
    def ADOSC(cls, data, fast_period=3, slow_period=10):
        """
        Accumulation/Distribution Oscillator
        :param data:
        :param int fast_period:
        :param int slow_period:
        :return:
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

        :param data:
        :param kwargs:
        :return:
        """
        fn = Function('OBV')
        return fn(data)


if __name__ == '__main__':
    print(Volume.OBV(['f']))
