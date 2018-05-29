"""
Overlap Studies
"""

import pandas as pd
from finta import TA
from talib.abstract import Function

__all__ = ['TRIMA', 'TRIX', 'KC', 'MA', 'MIDPRICE', 'HT_TRENDLINE', 'CHANDELIER', 'BBANDS', 'MIDPOINT', 'DO', 'DEMA',
           'EMA', 'ZLEMA', 'APZ', 'SAR', 'SAREXT', 'SMA', 'SMMA', 'FISH', 'HMA', 'TEMA', 'VAMA', 'VORTEX', 'ICHIMOKU',
           'ER', 'KAMA', 'VWAP', 'MAVP', 'MAMA', 'T3', 'WMA']


def TRIX(data, period=15, price='close'):
    """
    Triple Exponential Moving Average Oscillator

    TRIX is a momentum indicator that oscillates around zero.

    It displays the percentage rate of change between two triple smoothed exponential moving averages.

    To calculate TRIX we calculate triple smoothed EMA3 of n periods and then subtract previous period EMA3 value

    from last EMA3 value and divide the result with yesterdays EMA3 value.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :param str price: column used for indicator calculation (default = "close")
    :return pd.Series: with indicator data calculation results
    """
    exponential_average_one = EMA(data, period, price=price)
    exponential_average_two = exponential_average_one.ewm(ignore_na=False, min_periods=period - 1, span=period).mean()
    exponential_average_three = exponential_average_two.ewm(ignore_na=False, min_periods=period - 1, span=period).mean()

    return exponential_average_three.pct_change(periods=1)


def KC(data, period=20):
    """
    Keltner Channels

    KC are volatility-based envelopes set above and below an exponential moving average.

    This indicator is similar to Bollinger Bands, which use the standard deviation to set the bands.

    Instead of using the standard deviation, Keltner Channels use the Average True Range (ATR) to set channel
    distance.

    The channels are typically set two Average True Range values above and below the 20-day EMA.

    The exponential moving average dictates direction and the Average True Range sets channel width.

    Keltner Channels are a trend following indicator used to identify reversals with channel breakouts and channel
    direction.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    return TA.KC(data, period)


def DO(data, period=20):
    """
    Donchian Channel

    DC is a moving average indicator developed by Richard Donchian.

    It plots the highest high and lowest low over the last period time intervals.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    return TA.DO(data, period)


def ICHIMOKU(data):
    """
    Ichimoku indicator

    The Ichimoku Cloud, also known as Ichimoku Kinko Hyo, is a versatile indicator that defines support and
    resistance, identifies trend direction, gauges momentum and provides trading signals.

    Ichimoku Kinko Hyo translates into “one look equilibrium chart”.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    return TA.ICHIMOKU(data)


def CHANDELIER(data, period_1=14, period_2=22, k=3):
    """
    Chandelier Exit

    Chandelier Exit sets a trailing stop-loss based on the Average True Range (ATR).

    The indicator is designed to keep traders in a trend and prevent an early exit as long as the trend extends.

    Typically, the Chandelier Exit will be above prices during a downtrend and below prices during an uptrend.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period_1: first period used for indicator calculation
    :param int period_2: second period used for indicator calculation
    :param k:
    :return pd.Series: with indicator data calculation results
    """
    return TA.CHANDELIER(ohlc=data, period_1=period_1, period_2=period_2, k=k)


def ER(data, period=10, price='close'):
    """
    Kaufman Efficiency Oscillator

    ER indicator is an oscillator indicator that oscillates between +100 and -100, where zero is the center point.
    +100 is upward FOREX trending market and -100 is downwards trending markets.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :param str price: column used for indicator calculation (default = "close")
    :return pd.Series: with indicator data calculation results
    """
    change = data[price].diff(periods=period).abs()
    vol = data[price].diff().abs().rolling(window=period).sum()
    return pd.Series(change / vol)


def VAMA(data, period=8, column='close'):
    """
    Volume Adjusted Moving Average

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :param str column: column used for indicator calculation (default = "close")
    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    """
    return TA.VAMA(data, period, column)


def ZLEMA(data, period=26, price='close'):
    """
    Zero Lag Moving Average

    ZLEMA is an abbreviation of Zero Lag Exponential Moving Average. It was developed by John Ehlers and Rick Way.

    ZLEMA is a kind of Exponential moving average but its main idea is to eliminate the lag arising from the very
    nature of the moving averages and other trend following indicators.

    As it follows price closer, it also provides better price averaging and responds better to price swings.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :param str price: column used for indicator calculation (default = "close")
    :return pd.Series: with indicator data calculation results
    """
    lag = (period - 1) / 2
    return pd.Series(data[price] + (data[price].diff(lag)), name='zero_lag_ema')

    # return TA.ZLEMA(data, period)


def HMA(data, period=16):
    """
    Hell's Moving Average

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
    return TA.HMA(data, period)


def VORTEX(data, period=42):
    """
    Vortex Indicator

    The Vortex indicator plots two oscillating lines, one to identify positive trend movement and the other
    to identify negative price movement.

    Indicator construction revolves around the highs and lows of the last two days or periods.

    The distance from the current high to the prior low designates positive trend movement while the
    distance between the current low and the prior high designates negative trend movement.

    Strongly positive or negative trend movements will show a longer length between the two numbers while
    weaker positive or negative trend movement will show a shorter length.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    return TA.VORTEX(data, period)


def SMMA(data, period=14, price='close'):
    """
    Smoothed Simple Moving Average

    SMMA gives recent prices an equal weighting to historic prices.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :param str price: column used for indicator calculation (default = "close")
    :return pd.Series: with indicator data calculation results
    """
    ma = data[price].ewm(alpha=1 / period).mean()
    return pd.Series(ma, index=data.index, name='smoothed_ma')


def VWAP(data):
    """
    Weighted Moving Average

    WMAP helps to smooth the price curve for better trend identification.

    It places even greater importance on recent data than the EMA does.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    return TA.VWAP(data)


def FISH(data, period=10):
    """
    Fisher's Transform

    FISH was presented by John Ehler's. It assumes that price distributions behave like square waves.

    The Fisher Transform uses the mid-point or median price in a series of calculations to produce an oscillator.

    A signal line which is a previous value of itself is also calculated.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    return TA.FISH(data, period)


def APZ(data, period=21, dev_factor=2, ma_type=None):
    """
    Adaptive Price Zone

    APZ is as a volatility based indicator developed by Lee Leibfarth that appears as a set of bands placed over a
    price chart.

    Especially useful in non-trending, choppy markets, the APZ was created to help traders find potential turning
    points in the markets.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :param float dev_factor: standard derivation factor
    :param int ma_type: moving average type (0 simple, 1 exponential)
    :return pd.Series: with indicator data calculation results
    """
    return TA.APZ(data, period, dev_factor, ma_type)


# noinspection SpellCheckingInspection

def BBANDS(data, period=5, nbdevup=2, nbdevdn=2, ma_type=0, price='close'):
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

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :param float, int nbdevup: standard derivation to upper band
    :param float, int nbdevdn: standard derivation to lower band
    :param int ma_type: 0 for SMA or  1 for EMA
    :param str price: column used for indicator calculation (default = "close")
    :return pd.Series: with indicator data calculation results
    """
    std_dev = data[price].std()
    if ma_type == 1:
        middle_band = EMA(data, period=period, price=price)
    else:
        middle_band = SMA(data, period=period, price=price)
    upper_bband = pd.Series(middle_band + (nbdevup * std_dev), name='upper_bband')
    lower_bband = pd.Series(middle_band - (nbdevdn * std_dev), name='lower_bband')

    percent_b = (data[price] - lower_bband) / (upper_bband - lower_bband)

    b_bandwidth = pd.Series((upper_bband - lower_bband) / middle_band)

    return pd.concat([upper_bband, middle_band, lower_bband, b_bandwidth, percent_b], axis=1)


def DEMA(data, period):
    """
    Double Exponential Moving Average

    DEMA indicator attempts to remove the inherent lag associated to Moving Averages by placing more weight on
    recent values.

    The name suggests this is achieved by applying a double exponential smoothing which is not the case.

    The name double comes from the fact that the value of an EMA (Exponential Moving Average) is doubled.

    To keep it in line with the actual data and to remove the lag the value "EMA of EMA" is subtracted from the
    previously doubled EMA.

    Because EMA(EMA) is used in the calculation, DEMA needs 2 * period -1 samples to start producing values in
    contrast to the period samples needed by a regular EMA

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('DEMA')
    return fn(data, timeperiod=period)


def EMA(data, period=30, price='close'):
    """
    Exponential Moving Average

    Like all moving average indicators, they are much better suited for trending markets.

    When the market is in a strong and sustained uptrend, the EMA indicator line will also show an uptrend and
    vice-versa for a down trend.

    EMAs are commonly used in conjunction with other indicators to confirm significant market moves and to gauge
    their validity.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :param str price: column used for indicator calculation (default = "close")
    :return pd.Series: with indicator data calculation results
    """
    return data[price].ewm(ignore_na=False, min_periods=period - 1, span=period).mean()


def HT_TRENDLINE(data, price='close'):
    """
    Hilbert Transform

    Instantaneous Trend-line

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param str price: column used for indicator calculation (default = "close")
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('HT_TRENDLINE')
    return fn(data, price)


def KAMA(data, period=20, er_period=10, fast=2, slow=30, price='close'):
    """
    Kaufman's Adaptive Moving Average

    KAMA is a moving average designed to account for market noise or volatility.

    It's main advantage is that it takes into consideration not just the direction, but the market volatility as
    well.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :param int er_period: period used for indicator calculation
    :param int fast: fast period used for indicator calculation
    :param int slow: slow period used for indicator calculation
    :param str price: column used for indicator calculation (default = "close")
    :return pd.Series: with indicator data calculation results
    """
    er = ER(data, er_period)
    fast_alpha = 2 / (fast + 1)
    slow_alpha = 2 / (slow + 1)

    # smoothing constant
    # noinspection PyTypeChecker
    sc = pd.Series((er * (fast_alpha - slow_alpha) + slow_alpha) ** 2)
    sma_ = SMA(data, period, price)

    kama_ = []

    for smooth, ma, price in zip(sc, sma_.shift(-1), data[price]):
        try:
            kama_.append(kama_[-1] + smooth * (price - kama_[-1]))
        except (IndexError, TypeError):
            if pd.notnull(ma):
                kama_.append(ma + smooth * (price - ma))
            else:
                kama_.append(None)

    return pd.Series(kama_, index=sma_.index, name='KAMA')


def MA(data, period=25, ma_type=0):
    """
    Moving Average

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :param int ma_type: moving average type (0 simple, 1 exponential)
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('MA')
    return fn(data, timeperiod=period, matype=ma_type)


def MAMA(data, fast_limit=0.5, slow_limit=0.05):
    """
    MESA Adaptive Moving Average



    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param float fast_limit: fast limit period used for indicator calculation
    :param float slow_limit: slow limit period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('MAMA')
    return fn(data, fastlimit=fast_limit, slowlimit=slow_limit)


def MAVP(data, min_period=2, max_period=30, ma_type=0):
    """
    Volume Adjusted Moving Average

    Moving average with variable period.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int min_period: min period used for indicator calculation
    :param int max_period: max period used for indicator calculation
    :param int ma_type: moving average type (0 simple, 1 exponential)
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('MAVP')
    return fn(data, minperiod=min_period, maxperiod=max_period, matype=ma_type)


def MIDPOINT(data, period=14):
    """
    Mid Point

    MidPoint over period.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('MIDPOINT')
    return fn(data, timeperiod=period)


def MIDPRICE(data, period=14):
    """
    Mid Price

    Midpoint Price over period

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('MIDPRICE')
    return fn(data, timeperiod=period)


def SAR(data, accel=0.02, max_accel=0.2):
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

    fn = Function('SAR')
    return fn(data, acceleration=accel, maximum=max_accel)


def SAREXT(data, start=0, offset_on_reverse=0, accel_init_long=0.02, accel_long=0.02,
           accel_max_long=0.2, accel_init_short=0.02, accel_short=0.02, accel_max_short=0.2):
    """
    Parabolic SAR - Extended

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
    fn = Function('SAREXT')
    return fn(data, startvalue=start, offsetonreverse=offset_on_reverse, accelerationinitlong=accel_init_long,
              accelerationlong=accel_long, accelerationmaxlong=accel_max_long,
              accelerationinitshort=accel_init_short, accelerationshort=accel_short,
              accelerationmaxshort=accel_max_short)


def SMA(data, period=25, price='close'):
    """
    Simple Moving Average

    The simple moving average (SMA) is the most basic of the moving averages used for trading.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :param str price: column used for indicator calculation (default = "close")
    :return pd.Series: with indicator data calculation results
    """
    sma = data[price].rolling(center=False, window=period, min_periods=period - 1).mean()
    return pd.Series(sma, name='sma', index=data.index)


def T3(data, period=5, v_factor=0.7):
    """
    Triple Exponential Moving Average (T3)

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :param float v_factor: v factor
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('T3')
    return fn(data, timeperiod=period, vfactor=v_factor)


def TEMA(data, period=30):
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
    fn = Function('TEMA')
    return fn(data, timeperiod=period)


def TRIMA(data, period=30, price='close'):
    """
    Triangular Moving Average (TRIMA or TMA)

    Represents an average of prices, but places weight on the middle prices of the time period.

    The calculations double-smooth the data using a window width that is one-half the length of the series.

    The TRIMA is simply the SMA of the SMA.

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :param int period: period used for indicator calculation
    :param str price: column used for indicator calculation (default = "close")
    :return pd.Series: with indicator data calculation results
    """
    tma_list = []
    sma_list = []
    i = 0
    while i < len(data[price]):
        if period % 2 == 0:
            n_sma = period / 2 + 1
            start = i + 1 - n_sma
            end = i + 1
            sma = sum(data[price][start:end]) / n_sma
            sma_list.append(sma)
            n_tma = period / 2
            start = i + 1 - n_tma
            end = i + 1
        else:
            n_sma = (period + 1) / 2
            start = i + 1 - n_sma
            end = i + 1
            sma = sum(data[price][start:end]) / n_sma
            sma_list.append(sma)
            n_tma = (period + 1) / 2
            start = i + 1 - n_tma
            end = i + 1
        if i + 1 < period:
            tma = float('NaN')
        else:
            tma = sum(sma_list[start:end]) / n_tma
        tma_list.append(tma)
        i += 1
    return pd.Series(tma_list, 'TRIMA_{:d}'.format(period))


def WMA(data, period=30, price='close'):
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
    :param str price: column used for indicator calculation (default = "close")
    :return pd.Series: with indicator data calculation results
    """
    wma_ = []

    for chunk in _chunks(data, period, price):
        try:
            wma_.append(_chunked_wma(chunk, period))
        except AttributeError:
            wma_.append(None)

    wma_.reverse()
    return pd.Series(wma_, index=data.index, name='wma')


def _chunks(data, period, price='close'):
    """
    Create "n" chunks based on the number of periods.

    :param pd.DataFrame data:
    :param int period:
    :param str price: column used for indicator calculation (default = "close")
    :return:
    """
    df_rev = data[price].iloc[::-1]

    for i in enumerate(df_rev):
        chunk = df_rev.iloc[i[0]:i[0] + period]
        if len(chunk) != period:
            yield None
        else:
            yield chunk


def _chunked_wma(chunk, period):
    """

    :param pd.DataFrame chunk:
    :param int period:
    :return float:
    """
    denominator = (period * (period + 1)) / 2

    ma = []

    for price, i in zip(chunk.iloc[::-1].items(),
                        range(period + 1)[1:]):
        ma.append(price[1] * (i / denominator))

    return sum(ma)
