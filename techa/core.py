# -*- coding:utf-8 -*-
import inspect

import cycle
import momentum
import volume
import overlap
import volatility
import pattern
import statistic
import prices
import experimental

__all__ = ['TaLib']


# noinspection SpellCheckingInspection
class TaLib:
    """
    Technical Analysis Library
    """

    # Possible values: [ "talib" | "finta" | "core" ]
    # TODO Not fully implemented.
    # This attribute set a technical library as primary so the setted one (if possible) will be used .
    lib = 'core'

    @classmethod
    def calculate_indicator(cls, indicator, data, *args, **kwargs):
        indicator = str(indicator).upper()
        fn = None
        for fn_name in cls.get_functions():
            if indicator in fn_name:
                fn = getattr(cls, indicator)
        if fn is None:
            raise ValueError('{} function not found or not supported.'.format(indicator))
        else:
            return fn(data, *args, **kwargs)

    @classmethod
    def get_functions(cls):
        """
        Return all functions supported by this lib

        :return: all functions supported by this lib
        """
        return [s for s in sorted([fn for fn in cls.__dict__.keys() if fn.isupper()])]

    @classmethod
    def get_function_help(cls, func_name):
        return inspect.cleandoc(inspect.getdoc(getattr(cls, func_name))).replace('pd.', '').replace(': ',' ').replace(':return ', 'Return:\t').replace(':param ','Param:\t').replace('\tDataFrame ', '\t(DataFrame) ').replace('\tSeries','\t(Series) ').replace('\tint ','\t(int) ').replace('\tstr ', '\t(str) ').replace('\tfloat', '\t(float) ')

    # momentum
    ADX = classmethod(momentum.ADX)
    ADXR = classmethod(momentum.ADXR)
    APO = classmethod(momentum.APO)
    AROON = classmethod(momentum.AROON)
    AROONOSC = classmethod(momentum.AROONOSC)
    BASP = classmethod(momentum.BASP)
    BASPN = classmethod(momentum.BASPN)
    BOP = classmethod(momentum.BOP)
    CCI = classmethod(momentum.CCI)
    CMO = classmethod(momentum.CMO)
    COPP = classmethod(momentum.COPP)
    DX = classmethod(momentum.DX)
    EBBP = classmethod(momentum.EBBP)
    EFI = classmethod(momentum.EFI)
    EMV = classmethod(momentum.EMV)
    IFT_RSI = classmethod(momentum.IFT_RSI)
    IMI = classmethod(momentum.IMI)
    KST = classmethod(momentum.KST)
    MA = classmethod(momentum.MA)
    MACD = classmethod(momentum.MACD)
    MACDEXT = classmethod(momentum.MACDEXT)
    MACDFIX = classmethod(momentum.MACDFIX)
    MFI = classmethod(momentum.MFI)
    MINUS_DI = classmethod(momentum.MINUS_DI)
    MINUS_DM = classmethod(momentum.MINUS_DM)
    PLUS_DI = classmethod(momentum.PLUS_DI)
    PLUS_DM = classmethod(momentum.PLUS_DM)
    PPO = classmethod(momentum.PPO)
    ROC = classmethod(momentum.ROC)
    ROCP = classmethod(momentum.ROCP)
    ROCR = classmethod(momentum.ROCR)
    ROCR100 = classmethod(momentum.ROCR100)
    RSI = classmethod(momentum.RSI)
    STOCH = classmethod(momentum.STOCH)
    STOCHD = classmethod(momentum.STOCHD)
    STOCHF = classmethod(momentum.STOCHF)
    STOCHRSI = classmethod(momentum.STOCHRSI)
    TRIX = classmethod(momentum.TRIX)
    TSI = classmethod(momentum.TSI)
    ULTOSC = classmethod(momentum.ULTOSC)
    UO = classmethod(momentum.UO)
    VZO = classmethod(momentum.VZO)
    WILLR = classmethod(momentum.WILLR)
    WTO = classmethod(momentum.WTO)

    # Olverlap
    APZ = classmethod(overlap.APZ)
    BBANDS = classmethod(overlap.BBANDS)
    CHANDELIER = classmethod(overlap.CHANDELIER)
    DEMA = classmethod(overlap.DEMA)
    DO = classmethod(overlap.DO)
    EMA = classmethod(overlap.EMA)
    ER = classmethod(overlap.ER)
    FISH = classmethod(overlap.FISH)
    HMA = classmethod(overlap.HMA)
    HT_TRENDLINE = classmethod(overlap.HT_TRENDLINE)
    ICHIMOKU = classmethod(overlap.ICHIMOKU)
    KAMA = classmethod(overlap.KAMA)
    KC = classmethod(overlap.KC)
    MAMA = classmethod(overlap.MAMA)
    MAVP = classmethod(overlap.MAVP)
    MIDPOINT = classmethod(overlap.MIDPOINT)
    MIDPRICE = classmethod(overlap.MIDPRICE)
    SAR = classmethod(overlap.SAR)
    SAREXT = classmethod(overlap.SAREXT)
    SMA = classmethod(overlap.SMA)
    SMMA = classmethod(overlap.SMMA)
    T3 = classmethod(overlap.T3)
    TEMA = classmethod(overlap.TEMA)
    TRIMA = classmethod(overlap.TRIMA)
    VAMA = classmethod(overlap.VAMA)
    VORTEX = classmethod(overlap.VORTEX)
    WMA = classmethod(overlap.WMA)
    ZLEMA = classmethod(overlap.ZLEMA)

    # Volume
    AD = classmethod(volume.AD)
    ADOSC = classmethod(volume.ADOSC)
    OBV = classmethod(volume.OBV)
    WOBV = classmethod(volume.WOBV)

    # Volatitlity
    ATR = classmethod(volatility.ATR) if lib in 'core' else classmethod(momentum.ATR)
    NATR = classmethod(volatility.NATR)
    TRANGE = classmethod(volatility.TRANGE)

    # Price
    AVGPRICE = classmethod(prices.AVGPRICE)
    MEDPRICE = classmethod(prices.MEDPRICE)
    TYPPRICE = classmethod(prices.TYPPRICE)
    WCLPRICE = classmethod(prices.WCLPRICE)

    # Statistics
    BETA = classmethod(statistic.BETA)
    CORREL = classmethod(statistic.CORREL)
    LINEARREG = classmethod(statistic.LINEARREG)
    LINEARREG_ANGLE = classmethod(statistic.LINEARREG_ANGLE)
    LINEARREG_INTERCEPT = classmethod(statistic.LINEARREG_INTERCEPT)
    LINEARREG_SLOPE = classmethod(statistic.LINEARREG_SLOPE)
    STDDEV = classmethod(statistic.STDDEV)
    TSF = classmethod(statistic.TSF)
    VAR = classmethod(statistic.VAR)

    # cycle
    HT_DCPERIOD = classmethod(cycle.HT_DCPERIOD)
    HT_DCPHASE = classmethod(cycle.HT_DCPHASE)
    HT_PHASOR = classmethod(cycle.HT_PHASOR)
    HT_SINE = classmethod(cycle.HT_SINE)
    HT_TRENDMODE = classmethod(cycle.HT_TRENDMODE)

    # experimental
    SMEDPS = classmethod(experimental.SMEDPS)
    SPP = classmethod(experimental.SPP)
    SPPS = classmethod(experimental.SPPS)
    STYPP = classmethod(experimental.STYPP)

    class Pattern:
        """
        Candlestick pattern recognition methods.

        All functions returns a Series with a value in +100, 0 or -100 for each candlestick at "data" param.

        Possible values:

        * +100 means a bullish pattern shape.
        * -100 means a bearish pattern shape.
        * 0 means pattern is was not detected.

        """

        ABANDONED_BABY = classmethod(pattern.ABANDONED_BABY)
        ADVANCE_BLOCK = classmethod(pattern.ADVANCE_BLOCK)
        BELT_HOLD = classmethod(pattern.BELT_HOLD)
        BREAKAWAY = classmethod(pattern.BREAKAWAY)
        CLOSING_MARUBOZU = classmethod(pattern.CLOSING_MARUBOZU)
        CONCEAL_BABY_SWALL = classmethod(pattern.CONCEAL_BABY_SWALL)
        COUNTER_ATTACK = classmethod(pattern.COUNTER_ATTACK)
        DARK_CLOUD_COVER = classmethod(pattern.DARK_CLOUD_COVER)
        DOJI = classmethod(pattern.DOJI)
        DOJI_STAR = classmethod(pattern.DOJI_STAR)
        DRAGON_FLY_DOJI = classmethod(pattern.DRAGON_FLY_DOJI)
        ENGULFING = classmethod(pattern.ENGULFING)
        EVENING_DOJI_STAR = classmethod(pattern.EVENING_DOJI_STAR)
        EVENING_STAR = classmethod(pattern.EVENING_STAR)
        GAP_SIDE_SIDE_WHITE = classmethod(pattern.GAP_SIDE_SIDE_WHITE)
        GRAVESTONE_DOJI = classmethod(pattern.GRAVESTONE_DOJI)
        HAMMER = classmethod(pattern.HAMMER)
        HANGING_MAN = classmethod(pattern.HANGING_MAN)
        HARAMI = classmethod(pattern.HARAMI)
        HARAMI_CROSS = classmethod(pattern.HARAMI_CROSS)
        HIGH_WAVE = classmethod(pattern.HIGH_WAVE)
        HIKKAKE = classmethod(pattern.HIKKAKE)
        HIKKAKE_MOD = classmethod(pattern.HIKKAKE_MOD)
        HOMING_PIGEON = classmethod(pattern.HOMING_PIGEON)
        IDENTICAL_THREE_CROWS = classmethod(pattern.IDENTICAL_THREE_CROWS)
        INVERTED_HAMMER = classmethod(pattern.INVERTED_HAMMER)
        IN_NECK = classmethod(pattern.IN_NECK)
        KICKING = classmethod(pattern.KICKING)
        KICKING_BY_LENGTH = classmethod(pattern.KICKING_BY_LENGTH)
        LADDER_BOTTOM = classmethod(pattern.LADDER_BOTTOM)
        LONG_LEGGED_DOJI = classmethod(pattern.LONG_LEGGED_DOJI)
        LONG_LINE = classmethod(pattern.LONG_LINE)
        MARUBOZU = classmethod(pattern.MARUBOZU)
        MATCHING_LOW = classmethod(pattern.MATCHING_LOW)
        MAT_HOLD = classmethod(pattern.MAT_HOLD)
        MORNING_DOJI_STAR = classmethod(pattern.MORNING_DOJI_STAR)
        MORNING_STAR = classmethod(pattern.MORNING_STAR)
        ON_NECK = classmethod(pattern.ON_NECK)
        PIERCING = classmethod(pattern.PIERCING)
        RICK_SHAW_MAN = classmethod(pattern.RICK_SHAW_MAN)
        RISE_FALL_THREE_METHODS = classmethod(pattern.RISE_FALL_THREE_METHODS)
        SEPARATING_LINES = classmethod(pattern.SEPARATING_LINES)
        SHOOTING_STAR = classmethod(pattern.SHOOTING_STAR)
        SHORT_LINE = classmethod(pattern.SHORT_LINE)
        SPINNING_TOP = classmethod(pattern.SPINNING_TOP)
        STALLED_PATTERN = classmethod(pattern.STALLED_PATTERN)
        STICK_SANDWICH = classmethod(pattern.STICK_SANDWICH)
        TAKURI = classmethod(pattern.TAKURI)
        TASUKI_GAP = classmethod(pattern.TASUKI_GAP)
        THREE_BLACK_CROWS = classmethod(pattern.THREE_BLACK_CROWS)
        THREE_INSIDE = classmethod(pattern.THREE_INSIDE)
        THREE_LINE_STRIKE = classmethod(pattern.THREE_LINE_STRIKE)
        THREE_OUTSIDE = classmethod(pattern.THREE_OUTSIDE)
        THREE_STARSINSOUTH = classmethod(pattern.THREE_STARSINSOUTH)
        THREE_WHITE_SOLDIERS = classmethod(pattern.THREE_WHITE_SOLDIERS)
        THRUSTING = classmethod(pattern.THRUSTING)
        TRISTAR = classmethod(pattern.TRISTAR)
        TWO_CROWS = classmethod(pattern.TWO_CROWS)
        UNIQUE_THREE_RIVER = classmethod(pattern.UNIQUE_THREE_RIVER)
        UPSIDE_GAP_TWO_CROWS = classmethod(pattern.UPSIDE_GAP_TWO_CROWS)
        X_SIDE_GAP_THREE_METHODS = classmethod(pattern.X_SIDE_GAP_THREE_METHODS)

    @classmethod
    def detect_pattern(cls, pattern, data):
        """
        Detect a candlestick pattern using a DataFrame.

        :param str pattern: name of pattern to be detected
        :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
        :return pd.Series: for each DataFrame entry a 100, 0 or -100 will be returned.
        """
        fn = getattr(cls, str(pattern).upper())
        return fn(data)

    @classmethod
    def get_pattern_list(cls):
        """
        Get all supported patters names as list
        :return list: patters names list
        """
        return [s for s in sorted([p for p in cls.__dict__.keys() if p.isupper()])]


if __name__ == '__main__':
    from pprint import pprint

    print(TaLib.get_function_help('SMA'))
