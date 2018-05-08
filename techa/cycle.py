"""
Cycle Indicators
"""
from finta import TA
from talib.abstract import *

class Cycle:
    """
    Cycle Indicators
    """


    @classmethod
    def HT_DCPERIOD(cls, data):
        """
        Hilbert Transform - Dominant Cycle Period
        :param data:
        :param kwargs:
        :return:
        """
        return globals().get('HT_DCPERIOD')(data)


    @classmethod
    def HT_DCPHASE(cls, data):
        """
        Hilbert Transform - Dominant Cycle Phase
        :param data:
        :param kwargs:
        :return:
        """
        return globals().get('HT_DCPHASE')(data)


    @classmethod
    def HT_PHASOR(cls, data):
        """
        Hilbert Transform - In-Phase Indicator
        :param data:
        :param kwargs:
        :return:
        """
        return globals().get('HT_PHASOR')(data)


    @classmethod
    def HT_SINE(cls, data):
        """
        Hilbert Transform - Sinewave Indicator
        :param data:
        :param kwargs:
        :return:
        """
        return globals().get('HT_SINE')(data)


    @classmethod
    def HT_TRENDMODE(cls, data):
        """
        Hilbert Transform - Market Mode
        :param data:
        :param kwargs:
        :return:
        """
        return globals().get('HT_TRENDMODE')(data)


    @classmethod
    def WCLPRICE(cls, data):
        return globals().get('WCLPRICE')(data)


if __name__ == '__main__':
    print()
