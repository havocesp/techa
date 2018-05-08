"""
Statistic Functions
"""
import pandas as pd
from talib.abstract import *
from finta import TA


class Statistic:
    """
    Statistic Functions
    """

    @classmethod
    def BETA(cls, data, period=5):
        """
        Beta function
        TODO
        :param pd.DataFrame data:
        :param int period:
        :return pd.Series:
        """
        return globals().get('BETA')(data, timeperiod=period)


    @classmethod
    def CORREL(cls, data, period=30):
        """
        Correlation
        TODO
        :param pd.DataFrame data:
        :param int period:
        :return pd.Series:
        """
        return globals().get('CORREL')(data, timeperiod = period)


    @classmethod
    def LINEARREG(cls, data, period=14):
        """
        Linear Regression
        TODO
        :param pd.DataFrame data:
        :param int period:
        :return pd.Series:
        """
        return globals().get('LINEARREG')(data, timeperiod=period)


    @classmethod
    def LINEARREG_ANGLE(cls, data, period=14):
        """
        Linear Regression Angle
        TODO
        :param pd.DataFrame data:
        :param int period:
        :return pd.Series:
        """
        return globals().get('LINEARREG_ANGLE')(data, timeperiod=period)


    @classmethod
    def LINEARREG_INTERCEPT(cls, data, period=14):
        """
        Linear Regression Intercept
        TODO
        :param int period:
        :return pd.Series:
        """
        return globals().get('LINEARREG_INTERCEPT')(data, timeperiod=period)


    @classmethod
    def LINEARREG_SLOPE(cls, data, period=14):
        """
        Linear Regression Slope
        TODO
        :param pd.DataFrame data:
        :param int period:
        :return pd.Series:
        """
        return globals().get('LINEARREG_SLOPE')(data, timeperiod=period)


    @classmethod
    def STDDEV(cls, data, period = 5, nbdev = 1):
        """
        Standard Derivation
        TODO
        :param pd.DataFrame data:
        :param int period:
        :param float, int nbdev:
        :return pd.Series:
         """
        return globals().get('STDDEV')(data, timeperiod=period, nbdev=nbdev)


    @classmethod
    def TSF(cls, data, period=14):
        """
        TODO
        :param pd.DataFrame data:
        :param int period:
        :return pd.Series:
        """
        return globals().get('TSF')(data, timeperiod=period)


    @classmethod
    def VAR(cls, data, period=5, nbdev=1):
        """
        Variance
        TODO

        :param pd.DataFrame data:
        :param int period:
        :param float, int nbdev:
        :return pd.Series:
        """
        fn = Function('VAR')
        return fn(data, timeperiod=period, nbdev=nbdev)

if __name__ == '__main__':
    print(globals())
