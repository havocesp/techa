"""
Momentum Indicators
"""
import pandas as pd
from finta import TA
from talib.abstract import *


class Momentum:
    """
    Momentum Indicators
    """
    MI = TA.MI # Mass Index
    COPP = TA.COPP  # Coppock Curve
    VZO = TA.VZO # VZO
    KST = TA.KST  # Know Sure Thing
    TSI = TA.TSI  # True Stregth Index
    EFI = TA.EFI  # Elder Force Index
    IFT_RSI = TA.IFT_RSI
    BASP = TA.BASP  # buy and sell pressure
    BASPN = TA.BASPN  # buy and sell pressure normalized
    UO = TA.UO  # ultimate oscillator
    CFI = TA.CFI  # Cumulative Force Index.
    EBBP = TA.EBBP  # Bull power and bear power
    EMV = TA.EMV  # Ease of Movement
    WTO = TA.WTO  # Wave Trend Oscillator


    @classmethod
    def ADX(cls, data, period=14):
        """
        ADX

        ADX is 100 * smoothed moving average of absolute value (DMI +/-) divided by (DMI+ + DMI-).

        ADX does not indicate trend direction or momentum, only trend strength.
        Generally, ADX readings below 20 indicate trend weakness, and readings above 40 indicate trend strength.

        An extremely strong trend is indicated by readings above 50

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period:
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('ADX')(data, timeperiod=period)


    @classmethod
    def ADXR(cls, data, period=14):
        """

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('ADXR')(data, timeperiod=period)


    @classmethod
    def APO(cls, data, fast_period=12, slow_period=26, ma_type=0):
        """

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('APO')(data, fastperiod=fast_period, slowperiod=slow_period, matype=ma_type)


    @classmethod
    def AROON(cls, data, period=14):
        """
        Aroon indicator
        TODO
        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('AROON')(data, timeperiod=period)


    @classmethod
    def AROONOSC(cls, data, period=14):
        """
        Aroon Oscillator
        TODO
        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('AROONOSC')(data, timeperiod=period)


    @classmethod
    def BOP(cls, data):
        """
        TODO
        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('BOP')(data)


    @classmethod
    def CCI(cls, data, period=14):
        """
        Commodity Index Channel
        TODO

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('CCI')(data, timeperiod=period)


    @classmethod
    def CMO(cls, data, period=14):
        """
        Chaikin Momentum Oscillator

        CMO is an oscillator that measures the accumulation/distribution line of the moving average convergence
        divergence (MACD).

        The Chaikin oscillator is calculated by subtracting a 10-day exponential moving average (EMA) of the
        ADL from a three-day EMA of the ADL, and highlights the momentum implied by the ADL.

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('CMO')(data, timeperiod=period)


    @classmethod
    def DX(cls, data, period=14):
        """
        TODO
        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param kwargs: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('DX')(data, timeperiod=period)


    @classmethod
    def MACD(cls, data, slow_period=10, fast_period=21, signal=9):
        """
        Moving Average Convergence Divergence

        The MACD Line oscillates above and below the zero line, which is also known as the center-line.

        These crossovers signal that the 12-day EMA has crossed the 26-day EMA. The direction, of course, depends on
        the direction of the moving average cross.

        Positive MACD indicates that the 12-day EMA is above the 26-day EMA. Positive values increase as the shorter
        EMA diverges further from the longer EMA.

        This means upside momentum is increasing. Negative MACD values indicates that the 12-day EMA is below the
        26-day EMA.

        Negative values increase as the shorter EMA diverges further below the longer EMA. This means downside momentum
        is increasing.

        Signal line crossovers are the most common MACD signals. The signal line is a 9-day EMA of the MACD Line.

        As a moving average of the indicator, it trails the MACD and makes it easier to spot MACD turns.

        A bullish crossover occurs when the MACD turns up and crosses above the signal line.

        A bearish crossover occurs when the MACD turns down and crosses below the signal line.

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int slow_period: slow period used for indicator calculation
        :param int fast_period: fast period used for indicator calculation
        :param int signal: period used for signal calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('MACD')(data, fastperiod=fast_period, slowperiod=slow_period, signalperiod=signal)


    @classmethod
    def MACDEXT(ls, data, fast_period=12, fast_ma_type=0, slow_period=26, slow_ma_type=0, signal_period=9,
                signal_ma_type=0):
        """
        Moving Average Convergence Divergence Extended

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int fast_period: fast period used for indicator calculation
        :param int fast_ma_type: fast moving average type (0 simple, 1 exponential)
        :param int slow_period: slow period used for indicator calculation
        :param int slow_ma_type: slow moving average type (0 simple, 1 exponential)
        :param int signal_period: period used for signal calculation
        :param int signal_ma_type: signal moving average type (0 simple, 1 exponential)
        :return pd.Series: with indicator data calculation results with indicator data calculation results
        """
        return globals().get('MACDEXT')(data, fastperiod=fast_period, fastmatype=fast_ma_type, slowperiod=slow_period,
                                        slowmatype=slow_ma_type, signalperiod=signal_period,
                                        signalmatype=signal_ma_type)


    @classmethod
    def MACDFIX(cls, data, signal_period=9):
        """
        Moving Average Convergence Divergence
        TODO
        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int signal_period: period used for signal calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('MACDFIX')(data, signalperiod=signal_period)


    @classmethod
    def MFI(cls, data, period=14):
        """
        Money Flow Indicator

        MFI is a momentum indicator that measures the inflow and outflow of money into a security over a specific
        period of time.

        MFI can be understood as RSI adjusted for volume.

        The money flow indicator is one of the more reliable indicators of overbought and oversold conditions, perhaps
        partly because it uses the higher readings of 80 and 20 as compared to the RSI's overbought/oversold readings
        of 70 and 30.

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('MFI')(data, timeperiod=period)


    @classmethod
    def MINUS_DI(cls, data, period=14):
        """
        Minus Directional Index indicator

        TODO
        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('MINUS_DI')(data, timeperiod=period)


    @classmethod
    def MINUS_DM(cls, data, period=14):
        """
        Minus Directional Movement indicator

        DM is a valuable tool for assessing price direction and strength.

        This indicator was created in 1978 by J. Welles Wilder, who also created the popular relative strength index.

        DMI tells you when to be long or short.

        It is especially useful for trend trading strategies because it differentiates between strong and weak trends,
        allowing the trader to enter only the strongest trends.

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('MINUS_DM')(data, timeperiod=period)


    @classmethod
    def MOM(cls, data, period=9):
        """
        Momentum Indicator

        MOM is measured by continually taking price differences for a fixed time interval.

        To construct a 10-day momentum line, simply subtract the closing price 10 days ago from the last closing price.

        This positive or negative value is then plotted around a zero line.

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('MOM')(data, timeperiod=period)


    @classmethod
    def PLUS_DI(cls, data, period=14):
        """
        Plus Directional Index indicator
        TODO
        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('PLUS_DI')(data, timeperiod=period)


    @classmethod
    def PLUS_DM(cls, data, period=14):
        """
        Plus Directional Movement indicator
        DM is a valuable tool for assessing price direction and strength.

        This indicator was created in 1978 by J. Welles Wilder, who also created the popular relative strength index.

        DMI tells you when to be long or short.

        It is especially useful for trend trading strategies because it differentiates between strong and weak trends,
        allowing the trader to enter only the strongest trends.

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('PLUS_DM')(data, timeperiod=period)


    @classmethod
    def PPO(cls, data, fast_period=12, slow_period=26, ma_type=0):
        """
        TODO
        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int fast_period: fast period used for indicator calculation
        :param int slow_period: slow period used for indicator calculation
        :param int ma_type: moving average type (0 simple, 1 exponential)
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('PPO')(data, fastperiod=fast_period, slowperiod=slow_period, matype=ma_type)


    @classmethod
    def ROC(cls, data, period=10):
        """
        Rate of Change

        ROC is a pure momentum oscillator that measures the percent change in price from one period to the next.

        The ROC calculation compares the current price with the price “n” periods ago.

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('ROC')(data, timeperiod=period)


    @classmethod
    def ROCP(cls, data, period=10):
        """
        Rate of Change

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('ROCP')(data, timeperiod=period)


    @classmethod
    def ROCR(cls, data, period=10):
        """
        Rate of Change

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('ROCR')(data, timeperiod=period)


    @classmethod
    def ROCR100(cls, data, period=10):
        """
        Rate of Change as 100 percentage
        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('ROCR100')(data, timeperiod=period)


    @classmethod
    def RSI(cls, data, period=14):
        """
        Relative Strength Index

        RSI is a momentum oscillator that measures the speed and change of price movements.

        RSI oscillates between zero and 100. Traditionally, and according to Wilder, RSI is considered overbought when
        above 70 and oversold when below 30.

        Signals can also be generated by looking for divergences, failure swings and centerline crossovers.

        RSI can also be used to identify the general trend.

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('RSI')(data, timeperiod=period)


    STOCHD = TA.STOCHD


    @classmethod
    def STOCH(cls, data, fastk_period=5, slowk_period=3, slowk_ma_type=0, slowd_period=3, slowd_ma_type=0):
        """
        Stochastic Oscillator

        The Stochastic Oscillator is a momentum indicator comparing the closing price of a security to the range of it's
        prices over a certain period of time.

        The sensitivity of the oscillator to market movements is reducible by adjusting that time period or by taking a
        moving average of the result.

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int fastk_period: period used for K fast indicator calculation
        :param int slowk_period: period used for K slow indicator calculation
        :param int slowk_ma_type: slow K moving average type (0 simple, 1 exponential)
        :param int slowd_period: period used for D slow indicator calculation
        :param int slowd_ma_type: slow D moving average type (0 simple, 1 exponential)
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('STOCH')(data, fastk_period=fastk_period, slowk_period=slowk_period,
                                      slowk_matype=slowk_ma_type, slowd_matype=slowd_ma_type, slowd_period=slowd_period)


    @classmethod
    def STOCHF(cls, data, fastk_period=5, fastd_period=3, fastd_ma_type=0):
        """
        Stochastic %F

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int fastk_period: period used for K fast indicator calculation
        :param int fastd_period: period used for D fast indicator calculation
        :param int fastd_ma_type: fast D moving average type (0 simple, 1 exponential)
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('STOCHF')(data, fastk_period=fastk_period, fastd_period=fastd_period,
                                       fastd_ma_type=fastd_ma_type)


    @classmethod
    def STOCHRSI(cls, data, period=14, fastk_period=5, fastd_period=3, fastd_ma_type=0):
        """
        Stochastic RSI

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: RSI period
        :param int fastk_period: period used for K fast indicator calculation
        :param int fastd_period: period used for D fast indicator calculation
        :param int fastd_ma_type: fast D moving average type (0 simple, 1 exponential)
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('STOCHRSI')(data, timeperiod=period, fastk_period=fastk_period, fastd_period=fastd_period,
                                         fastd_ma_type=fastd_ma_type)


    @classmethod
    def TRIX(cls, data, period=30):
        """
        Triple Exponential Moving Average Oscillator
        The TRIX is a momentum indicator that oscillates around zero.

        It displays the percentage rate of change between two triple smoothed exponential moving averages.

        To calculate TRIX we calculate triple smoothed EMA3 of n periods and then subtracts previous period EMA3 value
        from last EMA3 value and divide the result with yesterdays EMA3 value.

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('TRIX')(data, timeperiod=period)


    @classmethod
    def ULTOSC(cls, data, period1=7, period2=14, period3=28):
        """
        Ultimate Oscillator

        UO or ULTOSC is a momentum oscillator designed to capture momentum across three different time frames.

        The multiple time frame objective seeks to avoid the pitfalls of other oscillators.

        Many momentum oscillators surge at the beginning of a strong advance and then form bearish divergence as the
        advance continues.

        This is because they are stuck with one time frame. The Ultimate Oscillator attempts to correct this fault by
        incorporating longer time frames into the basic formula.

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period1: first period used for indicator calculation period used for indicator calculation
        :param int period2: second period used for indicator calculation period used for indicator calculation
        :param int period3: third period used for indicator calculation period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('ULTOSC')(data, timeperiod1=period1, timeperiod2=period2, timeperiod3=period3)


    @classmethod
    def WILLR(cls, data, period=14):
        """
        Williams %R

        Williams %R, or just %R, is a technical analysis oscillator showing the current closing price in relation to
        the high and low of the past N days (for a given N).

        It was developed by a publisher and promoter of trading materials, Larry Williams.

        It's purpose is to tell whether a stock or commodity market is trading near the high or the low, or somewhere in
        between, of its recent trading range.

        The oscillator is on a negative scale, from −100 (lowest) up to 0 (highest).

        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :param int period: period used for indicator calculation period used for indicator calculation
        :return pd.Series: with indicator data calculation results
        """
        return globals().get('WILLR')(data, timeperiod=period)
