# -*- coding: utf-8 -*-
"""
Momentum Indicators
"""
import pandas as pd
from finta import TA
from talib.abstract import Function

from overlap import MA
from volatility import ATR

__all__ = ['MI']


def MI(data, period=9):
    """
    Mass Index
    MI uses the high-low range to identify trend reversals based on range expansions.

    In this sense, the Mass Index is a volatility indicator that does not have a directional bias.

    Instead, the Mass Index identifies range bulges that can foreshadow a reversal of the current trend.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    return TA.MI(data, period=period)


def COPP(data):
    """
    Coppock Curve

    COPP is a momentum indicator, it signals buying opportunities when the indicator moved from negative territory
    to positive territory.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    return TA.COPP(data)


def VZO(data, period=14):
    """
    VZO

    VZO uses price, previous price and moving averages to compute its oscillating value.

    It is a leading indicator that calculates buy and sell signals based on oversold / overbought conditions.

    Oscillations between the 5% and 40% levels mark a bullish trend zone, while oscillations between -40% and 5%
    mark a bearish trend zone.

    Meanwhile, readings above 40% signal an overbought condition, while readings above 60% signal an extremely
    overbought condition.

    Alternatively, readings below -40% indicate an oversold condition, which becomes extremely oversold below -60%.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    return TA.VZO(data, period)


def KST(data, r1=10, r2=15, r3=20, r4=30):
    """
    Know Sure Thing

    KST is a momentum oscillator based on the smoothed rate-of-change for four different time frames.

    KST measures price momentum for four different price cycles. It can be used just like any momentum oscillator.

    Chartists can look for divergences, overbought/oversold readings, signal line crossovers and center-line
    crossovers.

    :param pd.DataFrame data:  pandas DataFrame with open, high, low, close data
    :param int r1: period used at first ROC calculation
    :param int r2: period used at second ROC calculation
    :param int r3: period used at third ROC calculation
    :param int r4: period used at last ROC calculation
    :return pd.Series: with indicator data calculation results
    """
    return TA.KST(data, r1, r2, r3, r4)


def TSI(data, long=25, short=13, signal=13):
    """
    True Strength Index

    TSI is a momentum oscillator based on a double smoothing of price changes.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int long: long period used for indicator calculation
    :param int short: short period used for indicator calculation
    :param int signal: signal period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    return TA.TSI(data, long, short, signal)


def EFI(data, period=13):
    """
    Elder Force Index

    EFI is an indicator that uses price and volume to assess the power behind a move or identify possible turning
    points.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    return TA.EFI(data, period=period)


def IFT_RSI(data, rsi_period=14, wma_period=9):
    """
    Modified Inverse Fisher Transform applied on RSI.

    Suggested method to use any IFT indicator is to buy when the indicator crosses over –0.5 or crosses over +0.5

    if it has not previously crossed over –0.5 and to sell short when the indicators crosses under +0.5 or crosses
    under –0.5 if it has not previously crossed under +0.5.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int rsi_period: pandas DataFrame with open, high, low, close data
    :param int wma_period: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    return TA.IFT_RSI(data, rsi_period, wma_period)


def BASP(data, period=40):
    """
    Buy and Sell Pressure

    BASP indicator serves to identify buying and selling pressure.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    return TA.BASP(data, period)


def BASPN(data, period=40):
    """
    Buy and Sell Pressure Normalized

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    return TA.BASPN(data, period)


def UO(data):
    """
    Ultimate Oscillator

    UO is a momentum oscillator designed to capture momentum across three different time frames.

    The multiple time frame objective seeks to avoid the pitfalls of other oscillators.

    Many momentum oscillators surge at the beginning of a strong advance and then form bearish divergence as the
    advance continues.

    This is because they are stuck with one time frame. The Ultimate Oscillator attempts to correct this fault by
    incorporating longer time frames into the basic formula.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    return TA.UO(data)


def CFI(data):
    """
    Cumulative Force Index.

    Adopted from  Elder's Force Index (EFI).

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    return TA.CFI(data)


def EBBP(data):
    """
    Bull power and bear power by Dr. Alexander Elder

    EBBP show where today’s high and low lie relative to the a 13-day EMA

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    return TA.EBBP(data)


def EMV(data, period=14):
    """
    Ease of Movement

    EMV is a volume-based oscillator that fluctuates above and below the zero line.

    As its name implies, it is designed to measure the "ease" of price movement.

    Prices are advancing with relative ease when the oscillator is in positive territory.

    Conversely, prices are declining with relative ease when the oscillator is in negative territory.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return:pd.Series: with indicator data calculation results
    """
    return TA.EMV(data, period)


def WTO(data, channel_length=10, average_length=21):
    """
    Wave Trend Oscillator

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int channel_length: channel length value
    :param int average_length: average length value
    :return pd.Series: with indicator data calculation results
    """
    return TA.WTO(data, channel_length, average_length)


def STOCHD(data, period=3):
    """
    Stochastic Oscillator %D

    STOCH %D is a 3 period simple moving average of %K.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    return TA.STOCHD(data, period)


def ADX(data, period=14):
    """
    ADX

    ADX is 100 * smoothed moving average of absolute value (DMI +/-) divided by (DMI+ + DMI-).

    ADX does not indicate trend direction or momentum, only trend strength.
    Generally, ADX readings below 20 indicate trend weakness, and readings above 40 indicate trend strength.

    An extremely strong trend is indicated by readings above 50

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    temp_df = pd.DataFrame()
    temp_df['up_move'] = data['high'].diff()
    temp_df['down_move'] = data['low'].diff()

    positive_dm = []
    negative_dm = []

    for row in temp_df.itertuples():
        if row.up_move > row.down_move and row.up_move > 0:
            positive_dm.append(row.up_move)
        else:
            positive_dm.append(0)
        if row.down_move > row.up_move and row.down_move > 0:
            negative_dm.append(row.down_move)
        else:
            negative_dm.append(0)

    temp_df['positive_dm'] = positive_dm
    temp_df['negative_dm'] = negative_dm

    atr = ATR(data, period=period * 6)

    dir_plus = pd.Series(100 * (temp_df['positive_dm'] / atr).ewm(span=period, min_periods=period - 1).mean())

    dir_minus = pd.Series(100 * (temp_df['negative_dm'] / atr).ewm(span=period, min_periods=period - 1).mean())
    return pd.concat([dir_plus, dir_minus])
    # fn = Function('ADX')
    # return fn(data, period)


def ADXR(data, period=14):
    """
    Average Directional Movement Index Rating

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('ADXR')
    return fn(data, period)


def IMI(data):
    """
    Inter-day Momentum Index

    source: http://www.fmlabs.com/reference/default.htm?url=IMI.htm
    """
    imi_list = []
    up_sum = .0
    down_sum = .0
    i = 0
    while i < len(data['close']):
        if data['close'][i] > data['open'][i]:
            up_sum = up_sum + (data['close'][i] - data['open'][i])
        else:
            down_sum = down_sum + (data['open'][i] - data['close'][i])
        imi = 100 * (up_sum / (up_sum + down_sum))
        imi_list.append(imi)
        i += 1
    return imi_list


def APO(data, fast_period=12, slow_period=26, ma_type=0, price='close'):
    """
    Absolute Price Oscillator

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int fast_period: fast period used for indicator calculation
    :param int slow_period: slow period used for indicator calculation
    :param int ma_type: moving average type (0 simple, 1 exponential)
    :param str price: column used for indicator calculation (default = "close")
    :return pd.Series: with indicator data calculation results
    """

    apo_list = []
    i = 0
    while i < len(data[price]):
        if i + 1 < slow_period:
            apo = float('NaN')
        else:
            start_fast = i + 1 - fast_period
            end = i + 1
            sma_fast = MA(data[price][start_fast:end], period=fast_period, ma_type=ma_type)
            start_slow = i + 1 - slow_period
            end = i + 1
            sma_slow = MA(data[price][start_slow:end], period=slow_period, ma_type=ma_type)
            apo = sma_slow - sma_fast
        #            apo *= -1
        apo_list.append(apo)
        i += 1
    return pd.Series(apo_list, name='APO')


def AROON(data, period=14):
    """
    Aroon indicator

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: up and down indicators from data calculation
    """
    fn = Function('AROON')
    return fn(data, period)


def AROONOSC(data, period=14):
    """
    Aroon Oscillator

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('AROONOSC')
    return fn(data, period)


def BOP(data):
    """
    Balance of Power Indicator

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('BOP')
    return fn(data)


def CCI(data, period=14):
    """
    Commodity Index Channel

    CCI is a versatile indicator that can be used to identify a new trend or warn of extreme conditions.

    CCI measures the current price level relative to an average price level over a given period of time.

    The CCI typically oscillates above and below a zero line. Normal oscillations will occur within the range of
    +100 and −100.

    Readings above +100 imply an overbought condition, while readings below −100 imply an oversold condition.

    As with other overbought/oversold indicators, this means that there is a large probability that the price will
    correct to more representative levels.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CCI')
    return fn(data, period)


def CMO(data, period=14):
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
    fn = Function('CMO')
    return fn(data, period)


def DX(data, period=14):
    """
    Directional Movement Index

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('DX')
    return fn(data, period)


def MACD(data, slow_period=10, fast_period=21, signal=9, price='close'):
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
    :param str price: column used for indicator calculation (default = "close")
    :return pd.Series: with indicator data calculation results
    """
    ema_fast = pd.Series(data[price].ewm(ignore_na=False,
                                         min_periods=fast_period - 1, span=fast_period).mean(), index=data.index)

    ema_slow = pd.Series(data[price].ewm(ignore_na=False,
                                         min_periods=slow_period - 1, span=slow_period).mean(), index=data.index)

    macd_series = pd.Series(ema_fast - ema_slow, index=data.index, name='macd')

    macd_signal_series = macd_series.ewm(ignore_na=False, span=signal).mean()

    macd_signal_series = pd.Series(macd_signal_series, index=data.index, name='macd_signal')
    macd_df = pd.concat([macd_signal_series, macd_series], axis=1)

    return pd.DataFrame(macd_df)


def MACDEXT(data, fast_period=12, fast_ma_type=0, slow_period=26, slow_ma_type=0, signal_period=9,
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
    fn = Function('MACDEXT')
    return fn(data, fastperiod=fast_period, fastmatype=fast_ma_type,
              slowperiod=slow_period,
              slowmatype=slow_ma_type, signalperiod=signal_period,
              signalmatype=signal_ma_type)


def MACDFIX(data, signal_period=9):
    """
    Moving Average Convergence/Divergence Fix 12/26

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int signal_period: period used for signal calculation
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('MACDFIX')
    return fn(data, signalperiod=signal_period)


def MFI(data, period=14):
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
    fn = Function('MFI')
    return fn(data, period)


def MINUS_DI(data, period=14):
    """
    Minus Directional indicator

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('MINUS_DI')
    return fn(data, period)


def MINUS_DM(data, period=14):
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
    fn = Function('MINUS_DM')
    return fn(data, period)


def MOM(data, period=9):
    """
    Momentum Indicator

    MOM is measured by continually taking price differences for a fixed time interval.

    To construct a 10-day momentum line, simply subtract the closing price 10 days ago from the last closing price.

    This positive or negative value is then plotted around a zero line.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('MOM')
    return fn(data, period)


def PLUS_DI(data, period=14):
    """
    Plus Directional Index indicator

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('PLUS_DI')
    return fn(data, period)


def PLUS_DM(data, period=14):
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
    fn = Function('PLUS_DM')
    return fn(data, period)


def PPO(data, fast_period=12, slow_period=26, ma_type=0):
    """
    Percentage Price Oscillator

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int fast_period: fast period used for indicator calculation
    :param int slow_period: slow period used for indicator calculation
    :param int ma_type: moving average type (0 simple, 1 exponential)
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('PPO')
    return fn(data, fastperiod=fast_period, slowperiod=slow_period, matype=ma_type)


def ROC(data, period=10):
    """
    Rate of Change

    ROC is a pure momentum oscillator that measures the percent change in price from one period to the next.

    The ROC calculation compares the current price with the price “n” periods ago.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('ROC')
    return fn(data, period)


def ROCP(data, period=10):
    """
    Rate of Change

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('ROCP')
    return fn(data, period)


def ROCR(data, period=10):
    """
    Rate of Change

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('ROCR')
    return fn(data, period)


def ROCR100(data, period=10):
    """
    Rate of Change as 100 percentage

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('ROCR100')
    return fn(data, period)


def RSI(data, period=14, price='close'):
    """
    Relative Strength Index

    RSI is a momentum oscillator that measures the speed and change of price movements.

    RSI oscillates between zero and 100. Traditionally, and according to Wilder, RSI is considered overbought when
    above 70 and oversold when below 30.

    Signals can also be generated by looking for divergences, failure swings and center-line crossovers.

    RSI can also be used to identify the general trend.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation period used for indicator calculation
    :param str price: column used for indicator calculation (default = "close")
    :return pd.Series: with indicator data calculation results
    """
    rsi_series = pd.DataFrame(index=data.index)
    gain = [0]
    loss = [0]

    for row, shifted_row in zip(data[price], data[price].shift(-1)):
        if row - shifted_row > 0:
            gain.append(row - shifted_row)
            loss.append(0)
        elif row - shifted_row < 0:
            gain.append(0)
            loss.append(abs(row - shifted_row))
        elif row - shifted_row == 0:
            gain.append(0)
            loss.append(0)

    rsi_series['gain'] = gain
    rsi_series['loss'] = loss

    avg_gain = rsi_series['gain'].rolling(window=period).mean()
    avg_loss = rsi_series['loss'].rolling(window=period).mean()
    relative_strength = avg_gain / avg_loss
    rsi_ = 100 - (100 / (1 + relative_strength))
    return pd.Series(rsi_, index=data.index, name='RSI')
    # fn = Function('RSI')
    # return fn(data, period)


def STOCH(data, fastk_period=5, slowk_period=3, slowk_ma_type=0, slowd_period=3, slowd_ma_type=0):
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
    fn = Function('STOCH')
    return fn(data, fastk_period=fastk_period, slowk_period=slowk_period,
              slowk_matype=slowk_ma_type, slowd_matype=slowd_ma_type,
              slowd_period=slowd_period)


def STOCHF(data, fastk_period=5, fastd_period=3, fastd_ma_type=0):
    """
    Stochastic %F

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int fastk_period: period used for K fast indicator calculation
    :param int fastd_period: period used for D fast indicator calculation
    :param int fastd_ma_type: fast D moving average type (0 simple, 1 exponential)
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('STOCHF')
    return fn(data, fastk_period=fastk_period, fastd_period=fastd_period,
              fastd_ma_type=fastd_ma_type)


def STOCHRSI(data, period=14, fastk_period=5, fastd_period=3, fastd_ma_type=0):
    """
    Stochastic RSI

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: RSI period
    :param int fastk_period: period used for K fast indicator calculation
    :param int fastd_period: period used for D fast indicator calculation
    :param int fastd_ma_type: fast D moving average type (0 simple, 1 exponential)
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('STOCHRSI')
    return fn(data, period, fastk_period=fastk_period,
              fastd_period=fastd_period,
              fastd_ma_type=fastd_ma_type)


def TRIX(data, period=30):
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
    fn = Function('TRIX')
    return fn(data, period)


def ULTOSC(data, period1=7, period2=14, period3=28):
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
    fn = Function('ULTOSC')
    return fn(data, timeperiod1=period1, timeperiod2=period2, timeperiod3=period3)


def WILLR(data, period=14):
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
    willr_list = []
    i = 0
    close, high, low = data['close'], data['high'], data['low']
    while i < len(close):
        if i + 1 < period:
            willr = float('NaN')
        else:
            start = i + 1 - period
            end = i + 1
            willr = (max(high[start:end]) - close[i]) / (max(high[start:end]) - min(low[start:end])) * 100
        #            willr *= -1
        willr_list.append(willr)
        i += 1
    return willr_list
    # fn = Function('WILLR')
    # return fn(data, period)
