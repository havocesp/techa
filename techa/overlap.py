"""
Overlap Studies
"""
import pandas as pd
from finta import TA
from talib.abstract import *


class Overlap:
    """
    Overlap Studies
    """

    TRIX = TA.TRIX  # Triple Exponential Moving Average Oscillator
    KC = TA.KC  # Keltner Channels
    DO = TA.DO  # Donchian Channel
    ICHIMOKU = TA.ICHIMOKU  # Ichimoku indicator
    CHANDELIER = TA.CHANDELIER  # Chandelier Exit
    ER = TA.ER  # Kaufman Efficiency Oscillator
    VAMA = TA.VAMA  # Volume Adjusted Moving Average
    ZLEMA = TA.ZLEMA  # Zero Lag Moving Average
    HMA = TA.HMA  # Hell's Moving Average
    VORTEX = TA.VORTEX  # Vortex ondicator
    SMMA = TA.SMMA  # Volume Weighted Average Price
    VWAP = TA.VWAP  # Weighted Moving Average
    FISH = TA.FISH  # Fisher's transform
    APZ = TA.APZ  # Adaptive Price Zone


    @classmethod
    def BBANDS(cls, data, period=5, nbdevup=2, nbdevdn=2, ma_type=0):
        """
        Bollinger Bands

        Developed by John Bollinger, Bollinger Bands are volatility bands placed above and below a moving average.

        Volatility is based on the standard deviation, which changes as volatility increases and decreases.
        The bands automatically widen when volatility increases and narrow when volatility decreases.

        This method allows input of some other form of moving average like EMA or KAMA around which BBAND will be
        formed.

        Pass desired moving average as <MA> argument. For example BBANDS(MA=TA.KAMA(20)).

        This method returns other variations and derivatives of BBANDS as well.

        Bandwidth tells how wide the Bollinger Bands are on a normalized basis.

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data v
        :param int period: period used for indicator calculation
        :param float, int nbdevup: standard derivation to upper band
        :param float, int nbdevdn: standard derivation to lower band
        :param int ma_type: 0 for SMA or  1 for EMA
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('BBANDS')(data, timeperiod=period, nbdevup=nbdevup, nbdevdn=nbdevdn, matype=ma_type)


    @classmethod
    def DEMA(cls, data, period):
        """
        Double Exponential Moving Average
        TODO
        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('DEMA')(data, timeperiod=period)


    @classmethod
    def EMA(cls, data, period=30):
        """
        Exponential Moving Average

        Like all moving average indicators, they are much better suited for trending markets.

        When the market is in a strong and sustained uptrend, the EMA indicator line will also show an uptrend and
        vice-versa for a down trend.

        EMAs are commonly used in conjunction with other indicators to confirm significant market moves and to gauge
        their validity.

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('EMA')(data, timeperiod=period)


    @classmethod
    def HT_TRENDLINE(cls, data, **kwargs):
        """
        TODO
        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param kwargs: TODO
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('HT_TRENDLINE')(data, **kwargs)


    @classmethod
    def KAMA(cls, data, period=30):
        """
        Kaufman's Adaptive Moving Average

        KAMA is a moving average designed to account for market noise or volatility.

        It's main advantage is that it takes into consideration not just the direction, but the market volatility as
        well.

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('KAMA')(data, timeperiod=period)


    @classmethod
    def MA(cls, data, period=25, ma_type=0):
        """
        Moving Average

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('MA')(data, timeperiod=period, matype=ma_type)


    @classmethod
    def MAMA(cls, data, fast_limit=0.5, slow_limit=0.05):
        """
        MESA Adaptive Moving Average

        TODO

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param float fast_limit:
        :param float slow_limit:
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('MAMA')(data, fastlimit=fast_limit, slowlimit=slow_limit)


    @classmethod
    def MAVP(cls, data, min_period=2, max_period=30, ma_type=0):
        """
        Volume Adjusted Moving Average

        TODO

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int min_period: min period used for indicator calculation
        :param int max_period: max period used for indicator calculation
        :param int ma_type: moving average type (0 simple, 1 exponential)
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('MAVP')(data, minperiod=min_period, maxperiod=max_period, matype=ma_type)


    @classmethod
    def MIDPOINT(cls, data, period=14):
        """
        Mid Point
        TODO
        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('MIDPOINT')(data, timeperiod=period)


    @classmethod
    def MIDPRICE(cls, data, period=14):
        """
        Mid Price
        TODO
        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('MIDPRICE')(data, timeperiod=period)


    @classmethod
    def SAR(cls, data, accel=0.02, max_accel=0.2):
        """
        SAR stands for “stop and reverse,” which is the actual indicator used in the system.

        SAR trails price as the trend extends over time.

        The indicator is below prices when prices are rising and above prices when prices are falling.

        In this regard, the indicator stops and reverses when the price trend reverses and breaks above or below the
        indicator.

        Developed by John Bollinger, Bollinger Bands® are volatility bands placed above and below a moving average.

        Volatility is based on the standard deviation, which changes as volatility increases and decreases.

        The bands automatically widen when volatility increases and narrow when volatility decreases.

        This method allows input of some other form of moving average like EMA or KAMA around which BBAND will be
        formed.

        Pass desired moving average as <MA> argument. For example BBANDS(MA=TA.KAMA(20)).

        This method returns other variations and derivatives of BBANDS as well.

        Bandwidth tells how wide the Bollinger Bands are on a normalized basis.

        %b (pronounced "percent b") is derived from the formula for Stochastics and shows where price is in relation to
        the bands.

        %b equals 1 at the upper band and 0 at the lower band.
        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param float accel: acceleration factor
        :param float max_accel: max acceleration factor
        :return pd.Series: with indicator data calculation results with indicator data calculation results
        """
        return globals().get('SAR')(data, acceleration=accel, maximum=max_accel)


    @classmethod
    def SAREXT(cls, data, start=0, offset_on_reverse=0, accel_init_long=0.02, accel_long=0.02,
               accel_max_long=0.2, accel_init_short=0.02, accel_short=0.02, accel_max_short=0.2):
        """
        SAR Extended

        TODO
        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param start: start value
        :param int offset_on_reverse: offset on reverse
        :param float accel_init_long: initial long acceleration factor
        :param float accel_long: long acceleration factor
        :param float accel_max_long: max long acceleration factor
        :param float accel_init_short: initial short acceleration factor
        :param float accel_short: short acceleration factor
        :param float accel_max_short: max short acceleration factor
        :return pd.Series: with indicator data calculation results with indicator data calculation results
        """
        return globals().get('SAREXT')(data,
                                       startvalue=start,
                                       offsetonreverse=offset_on_reverse,
                                       accelerationinitlong=accel_init_long,
                                       accelerationlong=accel_long,
                                       accelerationmaxlong=accel_max_long,
                                       accelerationinitshort=accel_init_short,
                                       accelerationshort=accel_short,
                                       accelerationmaxshort=accel_max_short)


    @classmethod
    def SMA(cls, data, period=25):
        """
        Simple Moving Average

        The simple moving average (SMA) is the most basic of the moving averages used for trading.

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """

        return globals().get('SMA')(data, timeperiod=period)


    @classmethod
    def T3(cls, data, period=5, v_factor=0.7):
        """

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period:
        :param float v_factor:
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('T3')(data, timeperiod=period, vfactor=v_factor)


    @classmethod
    def TEMA(cls, data, period=30):
        """
        Triple exponential moving average

        Attempts to remove the inherent lag associated to Moving Averages by placing more weight on recent values.

        The name suggests this is achieved by applying a triple exponential smoothing which is not the case.

        The name triple comes from the fact that the value of an EMA (Exponential Moving Average) is triple.

        To keep it in line with the actual data and to remove the lag the value "EMA of EMA" is subtracted 3 times
        from the previously tripled EMA.

        Finally "EMA of EMA of EMA" is added.

        Because EMA(EMA(EMA)) is used in the calculation, TEMA needs 3 * period - 2 samples to start producing values
        in contrast to the period samples needed by a regular EMA.

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('TEMA')(data, timeperiod=period)


    @classmethod
    def TRIMA(cls, data, period=30):
        """
        Triangular Moving Average (TRIMA or TMA)

        Represents an average of prices, but places weight on the middle prices of the time period.

        The calculations double-smooth the data using a window width that is one-half the length of the series.

        The TRIMA is simply the SMA of the SMA.

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('TRIMA')(data, timeperiod=period)


    @classmethod
    def WMA(cls, data, period=30):
        """
        Weighted Moving Average

        It helps to smooth the price curve for better trend identification.

        HMA indicator is a common abbreviation of Hull Moving Average.

        The average was developed by Allan Hull and is used mainly to identify the current market trend.

        Unlike SMA (simple moving average) the curve of Hull moving average is considerably smoother.

        Moreover, because its aim is to minimize the lag between HMA and price it does follow the price activity much
        closer.

        It is used especially for middle-term and long-term trading.

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('WMA')(data, timeperiod=period)

if __name__ == '__main__':
    print()
