"""
Pattern Recognition
"""
from talib.abstract import Function

__all__ = ['ABANDONED_BABY', 'ADVANCE_BLOCK', 'BELT_HOLD', 'BREAKAWAY', 'CLOSING_MARUBOZU', 'CONCEAL_BABY_SWALL',
           'COUNTER_ATTACK', 'DARK_CLOUD_COVER', 'DOJI', 'DOJI_STAR', 'DRAGON_FLY_DOJI', 'ENGULFING',
           'EVENING_DOJI_STAR', 'EVENING_STAR', 'Function', 'GAP_SIDE_SIDE_WHITE', 'GRAVESTONE_DOJI', 'HAMMER',
           'HANGING_MAN', 'HARAMI', 'HARAMI_CROSS', 'HIGH_WAVE', 'HIKKAKE', 'HIKKAKE_MOD', 'HOMING_PIGEON',
           'IDENTICAL_THREE_CROWS', 'INVERTED_HAMMER', 'IN_NECK', 'KICKING', 'KICKING_BY_LENGTH', 'LADDER_BOTTOM',
           'LONG_LEGGED_DOJI', 'LONG_LINE', 'MARUBOZU', 'MATCHING_LOW', 'MAT_HOLD', 'MORNING_DOJI_STAR', 'MORNING_STAR',
           'ON_NECK', 'PIERCING', 'RICK_SHAW_MAN', 'RISE_FALL_THREE_METHODS', 'SEPARATING_LINES', 'SHOOTING_STAR',
           'SHORT_LINE', 'SPINNING_TOP', 'STALLED_PATTERN', 'STICK_SANDWICH', 'TAKURI', 'TASUKI_GAP',
           'THREE_BLACK_CROWS', 'THREE_INSIDE', 'THREE_LINE_STRIKE', 'THREE_OUTSIDE', 'THREE_STARSINSOUTH',
           'THREE_WHITE_SOLDIERS', 'THRUSTING', 'TRISTAR', 'TWO_CROWS', 'UNIQUE_THREE_RIVER', 'UPSIDE_GAP_TWO_CROWS',
           'X_SIDE_GAP_THREE_METHODS', 'detect_pattern', 'get_pattern_list']


def detect_pattern(pattern, data):
    """
    Detect a candlestick pattern using a DataFrame.

    :param str pattern: name of pattern to be detected
    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: for each DataFrame entry a 100, 0 or -100 will be returned
    """
    fn = getattr(__import__(__name__), pattern)
    return fn(data)


def get_pattern_list():
    """
    Get all supported patters names as list
    :return list: patters names list
    """
    return [p for p in __all__ if p[0].isupper()]


def ABANDONED_BABY(data):
    """
    Abandoned Baby
    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLABANDONEDBABY')
    return fn(data)


def ADVANCE_BLOCK(data):
    """
    Advance Block

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLADVANCEBLOCK')
    return fn(data)


def BELT_HOLD(data):
    """
    Belt-hold

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLBELTHOLD')
    return fn(data)


def BREAKAWAY(data):
    """
    Breakaway

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLBREAKAWAY')
    return fn(data)


def CLOSING_MARUBOZU(data):
    """
    Closing Marubozu

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLCLOSINGMARUBOZU')
    return fn(data)


def CONCEAL_BABY_SWALL(data):
    """
    Concealing Baby Swallow

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLCONCEALBABYSWALL')
    return fn(data)


def COUNTER_ATTACK(data):
    """
    Counterattack

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLCOUNTERATTACK')
    return fn(data)


def DARK_CLOUD_COVER(data):
    """
    Dark Cloud Cover

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLDARKCLOUDCOVER')
    return fn(data)


def DOJI(data):
    """
    Doji

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLDOJI')
    return fn(data)


def DOJI_STAR(data):
    """
    Doji Star

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLDOJISTAR')
    return fn(data)


def DRAGON_FLY_DOJI(data):
    """
    Dragon Fly Doji

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLDRAGONFLYDOJI')
    return fn(data)


def ENGULFING(data):
    """
    Engulfing Pattern

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLENGULFING')
    return fn(data)


def EVENING_DOJI_STAR(data):
    """
    Evening Doji Star

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLEVENINGDOJISTRAR')
    return fn(data)


def EVENING_STAR(data):
    """
    Evening Star

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLEVENINGSTAR')
    return fn(data)


def GAP_SIDE_SIDE_WHITE(data):
    """
    Gap Side

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLGAPSIDESIDEWHITEITE')
    return fn(data)


def GRAVESTONE_DOJI(data):
    """
    Gravestone Doji

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLGRAVESTONEDOJII')
    return fn(data)


def HAMMER(data):
    """
    Hammer

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLHAMMER')
    return fn(data)


def HANGING_MAN(data):
    """
    Hanging Man

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLHANGINGMAN')
    return fn(data)


def HARAMI(data):
    """
    Harami Patter

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLHARAMI')
    return fn(data)


def HARAMI_CROSS(data):
    """
    Harami Cross Patter

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLHARAMICROSS')
    return fn(data)


def HIGH_WAVE(data):
    """
    High Wave Candle

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLHIGHWAVE')
    return fn(data)


def HIKKAKE(data):
    """
    Hikkake Pattern

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLHIKKAKE')
    return fn(data)


def HIKKAKE_MOD(data):
    """
    Modified Hikkake Pattern

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """

    fn = Function('CDLHIKKAKEMOD')
    return fn(data)


def HOMING_PIGEON(data):
    """
    Homing Pigeon

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLHOMINGPIGEON')
    return fn(data)


def IDENTICAL_THREE_CROWS(data):
    """
    Identical 3 Crows

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLIDENTICAL3CROWS')
    return fn(data)


def INVERTED_HAMMER(data):
    """
    Inverted Hammer

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLINVERTEDHAMMER')
    return fn(data)


def IN_NECK(data):
    """
    In-Neck Pattern

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLINNECK')
    return fn(data)


def KICKING(data):
    """
    Kicking

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLKICKING')
    return fn(data)


def KICKING_BY_LENGTH(data):
    """
    Kicking - bull/bear determined by the longer marubozu

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLKICKINGBYLENGTH')
    return fn(data)


def LADDER_BOTTOM(data):
    """
    Ladder Bottom

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLLADDERBOTTOM')
    return fn(data)


def LONG_LEGGED_DOJI(data):
    """
    Long Legged Doji

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLLONGLEGGEDDOJI')
    return fn(data)


def LONG_LINE(data):
    """
    Long Line Candle

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLLONGLINE')
    return fn(data)


def MARUBOZU(data):
    """
    Marubozu

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLMARUBOZU')
    return fn(data)


def MATCHING_LOW(data):
    """
    Matching Low

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLMATCHINGLOW')
    return fn(data)


def MAT_HOLD(data):
    """
    Mat Hold

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLMATHOLD')
    return fn(data)


def MORNING_DOJI_STAR(data):
    """
    Morning Doji Star

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLMORNINGDOJISTAR')
    return fn(data)


def MORNING_STAR(data):
    """
    Morning Star

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLMORNINGSTAR')
    return fn(data)


def ON_NECK(data):
    """
    On-Neck Pattern


    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLONNECK')
    return fn(data)


def PIERCING(data):
    """
    Piercing Pattern

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLPIERCING')
    return fn(data)


def RICK_SHAW_MAN(data):
    """
    Rickshaw Man

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLRICKSHAWMAN')
    return fn(data)


def RISE_FALL_THREE_METHODS(data):
    """
    Rising/Falling Three Methods

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLRISEFALL3METHODS')
    return fn(data)


def SEPARATING_LINES(data):
    """
    Separating Lines

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLSEPARATINGLINES')
    return fn(data)


def SHOOTING_STAR(data):
    """
    Shooting Star

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLSHOOTINGSTAR')
    return fn(data)


def SHORT_LINE(data):
    """
    Short Line Candle

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLSHORTLINE')
    return fn(data)


def SPINNING_TOP(data):
    """
    Spinning Top


    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLSPINNINGTOP')
    return fn(data)


def STALLED_PATTERN(data):
    """
    Stalled Pattern

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLSTALLEDPATTERN')
    return fn(data)


def STICK_SANDWICH(data):
    """
    Stick Sandwich

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLSTICKSANDWICH')
    return fn(data)


def TAKURI(data):
    """
    Takuri (Dragonfly Doji with very long lower shadow)

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLTAKURI')
    return fn(data)


def TASUKI_GAP(data):
    """
    Tasuki Gap

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLTASUKIGAP')
    return fn(data)


def THREE_BLACK_CROWS(data):
    """
    Three Black Crows

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDL3BLACKCROWS')
    return fn(data)


def THREE_INSIDE(data):
    """
    Three Inside Up/Down

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDL3INSIDE')
    return fn(data)


def THREE_LINE_STRIKE(data):
    """
    Three-Line Strike

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDL3LINESTRIKE')
    return fn(data)


def THREE_OUTSIDE(data):
    """
    Three Outside Up/Down

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDL3OUTSIDE')
    return fn(data)


def THREE_STARSINSOUTH(data):
    """
    Three Stars In The South
    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDL3STARSINSOUTH')
    return fn(data)


def THREE_WHITE_SOLDIERS(data):
    """
    Three Advancing White Soldiers

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDL3WHITESOLDIERS')
    return fn(data)


def THRUSTING(data):
    """
    Thrusting Pattern
    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLTHRUSTING')
    return fn(data)


def TRISTAR(data):
    """
    Tristar Pattern

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLTRISTAR')
    return fn(data)


def TWO_CROWS(data):
    """
    Two Crows

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDL2CROWS')
    return fn(data)


def UNIQUE_THREE_RIVER(data):
    """
    Unique 3 River

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLUNIQUE3RIVER')
    return fn(data)


def UPSIDE_GAP_TWO_CROWS(data):
    """


    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLUPSIDEGAP2CROWS')
    return fn(data)


def X_SIDE_GAP_THREE_METHODS(data):
    """
    Upside/Downside Gap Three Methods

    :param pd.DataFrame data: pandas DataFrame with open, high, low, close data
    :return pd.Series: with indicator data calculation results
    """
    fn = Function('CDLXSIDEGAP3METHODS')
    return fn(data)
